# A6 Checklist — Project 11's Two Routines

Run this checklist over **both** routines (A: draft, B: execute) before trusting the gate.

## 1. Connectors pruned

- [ ] Only the connectors this routine actually needs are enabled
- [ ] Anything that can reach out — comments, pushes, branches — is scoped to the routine's stated job
- [ ] Routine B cannot contact anything except the repo it's attached to

## 2. Unrestricted pushes off

- [ ] **Allow unrestricted branch pushes** is OFF for both routines
- [ ] Routine A may only write to `claude/*` (its draft branch) — never `main`
- [ ] Routine B may write only to `claude/publish` — never `main`
- [ ] Merging to `main` is NOT possible from either routine config

## 3. A state file chosen

- [ ] A single state file records the gate crossing (default: `draft_approved.txt`)
- [ ] Routine A writes its draft to that state file on `claude/draft`
- [ ] Routine B reads the state file, then **does not re-read it** (no accidental double-fire)
- [ ] The state file is enough to tell, between runs, whether the draft is "pending" or "approved"

## 4. (Bonus) The human gate is real

- [ ] B fires **only** when I fire it (API trigger) — never on its own schedule
- [ ] B's bearer token was stored the moment it was shown (it is shown once)
- [ ] I actually read A's draft before firing B — the gate is a human decision, not a rubber stamp

---

