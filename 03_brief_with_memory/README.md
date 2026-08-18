# 03 — The Morning Brief with a Memory

**Project 3 of the Loop Engineering Series**
Difficulty: medium · Time: 45–60 min · Concepts: Scheduled Heartbeat + The Spine

---

## Goal

Build a scheduled loop that runs, reads its own memory (`progress.md`), gathers new findings from the repo (open TODO comments), writes a summary, and — on the second run — proves it remembers what it already recorded instead of starting from scratch.

---

## What This Project Demonstrates

- Setting up a **scheduled heartbeat** that fires on demand (simulating a daily cron)
- Using **the spine** pattern: read state → act → write state
- Proving loop memory by running twice — the second run must not repeat the first
- Updating a shared memory file (`progress.md`) with dated entries across runs

---

## Files

| File | Purpose |
|------|---------|
| `app.py` | Mock Python code containing TODO comments — the "findings" the loop scans for |
| `progress.md` | The spine's memory file. Starts empty; each run appends a dated entry summarizing what it found. |
| `output.md` | Transcript of all three runs — shows the loop building on its own memory each time. |

---

## How It Works

### 1. Seed the repo with TODOs and an empty spine

```bash
cat > app.py << 'EOF'
# TODO: add input validation here
def process(x):
    return x * 2

# TODO: handle the empty-list case
def total(items):
    return sum(items)
EOF

cat > progress.md << 'EOF'
# Progress Log

(empty — first run will populate this)
EOF

git add -A && git commit -m "seed repo with TODOs and empty progress.md"
```

### 2. Run the brief (first time)

```
Read progress.md. List all TODO comments currently in the repo that are not already logged in progress.md. Append a new dated entry to progress.md summarizing what you found. Do not repeat anything already logged.
```

**What happens:** `progress.md` is empty, so every TODO in `app.py` is new. The loop logs both TODOs with a timestamp:

```
## 2026-08-18 18:37:53
- app.py:1 — # TODO: add input validation here
- app.py:6 — # TODO: handle the empty-list case
```

### 3. Run the exact same command again

**What happens:** The loop reads `progress.md`, sees both TODOs are already logged, and writes:

```
## 2026-08-18 18:47:27
No new unlogged TODOs found since last run.
```

**This is the spine proof.** The second run didn't start from nothing — it read its own memory and recognized what was already recorded.

### 4. Add a new TODO and run a third time

```bash
# TODO: implement deduplication logic
def deduplicate(items):
    return list(set(items))
```

**What happens:** The loop finds one new TODO that isn't in `progress.md` yet and appends it:

```
## 2026-08-18 18:56:15
- app.py:11 — # TODO: implement deduplication logic
```

---

## The Spine Pattern

This project teaches **the spine** (Concept 12) — the three-step skeleton every loop with memory must follow:

```
┌─────────────┐
│   READ      │  ← Load progress.md (what do I already know?)
├─────────────┤
│   ACT       │  ← Scan repo for new findings (what changed since last time?)
├─────────────┤
│   WRITE     │  ← Append a dated entry to progress.md (what did I find?)
└─────────────┘
```

Without the **read** step, the loop has no memory and repeats itself every time. With it, the loop builds on its own history — each run starts where the last one left off.

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `/loop 5m <prompt>` | Schedule a recurring prompt every 5 minutes |
| `CronList` | View all active recurring jobs |
| `CronDelete <id>` | Cancel a specific recurring job |
| `cat progress.md` | View the spine's memory file |

---

## Going Further: Real Cron with `claude -p`

The spine pattern above runs inside a Claude Code session. But the same idea works on your own machine's crontab — no cloud, no `/loop`, just a local scheduled prompt.

`claude -p` runs a single prompt and then exits. Drop it straight into your computer's crontab:

```bash
claude -p "check the files for any TODOs" --allowedTools "Read,Edit" >> claude-cron.log 2>&1
```

**What this does:** Every time the cron fires, Claude reads the repo, applies the spine (read → act → write), and appends its output to `claude-cron.log`. The log file is the audit trail — you can see exactly what it found and when.

**Example crontab entry** (run daily at 9 AM):

```
0 9 * * * cd /path/to/your/repo && claude -p "Read progress.md. List any new TODO comments in the repo not already logged. Append a dated entry to progress.md." --allowedTools "Read,Edit" >> claude-cron.log 2>&1
```

The key difference from the in-session `/loop`: this runs as a standalone process on your laptop. It's a real scheduled loop — not a simulation — that wakes up, reads its memory, and goes back to sleep.

---

## What "Done" Looks Like

```
## Run 1 — 2026-08-18 18:37:53
2 new TODOs found (both in app.py). Logged.

## Run 2 — 2026-08-18 18:47:27
No new TODOs since last run. Spine confirmed working.

## Run 3 — 2026-08-18 18:56:15
1 new TODO found (app.py:11). Logged alongside prior entries.
```

The second run is the key moment: it says **"no new TODOs"** instead of re-discovering the same ones. That's proof the loop has a memory.

---

## Concept: Scheduled Heartbeat + The Spine

This project combines two concepts:

**Concept 6 — Scheduled Heartbeat:** A loop that fires at regular intervals (daily, hourly, every 5 minutes). Here we simulate it by running the same command multiple times by hand, but in production you'd use `/schedule` or a system cron.

**Concept 12 — The Spine:** Every loop that remembers something must follow the read → act → write skeleton. The memory file (`progress.md`) is the spine's backbone — it's what turns a stateless command into a loop that learns.

Together they create a loop that:
1. Wakes up on a schedule
2. Reads what it already knows
3. Checks for anything new
4. Updates its memory with the delta

This is the foundation for daily triage bots, changelog generators, and any automated process that needs to avoid repeating itself.

---

## Completion Criteria

✅ Spine file (`progress.md`) starts empty
✅ First run discovers and logs all existing TODOs with a timestamp
✅ Second run reads `progress.md` and reports "no new TODOs" — proving memory works
✅ Third run finds and logs only the newly added TODO — no duplication
✅ Each entry is dated, creating an auditable trail of observations

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
