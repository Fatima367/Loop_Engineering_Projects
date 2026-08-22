# 12 — Build a Dreaming Loop (Second Capstone)

**Project 12 of the Loop Engineering Series**
Difficulty: capstone · Time: 2–3 hrs · Concepts: 12 (The Spine), 11 (Maker-Checker), 6 (Schedule), Part 5 (Human Gate)

---

## Goal

Build a loop **on top of your loops**: on a weekly schedule it reads your other loops' logs, finds failures that repeat, and proposes the smallest rules-file change that would have prevented them — as a PR, never a direct commit. An improvement loop that *guesses* is worse than no improvement loop, so everything it proposes must cite its evidence.

---

## What This Project Demonstrates

- **The improvement loop** (Concept 12): a loop that reads *other loops' outputs* and changes the rules that steer them
- **Evidence over plausibility**: every proposed change must trace to cited, dated log entries
- **The human gate holds the rules**: nothing changes in `AGENTS.md` unless *you* merge the PR
- **A planted repeated failure** that the loop must catch and turn into a proposal
- **The deletion half**: a loop that only adds rules grows forever; it must also propose removing rules no recent run needed

---

## Prerequisite

A `progress.md` with **dated entries** — reuse the one from Project 3 or 8.

```bash
# Run Project 3's loop a few more times by hand first so you have at least
# 3–4 dated entries to work with.
```

This project's `progress.md` already includes the planted repeated failure
(`config.yaml` missing on 2026-08-15 / 16 / 17) so the loop has something to catch.

---

## Files

| File | Purpose |
|------|---------|
| `progress.md` | The spine the dreaming loop reads — includes the planted repeated `config.yaml` failure (3 dated entries). |
| `dreaming-state.md` | The dreaming loop's own state — `last_reviewed` date; only entries after it count. |
| `AGENTS.md` | The rules file the loop proposes changes to. Starts WITHOUT the config check (so the proposal has something to add) and WITH a rule no recent run needed (so it has something to delete). |
| `dream_prompt.txt` | The `/goal` prompt that drives a free-tier dreaming pass (verbatim from the course). |
| `proposal_example.md` | Mock PR description — shows how a proposal must cite dated entries. |
| `.github/workflows/dreaming-loop.yml` | Real-version weekly `on: schedule` template (project-local; needs a key to activate). |
| `README.md` · `output.md` | This doc · template transcript. |

> `config.yaml` deliberately does **not** exist in this folder — its absence is
> the planted trigger the loop must notice in the logs.

---

## How It Works

### 1. Seed the state

`dreaming-state.md` starts at `last_reviewed: 2026-08-14`. Everything in `progress.md` dated after that is fair game — including the three `config.yaml` failures.

```markdown
# Dreaming loop state
last_reviewed: 2026-08-14
```

### 2. Plant a repeated failure

Add these lines to `progress.md` by hand, across a few "runs":

```
2026-08-15: Failed — tried to read config.yaml, file not found.
2026-08-16: Failed — tried to read config.yaml, file not found.
2026-08-17: Failed — tried to read config.yaml, file not found.
```

### 3. Fire the dreaming pass

**Free-tier substitute (Claude Code):**

```bash
claude -p "$(cat 12_build_dreaming_loop/dream_prompt.txt)"
```

**Free-tier substitute (opencode):**

```bash
opencode run "Read progress.md entries after the date in dreaming-state.md. Find any failure that repeats more than once. Draft the smallest AGENTS.md change that would prevent it, on a new opencode/ branch — never commit directly to main. Cite the dated entries as evidence. Also propose one rule to delete that no recent run needed. Update dreaming-state.md."
```

The prompt does four things:
1. **Read** every entry after `last_reviewed`
2. **Find** failures that appear more than once → the `config.yaml` trio
3. **Draft** the smallest rules change on a `claude/` branch — PR only, never a direct commit
4. **Update** `dreaming-state.md` so the next run builds on this one

### 4. Read the proposal like a skeptic

Open the PR. Every claim must trace to a dated entry:

- **Add rule:** "check config.yaml exists before reading it" — cited to `2026-08-15`, `16`, `17`
- **Delete rule:** "pin dependency versions" — no recent run needed it

If the loop proposes something with no evidence, tighten the prompt — a guessing improvement loop steers every future run, so it's worse than none.

### 5. Merge or reject by hand

Nothing changes in `AGENTS.md` unless **you** merge the PR. The gate is a human decision, exactly as in Project 11.

### 6. Wire it to weekly

Once proven, schedule with cron or GitHub Actions `on: schedule` — same pattern as Project 3/6.

---

## Key Commands

| Command | What it does |
|---------|--------------|
| `claude -p "$(cat dream_prompt.txt)"` | One dreaming pass (free-tier) |
| `opencode run "<dream prompt>"` | Same for opencode |
| `grep -c "config.yaml" progress.md` | Confirm the repeated failure exists |
| `gh pr create --base master --head claude/...` | The PR (the loop does this itself) |
| `gh pr merge` | **You**, when you approve — nothing changes without this |

---

## What "Done" Looks Like

```
Dreaming pass fired.
  Entries after 2026-08-14: 5
  Repeated failures found: 3x "tried to read config.yaml, file not found"
    - 2026-08-15 / 2026-08-16 / 2026-08-17

PR opened  claude/dream-... → master
  title: dream: add config.yaml existence check
  body: proposes adding the rule + deleting the unused dependency-pin rule,
        each cited to dated entries

dreaming-state.md: last_reviewed: 2026-08-22

AGENTS.md: UNCHANGED until you merge the PR.
```

---

## Concept: The Improvement (Dreaming) Loop

A regular loop reads a repo and changes the repo. A **dreaming** loop reads a
regular loop's *logs* and changes the *rules* that steer the next loop:

```
            loop A  -> writes progress.md
            loop B  -> writes progress.md
                \        /
                 └───────┘
              dreaming loop (weekly)
                   │  reads entries after last_reviewed
                   │  finds repeats
                   ▼
        proposes rule change as a PR (claude/* branch)
                   │
              human reviews & merges  ◄── nothing changes without this
                   │
            AGENTS.md updated -> steers all future runs
```

The danger is a loop that *guesses*: it invents plausible improvements nobody
asked for, and every "improvement" silently steers future runs. That's why the
bar is concrete evidence — a cited dated entry per claim — and the gate is a
human merge. The **deletion** rule keeps the file from growing into a pile of
rules no current loop needs.

---

## Completion Criteria

✅ The proposed change traces to **real, cited dated entries** — not a plausible guess

✅ The planted repeated `config.yaml` failure (3 entries) is caught and turned into a proposal

✅ Nothing changed in your rules file without you merging the PR

✅ `dreaming-state.md` advanced past the last reviewed date (spine updated)

✅ For a bonus: it also proposed one deletion — a rule no recent run needed

---

*Part of the [Loop Engineering Projects](../) series — learning Claude Code's `/loop` skill through practical examples.*
