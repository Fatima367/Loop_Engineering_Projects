#!/bin/bash
# seed_commits.sh — create commits dated "yesterday" and "today" so the
# "summarize yesterday's commits" prompt has real data to work with.
#
# Run this inside the throwaway repo you use for Project 9:
#   ./seed_commits.sh

YESTERDAY=$(date -d "yesterday" +%Y-%m-%dT%H:%M:%S 2>/dev/null || date -v-1d +%Y-%m-%dT%H:%M:%S)
TODAY=$(date +%Y-%m-%dT%H:%M:%S)

echo "# mock repo for the rehearsal drill" > mock.md
git add mock.md

# Commit dated yesterday (author and committer).
GIT_AUTHOR_DATE="$YESTERDAY" GIT_COMMITTER_DATE="$YESTERDAY" \
  git commit -m "feat: add feature X" --date "$YESTERDAY"

echo "" >> mock.md
echo "change" >> mock.md
git add mock.md

# Commit dated today.
GIT_AUTHOR_DATE="$TODAY" GIT_COMMITTER_DATE="$TODAY" \
  git commit -m "fix: typo in mock" --date "$TODAY"

echo
echo "Seeded. Verify with:"
echo "  git log --oneline --since=yesterday --until=tomorrow"
git log --oneline --since="yesterday" --until="tomorrow"