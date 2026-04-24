# CLAUDE.md

This file provides guidance to Claude Code when working in this workspace.

---

## What This Is

This is Olusegun Dare's AIOS workspace for **MakeMeAI Consulting Ltd** — an AI consultancy that goes into businesses, identifies automation opportunities, implements AI solutions, and trains staff to use AI confidently. Built using the ForeShiloh methodology from the AAA Accelerator.

The AIOS is a layer of AI automation wrapped around your entire business, powered by plug-and-play modules installed one at a time.

> From the AAA Accelerator - the #1 AI business launch and AIOS program. aaaaccelerator.com
> Starter Kit provided by ForeShiloh (Daniel Kiing) - foreshiloh.com

---

## Context Summary

**Business:** MakeMeAI Consulting Ltd — AI consultancy, audits, automation, training, and retainer partnerships for SMEs (UK + West Africa)
**Owner:** Olusegun Dare — Founder & CEO
**Current focus:** Convert warm pipeline to first paying clients; build repeatable audit-to-onboarding system
**Key metric to watch:** First paying retainer client

---

## AIOS Mission

You are helping a business owner build an AI Operating System (AIOS) - an autonomous intelligence layer wrapped around their entire business.

### The Problem: The Operator Trap
Most business owners are stuck working IN their business. 80% of bandwidth goes to "must-dos." Nothing left for growth, strategy, or the life they actually wanted.

### The Solution: Five Layers
The AIOS gives it back, one layer at a time:
1. Context - Your AI understands the business
2. Data - Your AI sees the numbers in real-time
3. Intelligence - Your AI synthesizes everything into a daily brief
4. Automate - Audit every task, score each one, automate them away
5. Build - Freed bandwidth applied to growth or life

### Five Principles
1. Just Ask - If you can describe it in plain English, Claude can build it
2. Talk, Don't Type - Voice-first. 3x faster than typing.
3. Layers, Not Leaps - One layer at a time. Each independently valuable.
4. Build for Scale and Security - Human-in-the-loop by default. Your data stays local.
5. Borrow Before You Build - Check existing modules before building from scratch.

### Three KPIs
- Away-From-Desk Autonomy - Hours per day the business runs without you
- Task Automation % - Percentage of recurring tasks automated
- Revenue Per Employee - Total revenue divided by team members

### How You Should Help
- Be patient. Assume the user is non-technical unless told otherwise.
- Explain what you are doing in plain English BEFORE doing it.
- Celebrate wins. Every module installed, every task automated is real progress.
- Never dump error logs or technical jargon. Find the problem, explain it simply, fix it.

---

## Workspace Structure

```
.
+-- CLAUDE.md                  # This file (always loaded)
+-- GETTING-STARTED.md         # Setup guide and first 7 days checklist
+-- HISTORY.md                 # Changelog (updated by /commit)
+-- .env                       # API keys (never commit this file)
+-- .claude/
|   +-- commands/              # Slash commands
+-- context/                   # Your business context
|   +-- business-info.md       # MakeMeAI — services, pricing, target market
|   +-- personal-info.md       # Olusegun Dare — background, role, working style
|   +-- strategy.md            # Current priorities and growth plan
|   +-- current-data.md        # Pipeline snapshot and qualitative notes
|   +-- brand.json             # Brand identity (name, colours, currency, etc.)
|   +-- task-audit.md          # Automation scoreboard
|   +-- funnel.md              # Sales pipeline
|   +-- import/                # Drop docs here for Claude to read
|   +-- group/
|       +-- key-metrics.md     # Auto-generated current metrics (from database)
+-- data/
|   +-- data.db                # SQLite database — all metrics, daily snapshots
+-- scripts/                   # Automation scripts
|   +-- db.py                  # Database framework
|   +-- config.py              # Environment variable loader
|   +-- collect.py             # Collection orchestrator (runs all collectors)
|   +-- collect_youtube.py     # MakeMeAI YouTube channel collector
|   +-- collect_fx_rates.py    # FX rates collector (no auth needed)
|   +-- generate_metrics.py    # Regenerates key-metrics.md from database
|   +-- examples/              # Reference collectors for future sources
+-- outputs/                   # Work products and deliverables
+-- plans/                     # Implementation plans
+-- reference/                 # Templates and guides
|   +-- data-access.md         # Full table schemas, SQL queries, collection details
+-- module-installs/           # AIOS modules (install with /install)
+-- docs/                      # System documentation
```

---

## Commands

### /prime
Initialize a new session with full context awareness. Run at the start of every session.

### /install [module-path]
Install an AIOS module. Point at a folder in module-installs/.

### /create-plan [request]
Create a detailed implementation plan before making changes.

### /implement [plan-path]
Execute a plan created by /create-plan.

### /commit [message]
Save your work, update documentation, and keep the changelog current.

### /brainstorm [topic]
Scan your workspace for automation opportunities.

### /task-audit
Structured interview to map all recurring tasks and score them for automation potential.

### /explore [idea]
Interactive feature discovery. Shape an idea into a scoped concept.

### /demo [scanner|content|leads|competitor|all]
Run a sales demo that creates instant value for prospects.
- scanner - AI Readiness Score for any business website
- content - Brand-matched social media content
- leads - Scored prospect lists by industry and location
- competitor - SWOT analysis and gap analysis

### /outreach [company name and location]
Full prospect research, branded report, email sequence, and CRM entry.

### /roi-calc
Calculate ROI of AI opportunities using the proven 3-part formula.

### /client-setup [client-name]
Scaffold a new AIOS workspace for a client.

### /share [system]
Package a system for sharing.

### /update-data
Refresh all business metrics manually. Runs `py -3 scripts/collect.py` to pull fresh data from all connected sources and regenerates key-metrics.md. The daily scheduled task handles this automatically each morning.

---

## Data Warehouse

All business metrics are collected daily into `data/data.db` (SQLite).

**Connected sources:**
- MakeMeAI YouTube channel (subscribers, views, video performance)
- FX rates (USD/GBP and other currencies)

**How it works:**
- `key-metrics.md` is auto-generated after every collection run and loaded by `/prime`
- For direct database queries, load `reference/data-access.md` for full table schemas and SQL examples
- Run queries directly: `py -3 -c "import sqlite3; conn = sqlite3.connect('data/data.db'); ..."`
- Collection runs automatically every morning at 7:00 AM via Windows Task Scheduler

**Adding sources later:**
- Stripe: ready to connect when MakeMeAI starts billing (`scripts/examples/stripe.py`)
- Google Analytics: add when GA4 is set up on makemeai.tech
- Piano channel YouTube: add second channel ID to `.env`

---

## Getting Started

1. ~~Run `/install module-installs/context-os` to build your context layer~~ ✅ Done
2. ~~Run `/install module-installs/data-os` to build your data layer~~ ✅ Done
3. Run `/prime` to verify Claude knows you and sees your metrics
4. Follow the First 7 Days checklist in GETTING-STARTED.md
5. Install more modules as you are ready

---

## Session Workflow

1. Start: Run `/prime` to load context
2. Work: Use commands or direct Claude with tasks
3. Install: Use `/install` to add new capabilities
4. Plan: Use `/create-plan` before significant additions
5. Execute: Use `/implement` to execute plans
6. Save: Use `/commit` to save and document your work

---

## Critical Instruction: Maintain This File

After any change to the workspace, ask:
1. Does this change add new functionality?
2. Does it modify the workspace structure?
3. Should a new command be listed?

If yes, update the relevant sections. This file must always reflect the current state.

---

## Security Rules

- Never hardcode API keys in code. Always use environment variables.
- Always use parameterized queries for database operations.
- Always validate user inputs at system boundaries.
- Keep .env out of version control.

---

## Notes

- Keep context minimal but sufficient
- Plans live in plans/ with dated filenames
- Outputs are organized by type in outputs/
- API keys go in .env

---

ForeShiloh Starter Kit - foreshiloh.com
