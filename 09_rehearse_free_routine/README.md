# 09 — Rehearse a Routine for Free

**Project 9 of the Loop Engineering Series**
Difficulty: easy · Time: 20–30 min · Concept: One-Off Schedules & Reading Runs

---

## Goal

Prove a prompt works with one-off runs (free, don't count against your daily cap) before committing it to a real schedule.

---

## What This Project Demonstrates

- Firing a routine with a **one-off schedule** (`/schedule tomorrow at 9am` or **Run now**) — zero cost against your daily cap
- Reading the **full transcript** of a run, not just the status column
- Breaking a prompt **on purpose** to see what failure looks like
- Understanding the **A5 lesson**: green status means the session ended without an infrastructure error — nothing more

---

## Files

| File | Purpose |
|------|---------|
| `prompt_success.txt` | The working prompt — summarizes yesterday's commits onto a `claude/summary` branch |
| `prompt_broken.txt` | The broken prompt — asks to read a file that doesn't exist, guaranteeing failure |
| `seed_commits.sh` | Helper script that creates dated commits so the "summarize yesterday" prompt has real data |
| `output.md` | Transcript of both runs — one green success, one green failure — with the lesson |
| `summary.md` | The output Claude produced from the successful run |

---

## How It Works

### 1. Seed some commits (if your repo is fresh)

```bash
chmod +x seed_commits.sh
./seed_commits.sh
```

This creates backdated commits so "summarize yesterday's commits" has something to work with.

### 2. Fire the working prompt (one-off run)

**Via Claude CLI:**

```bash
claude -p "summarize yesterday's commits, write to summary.md onto a claude/summary branch" --allowedTools "Read,Edit,Bash"
```

**Via Routines UI:**

```
/schedule tomorrow at 9am, summarize yesterday's commits onto a claude/summary branch
```

Or click **Run now** in the routines UI. Either way — zero cost against your daily cap.

### 3. Read the full transcript

Don't just glance at the green checkmark. Open the transcript and verify:
- Did it actually find commits?
- Did it create the summary correctly?
- Did it write to the right branch?

### 4. Break it on purpose

Fire this prompt as another one-off run:

**Via Claude CLI:**

```bash
claude -p "Read a file called this-file-does-not-exist.md and summarize its contents into a new summary file onto a claude/summary branch." --allowedTools "Read,Edit,Bash"
```

**Via Routines UI:**

```
/schedule now, Read a file called this-file-does-not-exist.md and summarize its contents onto a claude/summary branch
```

### 5. Compare the two runs

Both runs show **green** in the status column. But one actually succeeded and one actually failed.

---

## What "Done" Looks Like

```
Run 1 (success):
  Status: ✅ green
  Transcript: Claude read git log, created summary.md, committed to claude/summary branch.

Run 2 (failure):
  Status: ✅ green
  Transcript: "The file this-file-does-not-exist.md does not exist. There's nothing to summarize."
```

Both green. One worked. One didn't.

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `/schedule <time>, <prompt>` | Fire a one-off run at a specific time |
| **Run now** (routines UI) | Fire immediately — no schedule needed |
| Full transcript view | The only way to know if a run truly succeeded |

---

## The A5 Lesson

**Why the status column couldn't tell them apart:**

> Green means the session ended without an infrastructure error — nothing more. It does not mean the task succeeded.

A prompt that reads a nonexistent file and gracefully says "file not found" exits cleanly. The session didn't crash. Infrastructure worked fine. Status: green. But the task failed.

Only the **full transcript** reveals the difference.

---

## Completion Criteria

✅ Working prompt fired as a one-off run — transcript confirms success

✅ Broken prompt fired as a one-off run — transcript confirms failure

✅ Both runs show green in the status column

✅ You can explain in one sentence why green status is not proof of success

---

## Note on Cost

Projects 9–12 use the real cloud Routine mechanism. One-off schedules and **Run now** fires don't count against your daily Routine cap, so this section is naturally close to free.

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
