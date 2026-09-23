# Phase 2 — Measure: metrics that survived scrutiny

Definitions that held up under sensitivity checks, with the reasoning. Copy them
rather than inventing equivalents — the point of a shared definition is that a
measurement taken in March is comparable to one taken in December.

If one of these is genuinely wrong for a given person, add a new named metric
alongside it and keep the old one running. Silently redefining a metric destroys the
series, and the series is where most of the value is.

---

## Timing

**The best metric in this whole method**, because nobody can self-report it and it
needs no interpretation.

- **Hour-of-day histogram** of messages, commits, or events, in local time.
- **Flatness** — the ratio of the busiest hour to the quietest. A normal person's
  activity has a shape; a peak-to-trough near 1.5 means no part of the day is off,
  which is a real and rare finding.
- **Walk-aways** — gaps of ≥2 hours mid-session, recorded at the hour the gap *began*.
  This answers "when do you stop," which is usually more interesting than when they
  start. Track gaps per session or per thread, never globally, or you measure the
  boundary between sessions instead.

Timing findings get much stronger when the same shape appears in unrelated archives.
One real case: 41% of commits between midnight and 07:00, 30% of messages in the same
window, walk-aways peaking at 02:00 and 07:00, and a completely flat app-usage curve —
four independent sources, four years, one conclusion.

## Register: request vs. instruction

How often someone hedges an ask rather than stating it. Meaningful only *within* a
context, and the ratio between two contexts is the real result.

```python
REQ = re.compile(r"(can you|could you|can i|could i|would you|do you think"
                 r"|what do you think|should (i|we)|is it (possible|ok|okay)"
                 r"|shall we|may i|do we need|pls can|please can)", re.I)
DIR = re.compile(r"^\s*(pls |please |now |just |go |do |make |build |add |remove "
                 r"|delete |fix |change |update |write |create |run |check |use |put "
                 r"|move |keep |stop |start |give |show |find |read |set |rename"
                 r"|destroy|leave it)", re.I)
# a message counts as an instruction only if it isn't also a hedged request
ratio = n_req / max(1, n_dir)
```

Add the person's other languages. Hedging markers are language-specific and a
monolingual regex will report a bilingual person as more direct than they are.

## Concession rate

Messages containing "you're right", "I was wrong", "my mistake", "good point", or the
equivalent. Often literally zero over thousands of messages, which is itself the
finding. Cheap to compute and one of the few metrics where the *absence* is the result.

## The silent decline

Strong, and genuinely invisible to the person.

Find every offer the other party made — "want me to", "shall I", "say the word",
"tell me which", "would you like" — near the end of a message. Classify what came back:

- **taken** — an acknowledgement, or anything under ~25 characters
- **refused** — begins with no / don't / skip / leave it / nah
- **dropped** — a substantive reply that simply doesn't mention the offer

In one real case: 252 offers, 62% dropped in silence, **2% refused out loud**. The
person was deciding constantly and saying so almost never — and the rate was the same
(65%) with a completely different AI tool, which is what made it credible.

**De-duplicate offers by text before counting**, and make sure both sides of any
comparison are de-duplicated the same way. This exact metric is where the two-rulers
error happened.

## Message runs — only with content classification

Counting consecutive messages sent without a reply is easy and **means nothing on its
own**. Roughly 89% of such runs are just fragmented typing. Always classify by content:

```python
SUMMON = r"^\s*(hi+|hey+|hello+|bb+|yo|喂+|在|u there|you there|here|awake)[\s\?!.]*$"
WHYQ   = r"^\s*(why+|點解|做咩|wtf|what happened|咩事|answer me|回我|覆我)[\s\?!.]*$"
FILLER = r"^[\s.。,，…·\-~!！?？\d]*$|^[emoji ranges]+$"
SORRY  = r"(sorry|對唔住|my fault|我錯|i'?m sorry|apolog)"

# >=40% summons/why  -> PURSUIT
# >=2 apologies      -> REMORSE
# >=50% filler       -> FILLER
# contains a link    -> SHARING
# mean length >=25   -> ARGUMENT
# otherwise          -> CHATTER  (this will be the overwhelming majority)
```

Report the categories separately. "1,528 bursts" is misleading; "15 instances of
pursuit in 11 years" is true and completely changes the conclusion.

## Reply latency

Median minutes to reply, computed separately for each side, per thread. Cap at ~72
hours so an abandoned thread doesn't dominate.

The **ratio between the two sides within a thread** is the interesting number —
consistently answering faster than the other person is a real signal about investment.
Aggregate latency across all contacts usually comes out even and says little.

## Effort balance

Per thread: share of messages sent, and mean characters each side. Large asymmetries
in either direction are worth naming — they describe a relationship's shape without
requiring any inference about anyone's feelings.

## Change over time

Bin by year or half-year, require a minimum volume per bin (150+ messages) so sparse
periods don't produce noise, and z-score within each thread before pooling across
threads — otherwise thread-level differences swamp the within-thread trend.

For anything causal-sounding, run the lagged version in both directions. See
failure-modes.md §7: a strong contemporaneous correlation had zero lagged effect in
either direction, and the causal reading would have been both wrong and cruel.

## Cross-corpus comparison

The strongest design available here, because the person is the constant and only the
context varies.

Run identical metrics over two archives from different contexts, restricted to the
same date window. Differences are attributable to the context.

Real example, same three weeks:

| | to people | to Claude | to Codex |
|---|---|---|---|
| average length | 5 chars | 391 | 197 |
| question mark | 2% | 36% | 35% |
| hedged ask | 0.2% | 18% | 20% |

Two things follow. The habits that hold steady across contexts are characterological.
The ones that swing are situational — and describing a situational trait as a
personality is the most damaging mistake this method can make.
