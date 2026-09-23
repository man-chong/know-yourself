# Phase 1 — Gather: where the data actually lives

Checked on macOS, September 2026. Paths drift; the shape of each finding tends not to.

The recurring surprise is that **platform exports contain far less than people expect**.
Inventory first and say the real number out loud — someone expecting thirteen years and
getting thirteen months should hear that before any analysis, not after.

## Contents

- [AI assistant transcripts](#ai-assistant-transcripts)
- [Messaging](#messaging)
- [Platform data downloads](#platform-data-downloads)
- [Local behavioural traces](#local-behavioural-traces)
- [Dead ends](#dead-ends)

---

## AI assistant transcripts

Usually the easiest corpus to get and the most misleading to interpret, because it is
entirely one register: the person at work, directing a machine, in whatever language
they use for work.

### Claude Code
`~/.claude/projects/<dir-slug>/*.jsonl` — JSONL, one object per line, keyed by the
**project directory**, not the account. Also `~/.claude/CLAUDE.md` for standing
instructions the person wrote about themselves.

**Trap:** subdirectories named `subagents/` contain agent sub-runs, not conversations.
In one case 260 of 307 files were subagent transcripts, and counting files instead of
sessions inflated the session count roughly fivefold. Filter on the path.

Rows have `type` of `user` / `assistant` / `system` / `attachment`. A `type: "user"`
row is frequently *not* something the person typed — tool results, hook output, slash
command echoes, and system reminders all arrive this way. Filter on content:

```python
def typed_by_me(o):
    m = o.get('message', o); c = m.get('content')
    if isinstance(c, list) and any(b.get('type') == 'tool_result' for b in c if isinstance(b, dict)):
        return False
    t = text(m).strip()
    if not t or o.get('isMeta'): return False
    return not any(j in t[:150] for j in
                   ('<system-reminder', '<local-command', '<command-name', 'Caveat:',
                    '<user-prompt', '[Request interrupted'))
```

Claude Code prunes old sessions. If the person has a manual archive, it will hold
sessions the live directory no longer does — merge, de-duplicating by `sessionId` and
keeping the longer copy.

### Codex
`~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`. Rows are `{type: "response_item",
payload: {role, content}}`. Also `~/.codex/memories/memory_summary.md`, which is the
model's own written profile of the person — genuinely useful as an independent second
opinion, since it was written without reference to your analysis.

**Trap:** Codex rewrites the entire thread into a fresh rollout file on every resume.
Raw message counts are inflated — in one case 719 → 471 after de-duplicating on exact
message text. This matters enormously when comparing against another corpus: comparing
de-duplicated Codex against non-de-duplicated Claude manufactured a significant result
out of nothing.

### Grok CLI
`~/.grok/sessions/%2FUsers%2F<user>/prompt_history.jsonl` is the clean one — flat rows
of `{timestamp, session_id, prompt}`. Per-session `updates.jsonl` files hold
`user_message_chunk` events but cover far fewer sessions. Drop prompts starting
`Grok said:` or with a shell prompt — those are pasted back, not typed.

### ChatGPT / Gemini
Not local. ChatGPT: Settings → Data controls → Export. Gemini: Google Takeout. Both
arrive as JSON by email, usually within hours.

---

## Messaging

This is the register the AI transcripts don't cover, and it is where the real
comparison lives. It is also the most sensitive material a person will hand over.

### WhatsApp — the desktop database
`~/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite`

Unencrypted Core Data. `ZWAMESSAGE` (`ZTEXT`, `ZMESSAGEDATE`, `ZISFROMME`,
`ZCHATSESSION`) joined to `ZWACHATSESSION` (`ZPARTNERNAME`, `ZSESSIONTYPE` — 0 is
one-to-one, 1 is a group). Timestamps are Core Data seconds: add 978307200 for Unix.

**Trap:** the Mac client syncs roughly a year. Session *metadata* survives much
longer, so `ZWACHATSESSION` will show contacts going back a decade with no messages
attached — which makes the database look far deeper than it is. Check content, not
session rows.

**Trap:** SQLite compares a number against a string by type order, so
`ZMESSAGEDATE < strftime('%s', '2025-01-01')` silently matches everything. Convert to
a number in Python and substitute it in.

### WhatsApp — chat exports (better)
On the phone: the chat → the contact name → **Export Chat → Without Media** → save to
Files. Lands in iCloud Drive and appears on the Mac. Contains the **full history for
that thread**, often many years further back than the desktop database, and needs no
device pairing.

Format is `[DD/MM/YYYY, HH:MM:SS] Name: text`, with wrapped messages continuing on
unprefixed lines — append those to the previous message or long messages get lost.
Strip U+200E and U+200F first. Drop `<x> omitted` placeholders before any analysis
(see failure-modes.md for the sticker incident).

For a person's whole history: Finder backup of the phone (needs "Trust This Computer"
and the passcode), then extract `ChatStorage.sqlite` from the backup via `Manifest.db`,
domain `AppDomainGroup-group.net.whatsapp.WhatsApp.shared`. This is a much bigger
privacy footprint than a few exports — the backup is the entire phone — so prefer
targeted exports unless the whole corpus is genuinely needed.

### iMessage
`~/Library/Messages/chat.db`. Requires Full Disk Access; without it the connection is
refused outright. Worth checking whether the person actually uses it — outside the US
they often don't, and a large file can be years of near-silence.

### Telegram / WeChat / Signal / LINE
Local stores exist and are large, but are in proprietary or encrypted formats. Use
each app's own export where one exists. Not worth reverse-engineering.

---

## Platform data downloads

Request under GDPR/CCPA from the app's settings. Usually arrives within days.

The pattern across all of them: **the interesting fields are stripped.** Expect
telemetry with timestamps and geography, and expect message content to be absent.
That's still useful — timing is one of the most self-invisible things there is — but
set expectations before the file arrives.

A real example: a 150 MB Grindr export contained 57,338 analytics events, all with
timestamps, city and device, and no `event_type` field. The chat report was three rows
of metadata. What remained was still the sharpest finding in the whole run (a
completely flat 24-hour usage curve), but nothing about *what* the person did.

Instagram and Facebook exports do include message content. Google Takeout covers
Search, YouTube, Location and Gmail separately — select carefully or it's enormous.

---

## Local behavioural traces

**Git** — `git log --author=<name> --date=format:'%H'` piped to a counter gives
hour-of-day work patterns for free, going back years, with no export needed. One of
the highest-value-per-effort sources available.

**Screen Time** — `~/Library/Application Support/Knowledge/knowledgeC.db`. App usage
and device sessions. Needs Full Disk Access.

**Shell history** — `~/.zsh_history`. Often nearly empty; check the line count before
planning anything around it.

---

## Dead ends

- **iOS app sandboxes.** There is no path to browse to another app's database on the
  phone. Only the app itself (via its export) or a full device backup.
- **WhatsApp's iCloud backup.** Encrypted; only WhatsApp can restore it.
- **"Request account info"** on WhatsApp returns account metadata, not messages.
- **GitHub personal accounts** have no audit log. Reads and clones are invisible.
  Only Team/Enterprise accounts record them.
