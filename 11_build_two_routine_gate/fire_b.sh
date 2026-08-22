#!/bin/bash
# fire_b.sh — fire Routine B through its API trigger, once you've approved A's draft.
#
# Fill in the two placeholders BEFORE running:
#   ROUTINE_B_ID    the routine's id (from the URL or the `/fire` example)
#   ROUTINE_B_TOKEN the bearer token shown ONCE when you created B's API trigger —
#                   copy it the moment it appears; it will not be shown again.
#
#   ./fire_b.sh
#
# (Paid-tier real version. The free-tier substitute is the two opencode steps
#  in the README — the human gate is you choosing to run the second command.)

ROUTINE_B_ID="REPLACE_WITH_ROUTINE_B_ID"
ROUTINE_B_TOKEN="REPLACE_WITH_ROUTINE_B_BEARER_TOKEN"

if [ "$ROUTINE_B_ID" = "REPLACE_WITH_ROUTINE_B_ID" ] \
   || [ "$ROUTINE_B_TOKEN" = "REPLACE_WITH_ROUTINE_B_BEARER_TOKEN" ]; then
  echo "!! Set ROUTINE_B_ID and ROUTINE_B_TOKEN in fire_b.sh first." >&2
  exit 1
fi

echo "Firing Routine B ($ROUTINE_B_ID)..."
curl -s -X POST "https://api.anthropic.com/v1/claude_code/routines/${ROUTINE_B_ID}/fire" \
  -H "Authorization: Bearer ${ROUTINE_B_TOKEN}" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Approved by me on review."}'

echo
echo "done — check Routine B's transcript for the PR it opened."