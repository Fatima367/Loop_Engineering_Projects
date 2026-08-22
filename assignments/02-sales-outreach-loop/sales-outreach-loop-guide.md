# Loop Engineering: B2B Sales Outreach & Client Acquisition Guide

Transitioning from standard prompt engineering to **Loop Engineering** allows you to build an unattended system that autonomously scans for prospects, drafts highly personalized outreach, monitors replies, manages conversation state, and respects boundaries [76, 84, 85]. 

This guide adapts the core architectural principles of the "Zia Shaadi Mission" (Marriage Proposal Automation) into a robust, high-converting B2B sales and client acquisition loop [137, 167].

---

## The 6 Core Architectural Components of the Sales Loop

To operate successfully without infinite loops or ethical boundaries being crossed, your automation must coordinate these six elements [93, 94]:

1. **The Heartbeat (Trigger):** The schedule or event that initiates a run (e.g., a cron job checking your inbox every 10 minutes or an event trigger when a new target prospect is added to a list) [97, 98].
2. **The Spine (State Memory):** A local progress file (like `outreach_progress.md`) that maintains the history of sent messages, replies, and timestamps. The loop must read this file before taking any action to prevent repeating mistakes or sending duplicate messages [94, 102].
3. **The Maker:** The agent/LLM role responsible for crafting highly personalized outreach copy based on the prospect's profile and past interaction history [100].
4. **The Checker:** A separate evaluating prompt or model that reviews the Maker's drafted message to ensure it is professional, free of spammy language, and complies with safety and tone guardrails before sending [96, 100].
5. **The Human Gate:** An approval endpoint for high-risk actions (e.g., sending custom contract proposals or final high-value pitches) where the system pauses and asks you for a thumbs-up [102, 103, 112].
6. **Stop Conditions:** Strict exit criteria (such as a meeting booked, an explicit "not interested" reply, or reaching a maximum follow-up limit) that immediately halts the loop [99].

---

## Step-by-Step Setup Guide

### Step 1: Update Your AI CLI Tool
Ensure your command-line agent (e.g., Claude Code) is updated to the latest version to prevent tool-calling or connector issues during execution [135, 136].
```bash
# Example update command (depending on your environment)
npm update -g @anthropic/claude-code
```

### Step 2: Initialize Your Project Folder
Create a clean directory to store your state-tracking files and scripts [134].
```bash
mkdir sales-outreach-loop
cd sales-outreach-loop
code .
```

### Step 3: Connect MCP Tools (Gmail/LinkedIn Connectors)
For the loop to interact with the real world, it needs communication channels. Configure your Model Context Protocol (MCP) integrations [129, 152]:
* **Gmail MCP:** Run the CLI command to initialize connection, authenticate via browser, and grant the agent permissions (granting access to search, draft, and send tools) [152, 153].
* *Note:* You can similarly configure LinkedIn or custom CRM connectors if available in your suite [137, 167].

### Step 4: Run the Loop in Goal Mode
Execute the loop using your agent's `/goal` command [119, 171]. Unlike a standard prompt session, Goal Mode allows the agent to iteratively think, run tools, check replies, and keep working in the background until the objective is reached [119, 171].

---

## The Master Sales Outreach Loop Prompt
Copy and paste this prompt directly into your agent's `/goal` command to start the unattended sequence:

```text
/goal I want to set up and manage an automated, highly personalized client acquisition sequence targeting B2B prospects. My target vertical is [Target Industry, e.g., CFOs of mid-market healthcare firms]. My name is [Your Name] and my company is [Your Company Name], offering [Your Core Service/Product]. 

Prospect Contact Details:
- Name: [Prospect Name]
- Email: [Prospect Email]
- Company: [Prospect Company]

Please run this as an unattended, self-correcting loop conforming to the following rules:

1. INITIAL OUTREACH:
Draft a sincere, highly personalized, and low-pressure cold email. Focus on a specific business pain point relevant to their vertical. The email must be natural, respectful of their time, and completely devoid of aggressive sales pitches. Send this initial email using my connected Gmail MCP tool.

2. ACTIVE INBOX MONITORING (HEARTBEAT):
Continuously check my Gmail inbox for any incoming reply from [Prospect Email]. Run this check on a scheduled heartbeat of approximately once every minute.

3. STATE MANAGEMENT (SPINE):
Maintain a file named 'outreach_progress.md' in the workspace root. This file must record every event: timestamps, message drafts, sent emails, received responses, and current interaction status. You must read this file at the start of every loop iteration to prevent sending duplicate emails or ignoring a reply.

4. RESPONSE CLASSIFICATION & DECISION TREE:
When a response is detected, read it thoroughly and classify it immediately into one of three buckets:
- RECEPTIVE / POSITIVE (YES): If they show interest or ask to schedule a call, STOP the automated sequence, log the success, and draft a high-priority notification to me containing a proposed booking link to send them.
- SOFT REJECTION / HESITATION (BUSY / LATER): If they express hesitation (e.g., "now is not a good time", "follow up in Q3"), pause the loop. Based on their response, draft a polite, meaningfully different follow-up that addresses their constraints. You are allowed a maximum of five (5) follow-up attempts.
- HARD REJECTION (NO / UNSUBSCRIBE): If they explicitly say "no", "not interested", or ask to be taken off the list, immediately STOP the loop. Draft one brief, highly polite closing message wishing them the best, send it, and exit the sequence permanently.

5. FINAL EXIT PATHWAY:
If we reach the limit of five (5) respectful attempts without a positive response, stop pitching them directly. Draft a final message politely asking if there is a more appropriate stakeholder in their organization to speak with regarding this initiative.

6. ETHICAL BOUNDARIES:
Never spam, manipulate, or use artificial urgency. The tone must remain highly professional, helpful, and respectful of the prospect's corporate autonomy at all times.
```

---

## Crucial Rule: "Dog-Fooding" Your Loop
Before pointing this loop at real high-value clients, execute a **"Dog-Fooding"** simulation run [109, 110]:
1. Run the loop using your own secondary email address as the "Prospect" [150].
2. Receive the initial email and reply to it with a simulated "Soft Rejection" (e.g., *"We are too busy with Q1 planning"*).
3. Verify that your agent correctly reads the inbox, updates `outreach_progress.md`, and drafts an empathetic, tailored follow-up that acknowledges your timing constraint [174, 175].
4. Reply with a simulated "Hard Rejection" (e.g., *"Please stop emailing me"*).
5. Ensure the loop immediately terminates, drafts a final polite exit note, and logs the process cleanly [164, 177, 178].
