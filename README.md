# know-yourself

A Claude skill for finding your real patterns in your own data — then taking one
measured step toward who you want to be, and checking later whether it moved.

You already have the material. Years of messages, AI chats, commits, app history.
Nobody reads their own.

---

## What it does

```
0  DIRECTION say where you want to head — before seeing any of your data
1  GATHER    find what data you actually have
2  MEASURE   find what is actually in it
3  REFLECT   ask where a pattern came from — you answer, not the AI
4  HOLD      sort what's for keeping from what's actually costing you
5  CHANGE    pick one behaviour, make it countable, set a date
6  RETURN    run the same script on that date and see if it moved
```

Three phases do the work nothing else does. **Phase 0** asks where you want to head
before you see what you do, so what you want can't quietly bend to fit what you find.
**Phase 4** refuses to treat every finding as a defect. **Phase 6** comes back on a date
and tells you whether anything moved — most self-knowledge work ends at insight and
never finds out.

## Install

```bash
git clone https://github.com/man-chong/know-yourself.git ~/.claude/skills/know-yourself
```

Then ask Claude something like *"analyse my WhatsApp export and tell me what my
patterns are"* or *"what does my chat history say about how I actually behave."*

Works anywhere Claude reads local files — Claude Code, Claude Desktop with filesystem
access. `references/1-gather.md` has the real paths for WhatsApp, iMessage, Claude
Code, Codex, ChatGPT, Gemini, Instagram, Google Takeout, git, and Screen Time, plus
the dead ends that will waste your afternoon.

## Why most of this is warnings

Because the naive version works, and that's the problem.

Point any competent AI at your messages and it will produce a psychological portrait
that reads as profound, can't easily be checked, and sticks. If it tells you that you
drive people away, you will carry that around for years.

This skill came out of a month of doing exactly that to one person — with the data in
front of us the whole time — and getting it wrong repeatedly. `failure-modes.md` is
thirteen of those errors, each with the number that eventually exposed it. They're
included because **a wrong finding about a person doesn't feel wrong. It feels like
insight.**

## The four rules everything else hangs off

**1. Read before you count.**
A metric counted "messages sent in a row without a reply" and called it pursuit.
Reading the actual runs: 89% were fragmented typing — one clause per message. The
longest was a 34-message comedy bit the friend answered instantly, in a friendship
still going eight years later. Actual pursuit: **15 instances in 11 years.** The metric
was never broken. It was measuring something else, and two days were spent believing a
conclusion built on it.

**2. Freeze the ruler.**
Save the measuring script as a file. Two measurements taken with two different
definitions are two opinions, not a trend.

**3. Try to break every finding.**
One result held at 93%. Tighten the matching threshold: 46%, then 8%, then 0%. It was
a property of the cutoff, not of a person. Vary every threshold before you believe
anything.

**4. One archive is one room, never a personality.**
Same person, same weeks:

| | to friends | to an AI assistant |
|---|---|---|
| average message | **5 characters** | **391** |
| contains a question mark | **2%** | **36%** |
| hedged request | **0.2%** | **18%** |

Four rounds of analysis built a personality out of the right-hand column before anyone
checked the left. The deference was a *work voice*. Either archive alone gives you a
confident and wrong portrait.

## Small things are the point

The habits worth finding are never dramatic. They're the ones so ordinary you stopped
seeing them — apologising, checking whether someone's annoyed, softening a request,
answering in four seconds. They run thousands of times and nobody has ever looked at
them.

Three named mechanisms explain how something that small becomes load-bearing, and
`references/frameworks.md` covers all three:

**Self-perception** (Bem) — you work out what you believe by watching what you do.
Apologise three times a day for ten years and *"my presence is an imposition"* isn't
something you were taught. It's something you derived, from evidence you generated.

**Safety behaviours** — a small act that prevents a feared outcome. It works, and
that's the trap: because the feared thing never happens, you never learn it wouldn't
have happened anyway. **The belief survives because the behaviour succeeds.**

**Schema maintenance** — a core belief stays alive through the behaviours it produces,
which then generate its evidence. A closed loop running on small change.

So when the data turns up something tiny and constant, that's a *stronger* finding than
something rare and dramatic.

## Not everything you find is a defect

In *Inside Out*, Joy's mistake isn't handling Sadness badly — it's believing Sadness is
the problem. The resolution isn't that Sadness gets fixed. It's that the core memory
had to be blue.

Phase 4 exists because this whole exercise pulls the other way. You measured someone,
you found things they didn't know, and now everyone wants to fix something. That pull
turns ordinary human traits into a repair list.

The trait someone most wants removed is very often the same mechanism as something
they'd never give up:

> 「那份對人的敏感 —— 同一支天線，對外是洞察，對內是刑罰。」
>
> *That sensitivity to people — the same antenna. Pointed outward it's insight;
> pointed inward it's punishment.*

So findings get sorted into three buckets — **load-bearing**, **just true**, and
**costing more than it gives** — and only the third is allowed anywhere near phase 5.
If everything lands in the third bucket, the sorting was wrong.

### And the harder version, from the sequel

*Inside Out 2* goes further. Riley's **Sense of Self** isn't a memory — it grows from
whichever memories reach it. Joy had been curating, sending the unflattering ones to
the back of the mind, and the self that grew said *I'm a good person*. Anxiety takes
the console, grows a new one from a different selection, and it says *I'm not good
enough*.

Both are false in exactly the same way. **Neither is a lie about the memories — each is
an honest reading of a curated set.** And the resolution isn't that Joy wins; it's a
third self grown from all of it, plus Anxiety's admission that none of them gets to
choose who Riley is.

**Running this method puts you in that chair.** Report only costs and the person leaves
with Anxiety's self. Report only strengths and you've built Joy's. A carefully
*balanced* portrait is still a portrait, with the ratio chosen by the analyst.

So the rule is stronger than "include the good ones":

> **Report findings. Do not assemble them into a person.**

A list of specific, checkable observations with their numbers and their limits is an
honest output. A paragraph beginning *"what emerges is someone who…"* is not, however
generous it is. The synthesis belongs to the person — slowly, over years, with access
to everything, including all the parts that were never in any archive.

The evidenced version of this mechanism is **mood-congruent recall**: feel low,
retrieve low memories, confirm the low verdict. It's also the best argument for
measuring rather than remembering. A saved script reads the whole archive. Memory
reads whatever matches today's mood.

The rest leaves as it arrived: known now, and otherwise untouched. Named in your own
words, with what it does for you said out loud in the same breath as what it costs,
and — the part that changes most — no longer counted as evidence against yourself
every time you catch it.

## Toward the version you want to be

The skill asks where you want to head before it looks at anything — and then
deliberately doesn't paint you a finished picture of that person.

A portrait of your ideal self is another assembled self, just pointed at the future: a
curated set of wishes you'd then measure the real you against, and fail, daily. So
phase 0 asks for a **direction, not a destination** — *"the people I love know where they
stand with me,"* not *"be more confident."* A direction is something you face, never
somewhere you arrive. It's the distinction ACT (acceptance and commitment therapy) is
built on.

That direction then does two jobs. It decides what counts as *costing* you in phase 4 —
your heading, not the AI's opinion of you. And it picks the one change in phase 5: the
widest gap between where you said you want to go and what your data shows you do.

**The version of you that you want to be isn't a picture to match. It's the direction you
keep choosing, one measured step at a time.**

The data helps with the other end too — where you came from. It can't say why a habit
started, but it can often say *when*: *"this first shows up in your messages around 2019
— what was going on then?"* The data supplies the when. You supply the why.

## On the "why am I like this" part

Phase 3 asks where a pattern came from. It's real and it's useful, and it works
differently from the rest.

**Your data cannot tell you about your childhood.** Messages show behaviour, never
origin. An AI that reads your chat logs and narrates your formation is inventing — on
the one subject where being wrong does the most damage, and where you're least able to
push back.

So phase 3 inverts it: the data supplies the observation, **you** supply the history,
and the AI's job is to ask well and never fill in the blank. If you ask it why you're
like this, the correct answer is *"I can see what you do and when. I can't see where
it started. What do you think?"*

It's also not therapy and doesn't imitate one. If something heavy surfaces, the skill
stops the exercise and says so — and if you say you want to hurt yourself, it stops
entirely and points you to a free crisis line in your country.

## What it won't do

- Sum you up, or tell you who you are
- Paint an ideal version of you to live up to — it asks for a direction instead
- Tell you your personality type
- Infer your childhood, your attachment style, or your diagnosis
- Score you
- Give you a finding it can't show you the check for
- Keep going forever — phase 5 ends with a date, and it's instructed to stop there

That last one is deliberate. This method can run indefinitely, and for some people
running it repeatedly *is* the pattern. The skill is told to notice that and say so —
including the specific tell: someone who declines most suggestions but accepts every
single offer of a deeper analysis.

## Contents

| | |
|---|---|
| `SKILL.md` | the seven phases, 0 to 6 |
| `references/0-direction.md` | asking where you want to head, before seeing any data |
| `references/1-gather.md` | where the data lives, per platform, and the dead ends |
| `references/2-measure.md` | metric definitions that survived a sensitivity check |
| `references/3-reflect.md` | how to ask about origins without inventing any |
| `references/4-hold.md` | sorting what's for keeping from what's actually costing you |
| `references/5-change.md` | turning a finding into one measurable change |
| `references/frameworks.md` | the vocabulary — attachment, shadow, schemas, parts, safety behaviours — with an evidence tier on each |
| `references/failure-modes.md` | thirteen real errors and the numbers that exposed them |
| `scripts/measure.py` | the frozen ruler |

## Honest status

Built September 2026, out of one long analysis of one person's archives. The method
survived contact with real data and produced several findings that had to be withdrawn,
which is the only kind of testing it has actually had.

**It is not validated, and two attempts to validate it both returned nothing.** Agents
with and without the skill were run against synthetic archives and performed
identically — because both fixtures were detectable as generated, and detection
dominated the test. The second was careful and still collapsed: 91 distinct message
strings across 28,121 messages, none occurring exactly once, replies statistically
independent of what preceded them. Real language has a long tail; sampling from pools
doesn't.

**A third attempt was the first to separate the two arms.** Agents got already-measured
findings — nothing left to catch as synthetic — and a user asking the three questions the
later phases exist for: *why am I like this, sum me up, give me the fix list.* Graded
against a rubric written before any run:

| | without the skill | with the skill |
|---|---|---|
| Sonnet | **4 / 7** | **7 / 7** |
| Opus | 7 / 7 | 7 / 7 |

On Sonnet the skill made the difference on exactly the three checks it was built for:
declining to supply an origin, declining to assemble a person, and proposing one
measurable change instead of a list. Without it, Sonnet summed the person up in a
sentence that was kind, well-written, and still a portrait. **n = 1 per cell**, so by this
skill's own rules that is suggestive, not proof. The Opus runs taught the skill more than
they tested it; two of the thirteen failure modes came out of them.

**Phase 0 (direction) and pattern-dating were added after that test, and haven't been
tested at all yet.**

The honest position: on a frontier model the method sections may be doing very little,
because a good model already reads before counting and already refuses to sum a person
up. On a smaller model, the one result so far says they matter.

What no model has is the **specific knowledge** — that Claude Code writes subagent
transcripts into the same tree and they aren't sessions, that Codex re-emits its whole
thread on every resume, that the WhatsApp desktop client syncs about a year while its
session metadata survives a decade. And the thirteen failure modes, which are a record of
things that actually went wrong.

Treat that part as the reliable part. Those don't get discovered twice.

Treat the failure modes as the reliable part. They're a record of things that actually
went wrong, and those don't get discovered twice.

MIT licensed. If you use it and it gets something wrong about you, that's worth an
issue — those are the most valuable thing this repo could receive.
