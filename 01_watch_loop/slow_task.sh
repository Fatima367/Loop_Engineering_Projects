#!/bin/bash
# simulates a long-running job (a build, a migration, a deploy)
sleep 180   # 3 minutes — long enough to prove the watch works, short enough not to burn quota
echo "Done" > task_result.txt
echo "Task finished at $(date)"