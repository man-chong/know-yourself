#!/usr/bin/env python3
"""
measure.py — the frozen ruler.

Copy this next to the person's notes, fill in the loaders, and KEEP IT. The point is
not this run's numbers; it is that the next run is comparable to this one. Two
measurements taken with two different definitions are two opinions, not a trend.

    python3 measure.py                                   # every corpus, all time
    python3 measure.py --window 2026-09-04 2026-09-22    # like for like
    python3 measure.py --cutoff 2026-08-25               # before / after a date

House rules, learned the hard way:

  * Do not "improve" a pattern in place. Add a NEW named metric beside it and keep
    the old one running, or the series breaks and the history becomes unusable.
  * Every loader de-duplicates, and they all de-duplicate the SAME way. Comparing a
    de-duplicated corpus against a raw one manufactures findings out of nothing.
  * Record every exclusion in a comment saying what it drops and why. Someone reading
    this in six months needs to know which filters are load-bearing.
"""
import argparse, json, os, re, glob, statistics as st, datetime as dt
from collections import Counter, defaultdict

TZ = dt.timezone(dt.timedelta(hours=8))    # set to the person's actual timezone

# ---------------------------------------------------------------- the frozen rulers
# Add the person's other languages. Hedging markers are language-specific, and a
# monolingual regex reports a bilingual person as more direct than they really are.

REQ = re.compile(r"(can you|could you|can i|could i|would you|do you think"
                 r"|what do you think|should (i|we)|is it (possible|ok|okay)"
                 r"|shall we|may i|do we need|pls can|please can)", re.I)
DIR = re.compile(r"^\s*(pls |please |now |just |go |do |make |build |add |remove "
                 r"|delete |fix |change |update |write |create |run |check |use |put "
                 r"|move |keep |stop |start |give |show |find |read |set |rename"
                 r"|destroy|leave it)", re.I)
CONCEDE = re.compile(r"(you'?re right|you are right|i was wrong|my (bad|mistake)"
                     r"|i'?m wrong|i made a mistake|fair enough|good point)", re.I)
OFFER = re.compile(r"(want me to|shall i|should i|do you want|say the word"
                   r"|tell me which|let me know if|would you like)", re.I)
ACK   = re.compile(r"^\s*(yes|yeah|ok|okay|sure|do it|go|pls|please|go ahead"
                   r"|sounds good|let'?s|try it|run it|do that)\b", re.I)
NO    = re.compile(r"^\s*(no\b|nope|don'?t|do not|skip|leave it|forget it|nah)", re.I)

HABITS = [
    ('asks "what do you think"', r"(what do you think|do you think|your opinion|wdyt)"),
    ('admits not knowing',       r"\b(i don'?t (know|understand)|teach me|how (do|can) i"
                                 r"|where can i|explain)"),
    ('thanks',                   r"\b(thank|thanks|thx|appreciate)"),
    ('apologises',               r"\b(sorry|my bad|apolog)"),
    ('softeners',                r"\b(pls|please|maybe|perhaps|if possible|a bit)"),
    ('laughing',                 r"(haha|lol|🤣|😂)"),
    ('corrects the other side',  r"\b(that'?s wrong|you'?re wrong|is wrong|outdated"
                                 r"|not correct)"),
]

# ------------------------------------------------------------------------- loaders
# Each returns (messages, offers):
#   messages = [(iso_timestamp, thread_or_session_id, text_the_person_typed)]
#   offers   = [(what_the_other_side_offered, what_came_back)]   -- '' if no reply
#
# See references/1-gather.md for real paths, real formats, and the traps in each.

def load_assistant_transcripts():
    """JSONL assistant logs. Skip agent sub-runs; they are not conversations."""
    msgs, offers = [], {}       # dict keyed on offer text == de-duplication
    # for f in glob.glob(os.path.expanduser('~/.claude/projects/**/*.jsonl'), recursive=True):
    #     if '/subagents/' in f: continue
    #     ...
    return msgs, list(offers.items())

def load_chat_exports(paths):
    """WhatsApp 'Export Chat -> Without Media' text files."""
    LINE  = re.compile(r'^\[(\d{1,2})/(\d{1,2})/(\d{4}), (\d{1,2}):(\d{2}):(\d{2})\] ([^:]+): (.*)$')
    # Media placeholders are not messages. One real export held 27,242 stickers on a
    # single day, most at identical timestamps — it dominated every count it touched.
    MEDIA = re.compile(r'^\s*(sticker|image|audio|video|document|GIF|Contact card'
                       r'|This message was deleted)\s*(omitted)?\s*$', re.I)
    ME = 'REPLACE_WITH_THEIR_NAME_IN_THE_EXPORT'
    out = []
    for p in paths:
        cur = None
        for line in open(p, encoding='utf-8', errors='replace'):
            line = line.replace('‎', '').replace('‏', '').rstrip('\n')
            m = LINE.match(line)
            if m:
                d, mo, y, H, M, S, who, txt = m.groups()
                cur = [dt.datetime(int(y), int(mo), int(d), int(H), int(M), int(S)),
                       who.strip() == ME, txt]
                out.append(cur)
            elif cur:
                cur[2] += ' ' + line       # a message that wrapped onto its own line
        thread = os.path.basename(os.path.dirname(p))
        for t, mine, txt in out:
            if mine and not MEDIA.match(txt.strip()) and 'end-to-end encrypted' not in txt:
                yield (t.isoformat(), thread, txt)

CORPORA = {
    # 'Assistant': load_assistant_transcripts,
    # 'People':    lambda: (list(load_chat_exports(glob.glob('exports/*/_chat.txt'))), []),
}

# -------------------------------------------------------------------------- report
def rulers(rows, label):
    v = [t for _, _, t in rows]
    if not v: return
    req  = sum(1 for t in v if REQ.search(t))
    dirc = sum(1 for t in v if DIR.match(t) and not REQ.search(t))
    print(f"  {label:<26}{len(v):>7}{len({r[1] for r in rows}):>7}{req:>7}{dirc:>8}"
          f"{req/max(1,dirc):>8.2f}{sum(1 for t in v if CONCEDE.search(t)):>7}"
          f"{100*sum(1 for t in v if '?' in t)//len(v):>6}%{sum(len(t) for t in v)//len(v):>8}")

def refusals(offers, label):
    """Deciding against something, and whether it was ever said out loud."""
    if not offers:
        return print(f"  {label:<26}{'— no counterpart transcript —':>42}")
    c = Counter()
    for _, reply in offers:
        c['silent' if not reply
          else 'refused' if NO.match(reply)
          else 'taken'  if ACK.match(reply) or len(reply) < 25
          else 'silent'] += 1
    n = sum(c.values())
    print(f"  {label:<26}{n:>7}{c['taken']:>8}{c['silent']:>9} ({100*c['silent']//n:>2}%)"
          f"{c['refused']:>7} ({100*c['refused']/n:>4.1f}%)")

def walkaways(rows):
    """When they stop. Gaps are per thread — a global gap just measures session ends."""
    w, prev = Counter(), {}
    for ts, tid, _ in sorted(rows):
        cur = dt.datetime.fromisoformat(ts.replace('Z', '+00:00'))
        if cur.tzinfo is None: cur = cur.replace(tzinfo=TZ)
        if tid in prev and (cur - prev[tid]).total_seconds() >= 7200:
            w[prev[tid].astimezone(TZ).hour] += 1
        prev[tid] = cur
    return w

def by_year(rows, label):
    """When a habit first shows up — its rate per year, with volume so thin years show.
    The archive's first year is not the habit's first year: if it's there from the start,
    all you know is that it's at least that old."""
    per = defaultdict(list)
    for ts, _, t in rows: per[ts[:4]].append(t)
    if not per: return
    years = sorted(per)
    print(f"\n  {label} by year — archive begins {min(r[0] for r in rows)[:10]}")
    print(f"  {'':<26}" + ''.join(f"{y:>8}" for y in years))
    print(f"  {'messages':<26}" + ''.join(f"{len(per[y]):>8}" for y in years))
    for hlabel, pat in HABITS:
        print(f"  {hlabel:<26}" + ''.join(
            f"{100*sum(1 for t in per[y] if re.search(pat, t, re.I))/max(1, len(per[y])):>7.1f}%"
            for y in years))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cutoff', default=None, help='split one corpus before/after this date')
    ap.add_argument('--window', nargs=2, metavar=('FROM', 'TO'),
                    help='restrict every corpus to the same dates — the like-for-like run')
    ap.add_argument('--by-year', action='store_true',
                    help='each habit per year — when it first shows up (phase 3 uses this)')
    a = ap.parse_args()

    if not CORPORA:
        raise SystemExit("Fill in CORPORA first — see references/1-gather.md for real paths.")

    data = {name: fn() for name, fn in CORPORA.items()}
    if a.window:
        data = {n: ([r for r in m if a.window[0] <= r[0][:10] <= a.window[1]], o)
                for n, (m, o) in data.items()}
        print(f"window {a.window[0]} .. {a.window[1]}")

    print(f"\n{'':<28}{'msgs':>7}{'threads':>7}{'asks':>7}{'orders':>8}{'ratio':>8}"
          f"{'conc':>7}{'?':>7}{'chars':>8}")
    print('  ' + '-' * 78)
    for name, (msgs, _) in data.items():
        rulers(msgs, name)
        if a.cutoff:
            rulers([r for r in msgs if r[0] < a.cutoff],  f'  · before {a.cutoff}')
            rulers([r for r in msgs if r[0] >= a.cutoff], f'  · after  {a.cutoff}')

    print(f"\n{'deciding against things':<28}{'offers':>7}{'taken':>8}{'silent':>13}{'said no':>15}")
    print('  ' + '-' * 78)
    for name, (_, offers) in data.items():
        refusals(offers, name)

    print(f"\n{'habit':<28}" + ''.join(f"{n[:10]:>12}" for n in data))
    print('  ' + '-' * (26 + 12 * len(data)))
    for label, pat in HABITS:
        print(f"  {label:<26}" + ''.join(
            f"{100*sum(1 for _,_,t in m if re.search(pat, t, re.I))//max(1,len(m)):>11}%"
            for m, _ in data.values()))

    for name, (msgs, _) in data.items():
        w = walkaways(msgs)
        if not w: continue
        print(f"\n  where {name} stops (gaps >= 2h, by hour) — total {sum(w.values())}")
        peak = max(w.values())
        for h in range(24):
            if w[h]: print(f"    {h:02d}:00 {'#' * max(1, 30*w[h]//peak)} {w[h]}")

    if a.by_year:
        for name, (msgs, _) in data.items():
            by_year(msgs, name)

if __name__ == '__main__':
    main()
