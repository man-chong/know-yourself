# know-yourself

A Claude skill for finding your real patterns in your own data — then changing one
thing and measuring whether it moved.

You already have the material. Years of messages, AI chats, commits, app history.
Nobody reads their own.

---

## What it does

```
1  GATHER    find what data you actually have
2  MEASURE   find what is actually in it
3  REFLECT   ask where a pattern came from — you answer, not the AI
4  CHANGE    pick one behaviour, make it countable, set a date
5  RETURN    run the same script on that date and see if it moved
```

Phase 5 is the part other methods don't have. Most self-knowledge work ends at
insight and never finds out whether anything changed.

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
nine of those errors, each with the number that eventually exposed it. They're
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
stops the exercise and says so.

## What it won't do

- Tell you your personality type
- Infer your childhood, your attachment style, or your diagnosis
- Score you
- Give you a finding it can't show you the check for
- Keep going forever — phase 4 ends with a date, and it's instructed to stop there

That last one is deliberate. This method can run indefinitely, and for some people
running it repeatedly *is* the pattern. The skill is told to notice that and say so —
including the specific tell: someone who declines most suggestions but accepts every
single offer of a deeper analysis.

## Contents

| | |
|---|---|
| `SKILL.md` | the five phases |
| `references/1-gather.md` | where the data lives, per platform, and the dead ends |
| `references/2-measure.md` | metric definitions that survived a sensitivity check |
| `references/3-reflect.md` | how to ask about origins without inventing any |
| `references/4-change.md` | turning a finding into one measurable change |
| `references/failure-modes.md` | nine real errors and the numbers that exposed them |
| `scripts/measure.py` | the frozen ruler |

## Honest status

Built September 2026, out of one long analysis of one person's archives. The method is
tested in the sense that it survived contact with real data and produced findings that
had to be withdrawn. It is **not** validated in the sense of having been run on many
people and compared against anything.

Treat the failure modes as the reliable part. They're a record of things that actually
went wrong, and those don't get discovered twice.

MIT licensed. If you use it and it gets something wrong about you, that's worth an
issue — those are the most valuable thing this repo could receive.
