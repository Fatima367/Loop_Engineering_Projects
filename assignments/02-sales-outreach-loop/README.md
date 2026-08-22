# Sales Outreach Loop

An automated, self-correcting client acquisition system for B2B prospects using Claude Code's loop functionality.


## Overview

This project implements an automated, highly personalized sales outreach sequence targeting B2B prospects. The system operates as an unattended, self-correcting loop that:

- Sends personalized cold emails
- Monitors inbox for replies on a heartbeat schedule
- Classifies responses and takes appropriate action
- Maintains complete state management
- Follows ethical boundaries throughout

## Project Structure

```
02-sales-outreach-loop/
├── README.md                    # This file
├── gmail.md                     # Simulated email inbox with all exchanges
├── outreach_progress.md         # Complete event log and state management
└── output.md                    # Claude's full output log
```

## Key Features

### 1. Automated Email Sequencing
- **Initial Outreach**: Personalized cold email focusing on relevant business pain points
- **Follow-up Strategy**: Up to 5 respectful follow-up attempts with different angles
- **Value-First Approach**: Shares benchmarks and resources before asking for meetings

### 2. Response Classification
The system automatically classifies incoming responses into three categories:

| Category | Action |
|----------|--------|
| **RECEPTIVE / POSITIVE** | Stop sequence, notify user, draft booking link |
| **SOFT REJECTION (BUSY/LATER)** | Pause loop, draft different follow-up (max 5 attempts) |
| **HARD REJECTION (NO/UNSUBSCRIBE)** | Stop loop, send polite goodbye, exit permanently |

### 3. State Management (SPINE)
- Complete event log with timestamps
- Message history tracking
- Current interaction status
- Duplicate prevention

### 4. Active Inbox Monitoring (HEARTBEAT)
- Scheduled checks every ~60 seconds
- Automatic response detection
- Real-time classification and action

## How It Works

### Loop Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    OUTREACH LOOP                            │
├─────────────────────────────────────────────────────────────┤
│  1. Read state file (outreach_progress.md)                  │
│  2. Check gmail.md for new replies                          │
│  3. If reply found:                                         │
│     ├── Classify response (POSITIVE/SOFT/HARD)              │
│     ├── Take appropriate action per decision tree           │
│     └── Update state file                                   │
│  4. If no reply: Continue monitoring                        │
│  5. Repeat every ~60 seconds                                │
└─────────────────────────────────────────────────────────────┘
```

### Decision Tree

```
                    Reply Detected
                          │
                          ▼
              ┌───────────────────────┐
              │  Classify Response    │
              └───────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │ POSITIVE │    │   SOFT   │    │   HARD   │
    │   YES    │    │ REJECTION│    │ REJECTION│
    └──────────┘    └──────────┘    └──────────┘
          │               │               │
          ▼               ▼               ▼
    Stop Sequence    Draft Different   Send Goodbye
    Notify User      Follow-up (max 5) Exit Permanently
    Send Booking     Respect Timing
```

## Ethical Guidelines

The system follows strict ethical boundaries:

- ✅ **Never spam** or send unwanted messages
- ✅ **Never manipulate** with artificial urgency
- ✅ **Always professional** and respectful tone
- ✅ **Respect corporate autonomy** of prospects
- ✅ **Provide value** before asking for anything
- ✅ **Easy opt-out** at every stage

## Example Session

### Prospect
- **Name**: Sarah Chen
- **Role**: CFO/Finance Leader
- **Company**: Meridian Health Partners

### Sequence Outcome

| Attempt | Type | Her Response |
|---------|------|--------------|
| Initial | Cold email | "Not a priority right now" |
| Follow-up #1 | Value (benchmark) | "Appreciate it, but not now" |
| Follow-up #2 | Value (report offer) | "Send it, I'll look later" |
| Follow-up #3 | Delivered report | "Thanks, will look when I can" |
| Follow-up #4 | Asked about timing | **"Q4 would be better, check back then"** |
| Final | Confirmed Q4 | — |

**Result**: Positive engagement with clear Q4 timeline established

## Key Success Factors

1. **Respected Timing**: Never pushed for a call when she said "not now"
2. **Provided Value First**: Shared benchmark data and free report
3. **Stayed Persistent but Polite**: 4 attempts with different angles
4. **Gave Prospect Control**: Asked "when would be better?" instead of assuming
5. **Left Door Open**: Made it easy to engage when ready

## State File Format

The `outreach_progress.md` file tracks:

```markdown
## Sequence Status
- **Prospect:** [Name]
- **Company:** [Company]
- **Email:** [Email]
- **Sequence Started:** [Date]
- **Current Status:** [Status]
- **Attempts Made:** [X/5]

## Event Log
| Timestamp | Event | Details |
|-----------|-------|---------|
| 2026-08-22 10:00 | Sequence Initiated | Preparing initial cold email |
| ... | ... | ... |

## Message History
[Full email content with timestamps]
```

## Gmail Simulation Format

The `gmail.md` file simulates an email inbox:

```markdown
## 📥 REPLY FROM SARAH CHEN - Response #X
**Date:** YYYY-MM-DD
**Subject:** Re: [Original Subject]

[Email content]

---
**Status:** REPLY RECEIVED - YYYY-MM-DD
**Classification:** [Classification]
---
```

## Usage

### Running the Loop

The loop is configured to run every ~60 seconds using Claude Code's cron functionality:

```bash
# The loop runs automatically once started
# Check gmail.md for Sarah's replies
# The system will classify and respond automatically
```

### Manual Monitoring

To check the current state:

```bash
# View progress
cat outreach_progress.md

# View email exchanges
cat gmail.md
```

### Stopping the Loop

The loop stops automatically when:
- A positive response is received
- A hard rejection is received
- The maximum follow-up limit (5) is reached
- The user manually stops it

## Customization

### Modifying the Sequence

To adapt this for different prospects:

1. Update prospect details in the goal statement
2. Customize the initial email template
3. Adjust follow-up angles based on industry/role
4. Modify the decision tree if needed

### Changing Timing

To adjust the monitoring frequency:

```javascript
// In the CronCreate call, modify the cron expression:
// Every minute: "*/1 * * * *"
// Every 5 minutes: "*/5 * * * *"
// Every hour: "0 * * * *"
```

## Files Explanation

| File | Purpose | Contents |
|------|---------|----------|
| `README.md` | Project documentation | This file |
| `gmail.md` | Simulated inbox | All email exchanges with clear reply headers |
| `outreach_progress.md` | State management | Event log, message history, current status |
| `output.md` | Execution log | Complete Claude output with tool calls |

## Technical Implementation

### Tools Used

- **CronCreate**: Schedules recurring inbox checks
- **Read/Write/Edit**: File operations for state management
- **Bash**: Shell commands for MCP tool checks

### Loop Configuration

```javascript
// Cron schedule
{
  cron: "*/1 * * * *",  // Every minute
  recurring: true,
  prompt: "Check gmail.md for any reply from Sarah Chen..."
}
```

## ⚠️ Why Local File Simulation?

This project uses local file simulation (`gmail.md`) instead of real Gmail integration due to:

- **🚫 Google Cloud Console is blocked** — This environment cannot access Google Cloud Platform to set up the Gmail API credentials required for real email integration
- **No Gmail API credentials** — Without a Google Cloud project with Gmail API enabled and OAuth 2.0 credentials, the agent cannot authenticate with Gmail
- **Workaround** — The local file simulation allows the full conversation workflow to function without external dependencies

## 🔌 Connect Real Gmail MCP (When Available)

The loop requires the ability to interact with the real world (reading and sending emails). This is done using the **Model Context Protocol (MCP)**:

1. In your Claude Code terminal, trigger the Gmail MCP connection command.
2. The tool will redirect you to a browser to authorize the agent.
3. Grant the necessary **read/write/send permissions**.
4. Once authorized, the agent will have access to Gmail-specific tools (e.g., **27 tools** for searching, drafting, and sending).

## Lessons Learned

1. **Value First**: Providing resources before asking for meetings builds trust
2. **Respect Timing**: Acknowledging constraints maintains relationships
3. **Give Control**: Letting prospects choose when to engage increases response rates
4. **Stay Persistent**: Multiple touchpoints with different angles work
5. **Track Everything**: Complete logs enable learning and optimization

## Next Steps

After a successful sequence:

- [ ] Set calendar reminder for Q4 follow-up
- [ ] Reference accepted resources in future outreach
- [ ] Consider reaching out to other stakeholders
- [ ] Document learnings for future sequences

## 🎓 What You'll Learn — Loop Engineering

This project is designed to learn **Loop Engineering** — the art of building autonomous, goal-driven AI systems that operate in cycles while maintaining ethical boundaries and state awareness.

### Core Concepts

1. **Goal Loop Architecture**
   - How to structure AI tasks as repeatable loops
   - Setting clear exit conditions and success criteria
   - Managing persistent state across iterations

2. **State Management (The Spine)**
   - Using markdown files as conversation memory
   - Maintaining context across multiple interactions
   - Preventing duplicate or contradictory actions

3. **Response Classification**
   - Building decision trees for AI responses
   - Categorizing inputs (YES/MAYBE/NO)
   - Triggering appropriate actions based on classification

4. **Ethical Guardrails**
   - Implementing hard stops on boundaries
   - Building respect for autonomy into the loop
   - Preventing manipulation and pressure patterns

5. **Heartbeat Monitoring**
   - Cron-based polling for new events
   - Checking for updates at regular intervals
   - Graceful handling of no-change scenarios

6. **Model Context Protocol (MCP)**
   - Connecting AI to external services (Gmail)
   - Managing permissions and authorization
   - Bridging local simulation with real-world tools

### Real-World Applications

| Use Case | Loop Pattern | Ethics |
|----------|--------------|--------|
| Customer support | Monitor inbox → classify → respond | Respect escalation limits |
| Lead nurturing | Check engagement → personalize → follow-up | Honor opt-out requests |
| Interview scheduling | Track responses → suggest times → confirm | Don't over-pursue |
| Feedback collection | Send survey → analyze → act on input | Maintain anonymity |

### Why Loop Engineering Matters

1. **Autonomy** — AI can operate independently while respecting boundaries
2. **Scalability** — Same pattern works for 1 conversation or 1000
3. **Transparency** — Full audit trail in progress files
4. **Safety** — Built-in stops prevent harmful automation
5. **Trust** — Recipients know the system respects their decisions

## 📝 License

Internal project - Northstar Revenue Systems

---

**Built with ❤️ using Claude Code's Goal Loop Feature**

*Remember: True respect means accepting "no" — even silence — as a complete answer.*
