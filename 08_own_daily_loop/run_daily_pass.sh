#!/bin/bash
# run_daily_pass.sh — free-tier hand-run version of the Project 8 daily loop.
#
# Instead of a real daily schedule (which burns quota), this drives the SAME
# body by hand a few times. Each pass runs the deterministic checker (a command,
# not the agent, decides if there's work), stamps the spine, and logs to
# run_log.txt. Run it once per "day" for a few days to prove the six parts hold
# together — then read progress.md and trust what it shipped because you read it.
#
#   ./run_daily_pass.sh        # one pass
#   for i in 1 2 3 4; do ./run_daily_pass.sh; sleep 2; done   # 4 fake "days"

cd "$(dirname "$0")"

echo "=== daily pass start $(date '+%Y-%m-%d %H:%M:%S') ===" >> run_log.txt

# The checker — exit code tells the maker-checker whether there is new work.
python todo_sweep.py
RC=$?

if [ "$RC" -eq 0 ]; then
  echo "todo_sweep: no new work. Nothing to grade this pass." >> run_log.txt
elif [ "$RC" -eq 1 ]; then
  echo "todo_sweep: NEW stale candidates found -> hand off to the reviewer." >> run_log.txt
fi

echo "=== daily pass end $(date '+%Y-%m-%d %H:%M:%S') ===" >> run_log.txt
exit "$RC"