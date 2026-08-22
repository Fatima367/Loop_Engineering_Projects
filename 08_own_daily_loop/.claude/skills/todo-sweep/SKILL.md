---
name: todo-sweep
description: Daily chore — flag TODO/FIXME comments in the repo older than 30 days, log them, and grade the change before opening a PR. Use when doing the daily sweep.
---

1. Run the checker first: `python todo_sweep.py`. It already finds stale TODO/FIXME comments and appends the new candidates to `progress.md`.
2. Read the candidates it reported. For each stale item, make the smallest sensible change (fix it, or remove it if it's obsolete).
3. Do not touch test files.
4. Have the reviewer agent grade the diff — open a PR only on PASS.
5. Confirm `progress.md` picked up the run, and stop after 1 review round under free tier.