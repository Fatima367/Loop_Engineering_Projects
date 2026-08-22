# 07 — Break It on Purpose

**Project 7 of the Loop Engineering Series**
Observability + Concept 13 (cost) · Difficulty: medium · Time: 45–60 min

---

## Goal

Sabotage your own loop, then diagnose the failure from the spine alone — without replaying the full run.

---

## What This Project Demonstrates

- **Measuring cost** — how many tokens one beat reads and writes, and what that means at your cadence (Concept 13)
- **Sabotaging a loop** — making it fail on purpose so you can see what failure looks like
- **Diagnosing from the spine** — reading `progress.md` and `loop.log` to figure out what went wrong and when, without re-running anything
- **Observability** — ensuring the loop leaves behind enough signal for a human to diagnose it cold

---

## Files

| File | Purpose |
|------|---------|
| `app.py` | The loop's target — a small Python file with 3 TODO comments the loop scans for |
| `progress.md` | The spine — a running log of every scan result. What the loop left behind for diagnosis. |
| `loop.log` | Structured log lines (exit code, message, needs_human flag) — the spine's quick-look signal |
| `sabotaged_prompt.txt` | The sabotage prompt — points at a file that does not exist |
| `monthly_cost_estimate.md` | One beat's token count × cadence = monthly cost |
| `output.md` | Full transcript of the normal run and the sabotaged run side by side |

---

## How It Works

### 1. Measure one beat's cost

Run the loop's prompt once with verbose output to capture token counts:

```bash
claude -p "Read progress.md. List all TODO comments in the repo not already logged there. Append a new timestamped entry to loop.log and progress.md summarizing what you found." --allowedTools "Read,Edit" --output-format json
```

Read the token line from the JSON output. Our measurement:

- **Input:** 93,069 tokens (fresh) + 94,592 (cached)
- **Output:** 1,206 tokens
- **Total per beat:** ~188,867 tokens · **Cost:** ~$0.42

Multiply by your cadence to get monthly cost:

| Cadence | Beats/month | Monthly tokens | Monthly cost (Sonnet 5) |
|---------|-------------|----------------|--------------------------|
| Daily | 30 | 5.7M | ~$12 |
| Hourly | 720 | 136M | ~$299 |

See `monthly_cost_estimate.md` for the full breakdown across models.

### 2. Sabotage it

Edit the prompt to point at a file that does not exist:

```
claude -p "Read nonexistent-file-xyz.md, find new TODOs, append a dated summary to progress.md" --allowedTools "Read,Edit"
```

Or give it an unreachable success condition:

```
/goal All tests pass and the file impossible-marker.txt exists. Stop after 3 tries.
```

The sabotaged prompt is saved in `sabotaged_prompt.txt` for reference.

### 3. Diagnose from the spine alone

Do **not** re-run the loop. Open only these two files:

- **`loop.log`** — check the log line. What does the exit code say? What does the message say? Is `needs_human=true`?
- **`progress.md`** — read the latest entry. What did the loop report? Did it leave a clear note, or did it fail silently?

From those two signals alone, answer:
1. **What failed?** The loop tried to read `nonexistent-file-xyz.md` — the file does not exist.
2. **When?** The timestamp in the log entry tells you exactly when it fired.
3. **Did it fail silently?** No — the log line has `needs_human=true` and `progress.md` has a dated note: "Attempted to read nonexistent-file-xyz.md — file does not exist after 3 tries."

---

## What "Done" Looks Like

```
## 2026-08-21 17:45

- Attempted to read nonexistent-file-xyz.md - file does not exist after 3 tries.
```

And in `loop.log`:

```
[2026-08-21 17:45:11] exit=1 message="nonexistent-file-xyz.md does not exist after 3 tries" needs_human=true
```

No re-run needed. The spine tells the whole story.

---

## Key Concepts

### The spine

The **spine** is whatever the loop leaves behind when it finishes — log lines, progress entries, output files. A good spine lets you diagnose failures without replaying the run. If your loop fails and leaves nothing, you're flying blind.

### Observability (Concept 14)

A green status only means the session ended without an infrastructure error — **it never means the task succeeded.** You have to open the transcript and read it to know the difference. The log line + progress.md pattern makes this concrete.

### Cost (Concept 13)

Every beat has a token price. Multiply by cadence to get monthly cost. Knowing this number lets you:
- Choose the right cadence (daily vs hourly vs weekly)
- Shorten the prompt if it's too expensive
- Scope the loop smaller before it runs overnight

---

## Completion Criteria

✅ Measured one beat's token count and calculated monthly cost at your cadence
✅ Sabotaged the loop with an unreachable condition (nonexistent file or impossible goal)
✅ Loop fired, failed, and left a clear log line + progress entry
✅ Diagnosed what failed and when from the spine alone — no replay
✅ Loop left a "needs a human" note instead of failing silently

---

## Real Version (Cloud Routine)

If Project 3 is running as a live Routine, sabotage it there instead:
1. Edit the Routine's prompt to point at a nonexistent file
2. Fire it with **Run now** (not the recurring schedule)
3. Open the Routine's detail page and read the run transcript
4. Diagnose from the transcript — same spine, just hosted

This makes the lesson concrete: a green Routine status doesn't mean the task succeeded. You have to read the transcript.

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
