# 🔁 Loop Engineering Projects

**12 projects. Four heartbeats. One skill: making AI loops you can trust.**

*From a one-minute watch loop to a dreaming loop that improves itself.*

[![Difficulty](https://img.shields.io/badge/difficulty-beginner%20→%20capstone-blue?style=flat-square)](#projects-at-a-glance)
[![Projects](https://img.shields.io/badge/projects-12-green?style=flat-square)](#projects-at-a-glance)
[![Source](https://img.shields.io/badge/source-agent%20factory-red?style=flat-square)](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course)

---

*A hands-on companion to the [Loop Engineering Crash Course](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course) by Agent Factory / Panaversity.*


---

## What Is Loop Engineering?

Loop engineering is building AI agents that **run recurring tasks on their own** — watching builds, fixing tests, reviewing PRs, auditing repos, and even proposing their own rule changes.

These 12 projects teach you every piece of the puzzle:

```
 ┌─────────────────────────────────────────────────────────────────────┐
 │  Heartbeats  │  Worktrees  │  Skills  │  Maker-Checker  │  Spine  │
 │  Connectors  │  Observability  │  Cost Awareness  │  Self-Improvement │
 └─────────────────────────────────────────────────────────────────────┘
```

Each project builds on the last. By **Project 8**, you have a full loop. By **Project 12**, it reads its own logs and proposes fixes as a PR — with nothing merging without your approval.

---

## Projects at a Glance

<details open>
<summary><strong>🟢 Beginner (Projects 1–3)</strong></summary>

| # | Project | Time | What You Learn |
|---|---------|------|----------------|
| 01 | [**Watch Loop**](01_watch_loop/) | 15–30 min | In-session heartbeat — poll for a file, detect it, stop |
| 02 | [**Make the Tests Pass**](02_tests_pass/) | 30–45 min | Conditional loop — agent works until a command says "done" |
| 03 | [**Morning Brief with Memory**](03_brief_with_memory/) | 45–60 min | Scheduled heartbeat + spine — prove the second run remembers the first |

</details>

<details open>
<summary><strong>🟡 Intermediate (Projects 4–7)</strong></summary>

| # | Project | Time | What You Learn |
|---|---------|------|----------------|
| 04 | [**Fix Loop with Checker**](04_fix_loop_with_checker/) | 1–2 hrs | Worktree + skill + maker-checker — PASS opens a PR, FAIL stops |
| 05 | [**Codify the Body**](05_codify_the_body/) | 1–1.5 hrs | Dynamic workflows — turn orchestration into one command |
| 06 | [**Doorbell Loop**](06_doorbell_loop/) | 45–60 min | Event-driven + connector — PR triggers review, no prompt typed |
| 07 | [**Break It on Purpose**](07_break_it_on_purpose/) | 45–60 min | Observability + cost — sabotage your loop, diagnose from the spine |

</details>

<details open>
<summary><strong>🔴 Capstone + Appendix (Projects 8–12)</strong></summary>

| # | Project | Time | What You Learn |
|---|---------|------|----------------|
| 08 | [**Your Own Daily Loop**](08_own_daily_loop/) | 2–4 hrs | **Capstone** — all six parts on a real chore, trusted unattended |
| 09 | [**Rehearse a Routine for Free**](09_rehearse_free_routine/) | 20–30 min | One-off schedules — prove a prompt before committing to a real one |
| 10 | [**The Secrets Drill**](10_secrets_drill/) | 30–45 min | Secrets — `.env` vs environment variables, and why the difference matters |
| 11 | [**Two-Routine Gate**](11_build_two_routine_gate/) | 1–2 hrs | Human gate — Routine A drafts, you decide, Routine B executes |
| 12 | [**Dreaming Loop**](12_build_dreaming_loop/) | 2–3 hrs | **Capstone** — self-improving loop that reads logs and proposes fixes |

</details>

---

## The Four Heartbeats

Every loop needs a heartbeat — something that fires it. Projects 1–6 complete the four patterns:

```
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  IN-SESSION  │     │  CONDITIONAL │     │  SCHEDULED   │     │ EVENT-DRIVEN │
  │              │     │              │     │              │     │              │
  │  /loop 1m    │     │  /goal until │     │  cron daily  │     │  PR opened   │
  │  polls until │     │  tests pass, │     │  spine reads │     │  workflow    │
  │  task done   │     │  then stops  │     │  progress.md │     │  fires       │
  │              │     │              │     │              │     │              │
  │  Project 1   │     │  Project 2   │     │  Project 3   │     │  Project 6   │
  └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

Projects 7–12 layer on **observability**, **cost awareness**, **self-improvement**, and **human gates** — the operational parts that make loops trustworthy enough to run unattended.

---

## The Six Parts of a Loop

Every mature loop has these components. They're introduced across Projects 4–8:

```
  HEARTBEAT ─── What fires the loop (cron, event, manual)
       │
  WORKTREE ──── Isolated checkout so edits don't collide
       │
  SKILL ─────── Written instructions the agent follows
       │
  MAKER-CHECKER ── Implementer drafts, reviewer grades (PASS / FAIL)
       │
  CONNECTOR ─── Plumbing to the outside world (GitHub Actions, PRs)
       │
  SPINE ─────── progress.md — the loop's memory across runs
```

---

## Two Rules

> **Rule 1:** Use a **throwaway git repo** or a fresh branch. A loop edits files on its own.
>
> **Rule 2:** **Set a limit first** — max tries, max minutes, or max spend — before anything runs unattended.

<details>
<summary><strong>⚠️ Practice note</strong></summary>

Every `/loop`, `/goal`, or cloud Routine fire burns real usage. On a free or limited plan:

- Prefer **one-off** fires over repeating schedules
- Always add your own **"stop after N tries"** clause — `/goal` has no built-in cap
- Do the drills with the **minimum number of runs** the "Done when" bar requires
- Where the course needs a real cloud Routine (9–12), `claude -p` one-shot calls can substitute

</details>

---

## Quick Start

```bash
# 1. Clone
git clone <your-repo-url>
cd Loop_Engineering_Projects

# 2. Start with Project 1
cd 01_watch_loop
# Open its README and follow along — ~15 minutes
```

Each project folder contains:
- **README.md** — goal, walkthrough, completion criteria
- **output.md** — transcript of a successful run
- Mock source files and tests ready to run

---

## Prerequisites

| Tool | What It's For | Required? |
|------|--------------|-----------|
| [Claude Code](https://claude.ai/code) (CLI, web, or IDE) | Running the loops | **Yes** — practice mode works for everything |
| Git + GitHub | PR-based projects (06, 10, 11) | Yes for those projects |
| Python 3 + pytest | Test-runner examples (02, 04, 05, 06, 08) | Yes for those projects |
| [OpenCode](https://opencode.ai) | Shell-based alternative to Claude Code | Optional — commands provided alongside Claude Code |


---

## Concepts Reference

| # | Concept | One-Liner |
|---|---------|-----------|
| 4 | **In-session loop** | `/loop` — polls on an interval while you watch |
| 5 | **Conditional loop** | `/goal` — keeps working until a condition is met |
| 6 | **Scheduled heartbeat** | Cron or `/schedule` — fires at a set time, unattended |
| 7 | **Event-driven** | A webhook or trigger fires the loop (e.g., PR opened) |
| 8 | **Worktree** | Isolated git checkout — edits don't collide |
| 9 | **Skill** | Written steps the agent follows (`SKILL.md`) |
| 10 | **Connector** | Plumbing to external systems (GitHub Actions, APIs) |
| 11 | **Maker-checker** | Implementer drafts, reviewer grades PASS / FAIL |
| 12 | **The spine** | `progress.md` — persistent memory across loop runs |
| 13 | **Cost awareness** | Token math: input + output × cadence = monthly cost |
| 14 | **Observability** | Log lines + progress.md for diagnosing failures |
| 15 | **Understanding gap** | Did your understanding keep up with what the loop changed? |

---

## Project Structure

```
Loop_Engineering_Projects/
│
├── 01_watch_loop/              ◻  In-session polling loop
├── 02_tests_pass/              ◻  Conditional fix loop
├── 03_brief_with_memory/       ◻  Scheduled loop with spine
├── 04_fix_loop_with_checker/   ◻  Worktree + maker-checker
├── 05_codify_the_body/         ◻  Dynamic workflow codification
├── 06_doorbell_loop/           ◻  Event-driven PR review
├── 07_break_it_on_purpose/     ◻  Sabotage + observability drill
├── 08_own_daily_loop/          ◻  Full six-part capstone
├── 09_rehearse_free_routine/   ◻  One-off schedule drill
├── 10_secrets_drill/           ◻  Environment vs .env
├── 11_build_two_routine_gate/  ◻  Two-routine human gate
├── 12_build_dreaming_loop/     ◻  Self-improving loop
│
├── assignments/                ◻  Additional practice projects
│   ├── 02-sales-outreach-loop/
│   └── sir-zia-shaadi-loop/
│
└── README.md                   ◻  This file
```

---

## Assignments

Additional practice projects built on the same loop engineering principles:

| Project | Description |
|---------|-------------|
| [**Sales Outreach Loop**](assignments/02-sales-outreach-loop/) | B2B email sequencing with self-correcting responses |
| [**Shaadi Loop**](assignments/sir-zia-shaadi-loop/) | Gmail-based interaction state tracker |

---

## How to Use This Repo

1. **Follow in order** — each project builds on concepts from earlier ones
2. **Read the README** in each folder before starting
3. **Run the project** using the commands in the README
4. **Check `output.md`** for what a successful run looks like
5. **Verify completion** against the checklist at the bottom of each README

---

## Contributing

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Open a PR — and if you have Project 6 set up, the doorbell will review it for you

---

<div align="center">

**Built as part of the Marathon series — learning AI agent engineering through practical, hands-on projects.**

*Based on the [Loop Engineering Crash Course](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course) by Agent Factory / Panaversity.*

</div>
