# 01 — Watch Loop

**Project 1 of the Loop Engineering Series**
Difficulty: easy · Time: 15–30 min · Concept: In-Session Loop

---

## Goal

Build a loop that watches a long-running task and tells you the moment it finishes — without you sitting there watching the terminal.

---

## What This Project Demonstrates

- Setting up an **in-session loop** that polls for task completion at regular intervals
- Using `/loop` to schedule recurring checks via CronCreate
- Detecting file creation as a signal that a background process has finished
- Stopping the loop cleanly once the task completes — no wasted tokens

---

## Files

| File | Purpose |
|------|---------|
| `slow_task.sh` | Simulates a long-running job (build, migration, deploy). Sleeps for 3 minutes, then writes `task_result.txt`. |
| `task_result.txt` | Output file created by `slow_task.sh` when it finishes. Serves as the completion signal. |
| `output.md` | Transcript of the loop in action — shows each polling cycle and the final detection. |
| `media/` | Screenshots documenting the project. |

---

## How It Works

### 1. Start the long task in the background

```bash
chmod +x slow_task.sh
./slow_task.sh &
```

This simulates a 3-minute background job. The `&` keeps your terminal free.

### 2. Set up the watch loop

```
/loop 1m check if task_result.txt exists in 01_watch_loop; if it does, tell me the task is done and say STOP
```

This creates a recurring cron job that:
- Checks every **1 minute** for the existence of `task_result.txt`
- Reports **"The task is done. STOP"** the moment it appears
- Stops itself after detecting completion

### 3. Walk away

The loop handles everything. No terminal-watching required.

### 4. Clean up

Once the loop reports the task is done, it automatically cancels itself. You can also cancel manually:

```
/CronDelete <job-id>
```

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `/loop 1m <prompt>` | Schedule a recurring prompt every 1 minute |
| `CronList` | View all active recurring jobs |
| `CronDelete <id>` | Cancel a specific recurring job |

---

## What "Done" Looks Like

```
● Scheduled: Check for task_result.txt in 01_watch_loop — every 1 minute
  Cron: */1 * * * * | Job ID: 0470c27c
  task_result.txt not found yet. The loop will check again in 1 minute.

  (several polling cycles...)

● task_result.txt not found yet. Still waiting.
● task_result.txt not found yet. Still waiting.
● task_result.txt not found yet. Still waiting.
● The task is done. STOP

● Loop complete — task_result.txt was found and the recurring job has been cancelled.
```

---

## Concept: In-Session Heartbeat

The **in-session loop** pattern (Concept 4) works like a heartbeat:

1. **Schedule** — Set up a recurring check at a fixed interval (e.g., every minute)
2. **Poll** — Each cycle, the loop looks for a completion signal (a file, an API response, a status change)
3. **React** — When the signal is found, the loop reports it and stops
4. **Clean up** — Cancel the cron job so it doesn't keep firing and wasting tokens

This is useful for:
- Watching builds, deploys, or migrations
- Polling for CI/CD pipeline completion
- Waiting for a file transfer or data sync
- Monitoring any background process that writes an output file

---

## Completion Criteria

✅ Long task (`slow_task.sh`) runs in the background
✅ In-session loop polls every minute for `task_result.txt`
✅ Loop detects the file and announces completion
✅ Loop stops cleanly after reporting — no wasted tokens
✅ You never had to watch the terminal

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
