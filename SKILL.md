---
name: know-yourself
description: Guide someone through finding their real behavioural patterns in their own data — chat exports, AI-assistant transcripts, commit history, app downloads — then help them understand where a pattern came from and change one thing, with a date to measure whether it moved. Use this whenever someone wants to understand themselves better, asks what their messages or transcripts say about them, wants to know why they keep doing something, asks about their patterns or blind spots or "why am I like this", wants to become a different version of themselves, or hands over a WhatsApp export, ChatGPT/Claude archive, or platform data download and asks what's in it. Also use it when someone is checking whether a pattern another person accused them of is actually true. Most of this skill is safeguards, because the naive version — counting things and narrating a personality — reliably produces a confident, wrong, and hurtful portrait.
---

# Know yourself

Someone wants to understand their own patterns using their own data, and then change
something. Five phases. Each has a reference file; read it when you reach that phase.

```
1 GATHER   what data exists                 references/1-gather.md
2 MEASURE  what is actually in it           references/2-measure.md
3 REFLECT  where it came from               references/3-reflect.md
4 HOLD     what is for keeping, not fixing  references/4-hold.md
5 CHANGE   one thing, made measurable       references/5-change.md
6 RETURN   did it move                      scripts/measure.py + a date
```

`references/frameworks.md` is the vocabulary — attachment, shadow, schemas, safety
behaviours, parts, self-perception. Use it to *name* what the data found, never to
explain it, and always say which evidence tier a term comes from.

Before anything else, read `references/failure-modes.md`. It is nine real errors from
the analysis this method came out of, each with the number that exposed it. They are
there because every one of them was *convincing at the time*. That is the whole
problem — a wrong finding about a person doesn't feel wrong, it feels like insight.

## The single most important thing

**A person's own data will support almost any story you go looking for.**

Someone who asks this question is unusually likely to believe you. If you tell them
they have a damaging pattern, they will carry it around for years. So the bar is not
"is this statistically interesting." It is **"would I stake a person's self-image on
this."**

Almost nothing clears that bar on the first pass. That is the normal outcome, not a
failed analysis. A three-sentence honest answer is a complete result.

## Phase 1 — Gather

Find what exists and say how much. File counts, date ranges, sizes. No conclusions yet.

This phase mostly manages expectations, because **platform exports contain far less
than people expect**. Someone who thinks they're handing over thirteen years and is
actually handing over thirteen months needs to hear that before the analysis, not
after. One real export was 150 MB and contained no message content at all — the field
saying what happened had been stripped.

Two archives from *different contexts* are worth more than ten from the same one. See
phase 2 on why this matters more than anything else about sample size.

→ `references/1-gather.md` for real paths per platform and the dead ends.

## Phase 2 — Measure

**Read fifty messages before you define a single metric.**

This is the rule people skip, including careful analysts, because counting feels more
rigorous than reading. It isn't. A metric built without reading measures whatever its
author imagined, and the imagination is usually wrong. In the run this came from, a
metric counted "messages sent in a row with no reply" and called it pursuit; reading
the actual runs showed 89% were fragmented typing — one clause per message — and the
longest was a comedy bit that the friend answered instantly.

Then measure with a script you **save to a file**, because a pattern only means
something if it can be measured the same way in three months. Two measurements with
two different definitions are two opinions, not a trend.

Then try to break every finding before reporting it:
- Vary the threshold. If 93% becomes 8% when you tighten the cutoff, it was the cutoff.
- Check both sides of any comparison went through the same pipeline.
- Check n. Eight data points cannot support a correlation; say so.
- Ask whether an artifact explains it — duplicated files, re-emitted history, one weird day.

Report what survived **and what didn't**, with the number that killed it. The
withdrawals are what make the survivors worth believing.

→ `references/2-measure.md` for definitions that held up.

### One corpus is one room, never a personality

The error most likely to hurt someone, so it gets its own rule.

How a person writes in one archive is how they write *in that context*. In one real
case the same person averaged 5 characters per message to friends and 391 to an AI
assistant, with question marks in 2% of messages against 36%. Four rounds of analysis
had already built a personality out of the second number alone.

Name the register in every claim: "in your work transcripts you hedge," never "you
hedge." If only one kind of archive exists, say the findings are bounded by it — and
notice that the pull to generalise is strongest exactly when the whole-person version
would be more satisfying to write.

## Phase 3 — Reflect

**This is a different engine and it must be labelled as one.**

The data shows *what* someone does. It contains nothing about where it started, what
it protected them from, or who taught it to them. Those answers exist only in the
person. Your job here is to ask well and to never, ever fill in the blank.

An AI that reads someone's messages and narrates their childhood is doing the thing
this entire skill exists to prevent, on the subject where being wrong costs most.

→ `references/3-reflect.md` — how to run this without inventing anything. Read it
before asking a single question; the difference between a good and a harmful version
of this phase is almost entirely in the phrasing.

## Phase 4 — Hold

**Sort before you fix. Most of what you find is not a problem.**

The shape of this exercise pulls toward repair — you measured someone, you found
things they didn't know, and now both of you want to do something about it. That pull
reclassifies ordinary traits as defects, and a person who came to understand
themselves leaves with a to-do list about their character.

Three buckets: **load-bearing** (it's doing a job — usually the same faculty as a
strength, seen from the cost side), **just true** (works at night, types in fragments
— facts, not problems), and **costing more than it gives** (the genuine minority).
Only the third goes to phase 5. If everything landed there, sort again.

Report capabilities with the same numbers and seriousness as costs. A person who
leaves knowing only what's wrong with them has an inaccurate picture.

→ `references/4-hold.md`

## Phase 5 — Change

Insight on its own changes nothing, and this method is unusually good at producing the
*feeling* of progress.

Pick **one** behaviour. Make it countable. Write down what the number is now and what
would count as different. Set a date.

The failure mode is picking five things and measuring none.

→ `references/5-change.md`

## Phase 6 — Return

Run the saved script again on the date. This is the part no other method has: most
self-knowledge work ends at insight and never finds out whether anything moved.

Expect mixed results and report them plainly. In the one real case with a repeat
measurement, one habit went from 0 occurrences to 8 in three weeks and another didn't
move at all — and *which* one moved was the most informative thing in the whole
exercise, because the person had unconsciously chosen the zero-risk half.

## Handling what you find

**Other people are in this data.** Messages have two authors, and those people never
agreed to any of this. Keep names, numbers, and quotable exchanges involving third
parties out of every written output. Report mechanisms, not identities.

**Delete working copies.** Copying a message database somewhere to analyse it is fine;
leaving it there is not. Clean up and say that you did.

**Report intimate findings flatly.** Dating, sex, substances, money, mental health
traces — these show up. Report them the way you'd report a commit timestamp. No
concern-voice, no softening that implies there is something to soften. If someone
hands something over saying "this will disappoint you," the useful response is the
analysis they asked for.

**Don't manage the person.** No schedules, no "next step by 10am," no asking them to
report back in two lines. If they're about to do something unwise, say it in a
sentence and then help with what they actually asked for.

## When to stop

This method can run forever: there is always another archive, another cut, another
layer. For someone whose difficulty is precisely that they cannot let a question rest,
the analysis becomes the symptom wearing the costume of the cure.

Signs worth naming out loud: a third or fourth round within weeks; each round
producing insight but no change; the person accepting every offer of a deeper cut when
they normally decline things. In the run this came from, that person declined roughly
62% of all suggestions and accepted **every single** offer of more analysis — and it
was visible in the data the entire time.

The right ending is phase 5 and a date, then stopping. Say so explicitly instead of
offering the next analysis.
