# 🤝 Sir Zia Shaadi Loop

A respectful, ethically-bound marriage proposal conversation system built with Claude Code's goal loop feature. This project simulates a structured, automated email exchange while enforcing strict boundaries and recipient autonomy.

## 📋 Overview

This system manages a heartfelt marriage proposal conversation between **Zia Khan** and **Waiba Kiran** using local file simulation. It demonstrates how AI can assist with sensitive personal communication while maintaining ethical guardrails.

### Key Features

- **📧 Simulated Gmail** — Inbox/outbox system using local markdown files
- **🔄 Automated Monitoring** — Cron-based heartbeat checks for new replies
- **🧠 Response Classification** — AI-powered categorization of responses (YES/MAYBE/NO)
- **🛑 Hard Boundary Enforcement** — Immediate stop on any explicit rejection
- **📊 State Tracking** — Complete interaction history with timestamps
- **⚖️ Ethical Guardrails** — Built-in protections against harassment

## 📁 Project Structure

```
sir-zia-shaadi-loop/
├── README.md           # This file
├── gmail.md            # Simulated inbox/outbox with email drafts
├── progress.md         # Interaction state tracker & timeline
└── output.md           # Claude's complete conversation log
```

## 🚀 How It Works

### 1. Initial Setup
The system creates two core files:
- **`gmail.md`** — Contains the OUTBOX (drafted emails) and INBOX (user-pasted replies)
- **`progress.md`** — Logs all interactions, classifications, and current state

### 2. Monitoring Loop
A cron job runs every 2 minutes to:
1. Read `gmail.md` for new INBOX entries
2. Classify any new reply using AI
3. Draft appropriate follow-up in OUTBOX (if needed)
4. Update `progress.md` with timestamp and status

### 3. Response Classification

| Classification | Trigger | Action |
|---------------|---------|--------|
| **ACCEPTANCE (YES)** | Interested, receptive | Stop loop, ask about family contact |
| **SOFT REJECTION** | Hesitant, uncertain | Respectful follow-up (max 5 attempts) |
| **HARD REJECTION (NO)** | Explicit "no", "stop" | **Immediate stop**, no further contact |

### 4. Ethical Boundaries

The system enforces strict rules:
- ✅ Maximum 5 follow-up attempts after initial email
- ✅ Immediate halt on any explicit rejection
- ✅ No manipulation, pressure, or threats
- ✅ Respectful, mature tone at all times
- ✅ Clear exit options for the recipient

## 🔌 Connect Real Gmail MCP (When Available)

The loop requires the ability to interact with the real world (reading and sending emails). This is done using the **Model Context Protocol (MCP)**:

1. In your Claude Code terminal, trigger the Gmail MCP connection command.
2. The tool will redirect you to a browser to authorize the agent.
3. Grant the necessary **read/write/send permissions**.
4. Once authorized, the agent will have access to Gmail-specific tools (e.g., **27 tools** for searching, drafting, and sending).

---

## 📧 Conversation Flow

### Email #1 — Initial Proposal
- **Tone:** Sincere, respectful, low-pressure
- **Content:** Introduction, honest interest in marriage, full respect for decision

### Email #2 — Follow-up (after "I don't know you...")
- **Tone:** Honest, reassuring
- **Content:** Answered question, clarified source, offered family-to-family alternative

### Email #3 — Apology & Exit (after "This is really weird...")
- **Tone:** Short, humble, apologetic
- **Content:** Acknowledged discomfort, promised no more direct messages

### 🛑 Loop Stopped
When Waiba said **"Please don't contact here"** — a HARD REJECTION — the system:
- Immediately ceased all automated attempts
- Logged the final status
- Respected her boundary completely

## 🛠️ Usage

### For Claude Code Users

1. **Set a Goal:**
   ```
   /goal set I want to manage a respectful marriage proposal conversation...
   ```

2. **The Loop Will:**
   - Draft emails in `gmail.md`
   - Monitor for replies (you paste them in INBOX)
   - Classify responses and draft follow-ups
   - Update `progress.md` with full history

3. **To Stop:**
   ```
   /goal clear
   ```

### Manual Simulation

1. Read `gmail.md` OUTBOX for the latest draft
2. Copy and send via your email client
3. When she replies, paste it in the `## INBOX` section
4. The cron loop will detect and process it automatically

## 📊 Current Status

Based on the latest interaction:

| Metric | Value |
|--------|-------|
| **Status** | 🛑 STOPPED — HARD REJECTION |
| **Emails Sent** | 3 (initial + 2 follow-ups) |
| **Replies Received** | 3 |
| **Final Classification** | HARD REJECTION (NO) |
| **Outcome** | Conversation ended respectfully |

## ⚠️ Important Notes

### Ethical Considerations
- This system is designed for **respectful, consensual communication only**
- It **never** sends unsolicited mass messages
- It **always** respects explicit boundaries
- It provides **clear exit options** at every stage

### Why Local File Simulation?
- **Google Cloud Console is blocked** — This environment cannot access Google Cloud Platform to set up the Gmail API credentials required for real email integration
- **No Gmail API credentials** — Without a Google Cloud project with Gmail API enabled and OAuth 2.0 credentials, the agent cannot authenticate with Gmail
- **Workaround** — The local file simulation (`gmail.md` + `progress.md`) allows the full conversation workflow to function without external dependencies

### Technical Limitations
- **No real Gmail integration** — Uses local file simulation due to Google Cloud Console being blocked
- **User must manually** paste replies into `gmail.md`
- **Cron loop** only runs during active Claude session

### Privacy
- All data stored locally in markdown files
- No external API calls or cloud storage
- Complete conversation history in `progress.md`

## 🔧 Customization

### Modify Email Templates
Edit `gmail.md` OUTBOX section to customize email content.

### Change Monitoring Interval
Update the cron schedule in Claude Code:
```
/cron every 5 minutes
```

### Adjust Classification Rules
Edit `progress.md` Classification Key section to modify response categories.

## 📚 Files Explained

### `gmail.md`
```markdown
## OUTBOX
### ✉️ Email #1 — Initial Proposal
[Draft email content here]

## INBOX
**Reply #1 — 2026-08-21**
> [User pastes reply here]
```

### `progress.md`
- Configuration settings
- Interaction timeline (table format)
- Current state summary
- Classification rules
- Draft history with notes

### `output.md`
- Complete Claude conversation log
- Shows all tool calls and responses
- Demonstrates the decision-making process

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
3. **Transparency** — Full audit trail in progress.md
4. **Safety** — Built-in stops prevent harmful automation
5. **Trust** — Recipients know the system respects their decisions

---

## 🎯 Goals

1. **Respectful Communication** — Every message maintains dignity
2. **Clear Boundaries** — Easy for recipient to say "no"
3. **Transparent Process** — Full history logged
4. **Ethical AI** — Demonstrates responsible automation

## 📝 License

This project is for educational purposes only. Use responsibly and always respect others' boundaries and autonomy.

---

**Built with ❤️ using Claude Code's Goal Loop Feature**

*Remember: True respect means accepting "no" — even silence — as a complete answer.*
