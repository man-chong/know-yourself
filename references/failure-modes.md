# Failure modes

Every entry below is a real error from the analysis this method came out of, with the
number that exposed it. They are here because each one was *convincing* at the time —
that is the whole problem. A wrong finding in this domain doesn't feel wrong. It feels
like insight.

Read this before reporting a finding you're pleased with.

---

## 1. Counting without reading

**The big one.** 62,081 messages across 11 years were measured — burst lengths, reply
latencies, correlations, a significance test — before a single message was read.

The headline metric counted "runs of consecutive messages sent with no reply in
between" and called it pursuit. Reading the actual runs:

| what they turned out to be | share |
|---|---|
| fragmented chatter — one clause per message | **89%** |
| sharing links | 4% |
| filler: dots, emoji, no words | 4% |
| **actual pursuit** | **1.5%** |

The longest "burst" was a 34-message run of rhyming Cantonese abuse — a comedy bit the
friend answered instantly, in a friendship still going eight years later. The
runner-up was 54 consecutive full stops, answered with "Fk u" and a laugh.

The metric was measuring **typing style**, not behaviour. Every downstream finding
inherited the error, and a person spent two days believing he had a pattern that
damages his relationships, on the strength of it.

**The fix is cheap and boring:** open fifty messages and read them before defining any
metric. Then read a sample of whatever the metric flags, and check it flagged the
thing you meant.

## 2. Two rulers, one comparison

A difference was reported at 5.6× with p = 0.008. It came from comparing a
**de-duplicated** corpus against a **non-de-duplicated** one — the divisor on one side
was inflated. Measured identically on both sides: 2.4×, p = 0.109. Not significant.

Any time two groups differ, check that both went through the same pipeline before
believing the difference. Different filtering on the two sides manufactures effects
reliably and invisibly.

## 3. Findings that are really threshold settings

"93% of dropped threads he later returns to." Sensitivity check:

```
≥30% keyword overlap → 93%
≥50%                 → 46%
≥65%                 →  8%
≥75%                 →  0%
```

Not a finding. A property of the cutoff.

**Vary every threshold before reporting anything built on one.** If the result moves
that much, the correct output is "no result," and that is a perfectly good thing to
report.

## 4. Counting files instead of things

"164 sessions" was a file count. 260 of the files were subagent sub-runs, not
conversations. The true number was 32 for the period in question — off by a factor of
five, and it had already been written into three documents as a fact.

Before any count becomes a claim, confirm one row is one of the thing being counted.

## 5. One weird day

A thread appeared to contain a single unbroken run of 27,242 messages. It was stickers
— most at identical timestamps, on one day in 2019. That single day also accounted for
nearly all of one year's message volume in that thread.

Always look at the extreme value directly. Distributions in personal data are full of
one-day artifacts, and they distort means, maxima and any "longest ever" claim.

## 6. n = 8

Eight relationships were compared against six candidate predictors. Best correlation
was r = +0.53, presented initially as though it meant something. With n = 8 the
threshold for p < 0.05 is r = 0.71.

Small-n correlations are a coin flip with extra steps. Report n alongside every r, and
if n is small, say "no predictor survives" rather than ranking noise.

## 7. Contemporaneous read as causal

Within relationships over time, bursting and slow replies correlated at r = +0.60 over
34 thread-years — strong, and p < 0.001.

The obvious story was "his bursting drives people away." Lagged test across 42
consecutive half-year transitions:

```
bursting  → their delay next period    r = +0.04
their delay → bursting next period     r = −0.10
```

Both zero. The two co-occur; neither predicts the other. The obvious story was wrong,
and it was the story the person most feared was true about themselves.

**Where a finding implies blame, test the lag before implying it.** This one is worth
extra care because the causal version is always the more compelling write-up.

## 8. Generalising from one register

The deepest error, and the one that took longest to catch. Four rounds of analysis
built a psychological portrait — deferential, hedging, never asserting — from
AI-assistant transcripts alone.

Then the messaging archive:

| | to people | to an AI assistant |
|---|---|---|
| average message | **5 chars** | **391** |
| contains a question mark | **2%** | **36%** |
| hedged ask | **0.2%** | **18%** |
| swearing | **3%** | **0%** |

Same person, same months. The deference was a **work voice**, and a whole personality
had been inferred from it without anyone checking whether it generalised.

**A single corpus supports claims about a person in that context. Nothing more.** Say
so in the writeup, every time, even when it makes the finding less satisfying — and
notice that "less satisfying" is exactly the pressure that causes this error.

## 9. Letting the analysis become the symptom

Four analyses in a month, three withdrawn findings, six written entries — for a person
whose identified difficulty was that he could not let an unresolved question rest.
Each round was individually justified. Together they were the pattern, running with
assistance.

Worth noticing: this person declined roughly 62% of suggestions in general, and
accepted **every single** offer of a deeper analysis. That asymmetry was visible in
the data the whole time.

**If someone accepts every offer of more, that is information.** Name it, set a date
for the next measurement, and stop offering.

## 10. Manufacturing harshness on request

"Be honest with me." "Don't soften it." "I'd rather hear the brutal version."

That framing is an invitation to invent severity, and complying feels like integrity.
It isn't — it's fabricating in the direction the person is already braced for, which is
the direction they will most readily believe.

The request is usually sincere and worth honouring, but what it actually asks for is
**no flinching**, not more damage. If the findings are mild, the honest answer is mild
findings delivered without hedging. If the data can't support a verdict, saying so
plainly *is* the unsoftened version.

Watch for the tell in your own draft: an adjective doing work no number supports.

## 11. Testing a method on data you generated yourself

Two attempts were made to validate this skill against synthetic message archives.
Both failed, and not because the skill failed — because the fixtures were detectable
and detection dominated the result. Agents with and without the skill performed
identically, so the tests discriminated nothing.

The second fixture was careful: jittered timestamps, weighted vocabulary, uneven days,
1,032 active days across four years. It still collapsed under inspection —
**91 distinct message strings across 28,121 messages, none occurring exactly once, and
replies statistically independent of what preceded them.** Real language has a long
tail and real replies answer things; sampling from pools produces neither.

A third attempt fixed the fixture problem by handing agents already-measured findings,
so there was nothing to catch as synthetic — and hit a different leak. The author's own
global instructions load into every test agent, so a fictional user's findings got read
as the author's: one baseline quoted the author's real work history back at a stranger.
Any test that runs on the author's machine inherits the author's context. Say so when
reporting it, and don't credit the skill for insight the context file supplied.

The general lesson is worth more than the specific one. **A method that only ever meets
data its author built has not been tested.** The honest status of a tool in that state
is "unvalidated," and saying so is more useful than a passing test against a fixture
that was never going to fail it.

## 12. A zero with nothing to read

A finding said the person had **never once disagreed with a friend in writing** — zero
hits across 29,500 messages, thresholds varied, samples read. It looked solid.

It wasn't measured at all. The search phrases were 10–16 characters long ("I disagree",
"that's not right"); the person's median message to friends was **6 characters**. Half
the messages physically couldn't contain a match, and bursts split a phrase across two
messages where it can't match either. The usual check — *read samples of what was
flagged* — was useless, because **there were no hits to sample.**

An absence is the one finding reading can't verify. Before believing a zero, search in
the words the person actually uses — the short forms, the slang, the other languages —
and read a handful of conversations end to end looking for the thing by hand. Until
then, report it as *unmeasured*, not as *zero*. "I never disagree with my friends" is a
self-concept, and it shouldn't be built on a search that couldn't have found anything.

## 13. The denominator doing the talking

Three versions of one error, all from the same findings sheet:

**Units that don't match.** 4.1% of messages to friends contained an apology; 7.8% of
messages to ChatGPT did. "I apologise even more to a machine" follows — except one
thought on WhatsApp is a burst of five fragments, and on ChatGPT it's one long message.
Per message, the two rooms aren't the same unit. Counted per turn, the order could flip.

**A trigger with no base rate.** "Check-ins usually follow a friend going quiet for 6+
hours" — while 38% of the person's own messages went out between 23:00 and 04:00. Any
friend who sleeps goes quiet for six hours most nights. Until you know how often
ordinary messages *also* follow a gap like that, there's no trigger, just a clock.

**One thread posing as a pool.** One friendship held 22,000 of the 29,500 messages. A
pooled rate across "six friends" was mostly one relationship.

In each case the numerator was right and the conclusion came from the denominator.
Ask of every rate: *per what?* And is the "what" the same on both sides?

