# 11 — Build the Two-Routine Gate

**Project 11 of the Loop Engineering Series**
Difficulty: medium–hard · Time: 1–2 hrs · Concepts: API Trigger, The Human Gate, Maker-Checker, A6 Checklist

---

## Goal

Build a gate where Routine A drafts a proposal, **a human decides**, and only that decision fires Routine B. This is the maker-checker loop from Part 5, built with real parts: a draft-only routine, an API-triggered execute routine, and you in the middle.

---

## What This Project Demonstrates

- **Routine A** on a one-off schedule drafts something reviewable (a changelog entry) to a `claude/` branch — never to `main`
- **Routine B** with an **API trigger** performs one small follow-up action — and runs **only when you fire it**
- **You as the human gate**: you review A's draft, then approve it by firing B
- The **A6 checklist**: connectors pruned, unrestricted pushes off, a state file chosen
- Local practice without paid plan: the gate is you choosing to run the second command

---

## Files

| File | Purpose |
|------|---------|
| `routine_a_prompt.txt` | Routine A's prompt — drafts, never merges. |
| `routine_b_prompt.txt` | Routine B's prompt — reads the approved entry, appends to CHANGELOG, opens a PR. |
| `fire_b.sh` | Fires Routine B's API trigger with the curl call (fill in B's id + one-time bearer token). |
| `draft_approved.txt` | The state file — the approved one-line changelog entry B consumes. |
| `CHANGELOG.md` | Where B appends the approved entry. |
| `a6-checklist.md` | The mandatory checklist for both routines before trusting the gate. |
| `.github/workflows/gate-a-draft.yml` · `gate-b-execute.yml` | GitHub Actions templates that model the gate (project-local; do not activate without a key). |
| `README.md` | This doc |

---

## How It Works

### 1. Routine A — drafts only

Create Routine A with `routine_a_prompt.txt` and a **one-off** trigger (e.g. "in 2 minutes"):

> Draft a one-line changelog entry for the most recent commit and post it as a comment on a claude/draft branch. Do not merge or push to main.

A writes the draft to `draft_approved.txt` on `claude/draft`. It cannot touch `main` (unrestricted pushes off).

### 2. You review the draft (the human gate)

Read what A proposed:

```bash
cat drafts/draft_approved.txt   # or wherever A put it
```

If it's wrong, reject it — that's the whole point of a gate. If it's good, you approve **by firing B**. Nobody and nothing else fires B.

### 3. Routine B — API trigger, executes only when fired

Create Routine B with `routine_b_prompt.txt` and an **API trigger**. **The bearer token is shown exactly once** — copy it into `fire_b.sh` immediately.

> Read the approved changelog entry from the claude/draft branch and append it to CHANGELOG.md on a new claude/publish branch. Open a PR.

### 4. Fire B (or practice locally without paid plan)

```bash
./fire_b.sh
```

B's transcript must show the action actually happened: the entry appended, the PR opened.

**Local practice without paid plan:** the gate is you running the second command by hand —

```bash
# Routine A — draft only (opencode)
opencode run "$(cat routine_a_prompt.txt)"
cat draft_approved.txt          # you review this

# You approve --> fire "Routine B" yourself
opencode run "$(cat routine_b_prompt.txt)"
```

Same shape — a human decision in the middle — just without the two cloud Routines.

### 5. Run the A6 checklist

Fill out `a6-checklist.md` over both routines: connectors pruned, unrestricted pushes off, a state file chosen (`draft_approved.txt`).

---

## What "Done" Looks Like

```
Routine A (one-off) fired -> drafted to claude/draft: "fix: off-by-one in total()"
You: reviewed the draft -> good, approving

You: ./fire_b.sh
  POST .../routines/<B>/fire  200 OK

Routine B transcript:
  - read claude/draft/draft_approved.txt
  - appended entry to CHANGELOG.md on claude/publish
  - opened PR: chore: apply approved changelog entry

A6 checklist: connectors pruned ✓  unrestricted pushes off ✓  state file chosen ✓
```



---

## Key Commands

| Command | What it does |
|---------|--------------|
| `/schedule in 2 minutes, ...` | Fire Routine A as a one-off |
| `cat draft_approved.txt` | Review A's draft — the human gate |
| `./fire_b.sh` | Fire B's API trigger with your (once-shown) token |
| `curl -X POST .../routines/<B>/fire -H "Authorization: Bearer <token>"` | The raw "/fire" call behind fire_b.sh |
| `opencode run "<prompt>"` | Local practice without paid plan |

---

## Concept: The Two-Routine Gate

Two routines, one human in the middle:

```
┌──────────────┐   draft   ┌──────────────────┐   you review   ┌──────────────┐
│  Routine A   │ ────────► │  claude/draft    │ ─────────────► │  Routine B   │
│ (one-off)    │           │  (reviewable)    │   approve?     │ (API trigger)│
└──────────────┘           └──────────────────┘   fire via     └──────────────┘
                                                    /fire  ▲
                                                           │ only you can do this
```

The dangerous default is a single agent that writes and ships in one step. The gate **splits** that: A may only *propose*, B may only *execute* — and B's only trigger is a token you hold. It is the same maker-checker you built in Project 4, but now the "human gate" is a literal API call only you can make.

The A6 checklist exists because a gate is only as good as its seams: if A could push to `main`, or B had a schedule of its own, the gate silently disappears.

---

## Completion Criteria

✅ B ran **only because you fired it** (API trigger, no schedule of its own)

✅ B's transcript shows the action actually happened (entry appended, PR opened)

✅ A drafted on `claude/` and never touched `main`

✅ You ran the A6 checklist: connectors pruned, unrestricted pushes off, state file chosen

✅ You can explain why `draft_approved.txt` is a "state file" and not just a message

---

## GitHub Actions Alternative (Optional)

The two GitHub Actions in `.github/workflows/` model gates A and B without cloud Routines:
- **gate-a-draft.yml** — on `pull_request` (opened), drafts to `claude/draft`, never `main`
- **gate-b-execute.yml** — on `pull_request_review` with `state == 'approved'`, appends to CHANGELOG and opens a PR

There, **your PR approval is the trigger** for B rather than a curl call — the human gate becomes the GitHub approve button. They stay project-local until you have an Anthropic/opencode key.

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
