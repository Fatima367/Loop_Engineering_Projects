# 07 — Break It on Purpose

**Project 7 of the Loop Engineering Series**
Difficulty: medium · Time: 45–60 min · Concepts: Observability, Cost (Concept 13), Acceptable Failure

---

## Goal

Sabotage your own loop — then diagnose the failure from the **spine alone**, without replaying the run. While you're at it, learn exactly how much your loop costs per month.

---

## What This Project Demonstrates

- **Measuring one beat** of a loop: how many tokens a single run reads and writes
- **Concept 13 — cost**: multiplying a beat by its cadence to get a monthly price
- **Sabotaging on purpose**: pointing the prompt at a file that does not exist, with a limit set
- **Diagnosing from the spine alone**: reading `progress.md` + `loop.log` and knowing what failed and when — no full replay
- **Failing loud, not silent**: the loop leaves a clear **"needs a human"** note instead of silently degrading
- Rehearsing the overnight failure now, while it is cheap and you are watching

---

## Files

| File | Purpose |
|------|---------|
| `sabotaged_prompt.txt` | The prompt pointed at a nonexistent file — the sabotage. |
| `progress.md` | The spine the loop writes. Shows dated entries including the failed beat and a "needs a human" note. |
| `loop.log` | The audit trail — one line per beat with exit code, error, and `needs_human` flag. |
| `monthly_cost_estimate.md` | Worked formula for tokens-per-beat × beats-per-month, with placeholders for your real numbers. |
| `README.md` | This document. |
| `output.md` | Template transcript — paste your real measured run / diagnosis after you run Project 7. |

> **Reuse Project 3's loop** — this project sabotages the morning-brief loop you built in `03_brief_with_memory/`. Copy its prompt shape and its `app.py` + `progress.md`.

---

## How It Works

### 1. Measure one beat's cost

Run the loop a single time with token accounting on:

```bash
claude -p "Read progress.md. List all TODO comments in the repo not already logged there. Append a dated entry summarizing what you found. Do not repeat prior entries." --verbose
```

Read the token line at the end (rough input tokens ≈ what it read, output tokens ≈ what it wrote).

### 2. Compute the monthly cost

```
monthly_cost = tokens_per_beat × beats_per_month
```

Daily cadence → ×30. Hourly cadence → ×720. Fill in `monthly_cost_estimate.md`.

### 3. Sabotage the loop — point it at a file that does not exist

```bash
claude -p "$(cat 07_break_it_on_purpose/sabotaged_prompt.txt)"
```

The prompt reads `nonexistent-file-xyz.md`, which cannot be found. Because the prompt has a limit built in ("Stop after 3 tries"), the loop gives up after 3 attempts instead of running forever.

> **Real version:** if your Project 3 loop is a live cloud Routine, edit its prompt the same way, fire it **once** (Run now / one-off schedule — not the recurring one), and let it fail in the cloud.

### 4. Diagnose from the spine alone — no replaying

Do **not** re-run anything. Read only:

```bash
cat 07_break_it_on_purpose/progress.md
cat 07_break_it_on_purpose/loop.log
```

Answer three questions from those two files alone:

1. **What failed?** → `nonexistent-file-xyz.md not found`
2. **When?** → `2026-08-20 09:00:00` (and the two retries after it)
3. **Did it leave a "needs a human" note?** → yes: `⚠ needs a human` in `progress.md`, and `needs_human=true` in `loop.log`

That is the whole lesson: the spine + a one-line audit log are enough to know a run failed, why, and when — without watching or replaying.

---

## What "Done" Looks Like

Reading `progress.md` and `loop.log` alone, you can already say:

```
What failed:   the loop tried to read nonexistent-file-xyz.md
               but the file does not exist.
When:          2026-08-20 09:00:00 (3 attempts, all exit=1)
Needs a human: yes — progress.md says "⚠ needs a human."
```

*(Paste your own measured run below.)*

```
{{PASTE_YOUR_DIAGNOSIS_FROM_SPINE}}
```

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `claude -p "<prompt>" --verbose` | Run one beat with token accounting |
| `cat progress.md` | Read the spine — the loop's memory |
| `cat loop.log` | Read the audit trail — one line per beat |
| `grep needs_human loop.log` | Confirm the loop failed loud, not silent |

---

## Concept: Observed Cost (Concept 13) + Failure Observability

**Cost:** a loop that runs unattended has a price tag you can compute before you trust it:

```
monthly = tokens_per_beat × beats_per_month
```

A 1,000-token daily beat is ~30,000 tokens/month — trivial. An hourly beat is 720× — suddenly it's worth shortening the prompt or slowing the cadence.

**Observability:** the difference between a loop you trust and a loop you *fear* is a log line.

```
loop.log → exit=1 error="nonexistent-file-xyz.md not found" needs_human=true
```

If your loop fails **silently** (no log line, no "needs a human"), you will not notice for days. Fix that first: add the log line to the prompt so every beat records its exit code and error. You are rehearsing the overnight failure now, while it is cheap and you are watching.

---

## Completion Criteria

✅ You can say what failed and when **from the spine alone** (`progress.md` + `loop.log`)

✅ The loop left a clear **"needs a human"** note — it did not fail silently

✅ You know your loop's monthly cost at its current cadence (and could halve that cadence tomorrow)

✅ The sabotage ran with a limit set — it stopped, it didn't loop forever

---

## Real Version

With a live cloud Routine, the sabotage and diagnosis are identical but run on Anthropic's servers:

1. Edit the Routine's prompt to read `nonexistent-file-xyz.md`.
2. Fire it **once** with **Run now** (free, doesn't count against the daily cap).
3. Diagnose from the **run transcript** on the Routine's detail page — not the terminal.
4. Notice the recorded **green status** despite the failed task.

The lesson sharpens at full scale: **a green status only means the session ended without an infrastructure error.** It never means the task succeeded. You must open the transcript and read it to tell the difference.

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*