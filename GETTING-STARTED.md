# Getting Started with Your AIOS

> Welcome to the ForeShiloh Starter Kit. This is your AI Operating System foundation.
> Give this folder to Claude Code and say: "Read GETTING-STARTED.md and help me set up."

---

## What This Is

This is a pre-built AIOS workspace based on the same methodology Daniel Kiing used to build ForeShiloh's 1,654-tool ecosystem in 37 days inside the AAA Accelerator. You are not getting a copy of Daniel's system. You are getting the foundation to build your own.

Everything here is designed so you never need to write code. You speak to Claude in plain English and it builds.

---

## First 7 Days Checklist

### Day 1: Context Layer (your first session)
- [ ] Open this folder in Claude Code
- [ ] Run `/install module-installs/context-os` and answer the interview questions
- [ ] Claude will create your context files (business-info, personal-info, strategy)
- [ ] Run `/prime` and verify Claude knows your business
- [ ] Celebrate. Your AI now understands you.

### Day 2-3: Explore and Customise
- [ ] Read through your context files and add more detail (the more context, the better Claude performs)
- [ ] Run `/brainstorm` to discover automation opportunities in your business
- [ ] Run `/task-audit` to map all your recurring tasks and score them

### Day 4-5: Data Layer
- [ ] Run `/install module-installs/data-os` to connect your first data source
- [ ] Set up your .env file with API keys (see the API Key Guide below)
- [ ] Run `/install module-installs/daily-brief` for your AI morning intelligence report

### Day 6: Mobile Access
- [ ] Run `/install module-installs/command-os` to set up your Telegram bot
- [ ] Test sending a message to your bot from your phone

### Day 7: Client Tools
- [ ] Try `/demo scanner` on a business you know (this is your lead generation weapon)
- [ ] Try `/demo content` on a website to generate social media posts
- [ ] Review your task audit and pick your first automation to build

---

## API Key Guide

These are the keys you will need. Most have free tiers.

| Key | Where to Get It | Free Tier | What It Powers |
|-----|----------------|-----------|----------------|
| ANTHROPIC_API_KEY | console.anthropic.com | Pay as you go | Claude (your AI brain) |
| TELEGRAM_BOT_TOKEN | @BotFather on Telegram | Free | Your mobile bot |
| GEMINI_API_KEY | aistudio.google.com | 1,500 req/day free | Image gen, video analysis, cheap summarisation |
| ALPHA_VANTAGE_API_KEY | alphavantage.co/support | 25 req/day free | News sentiment (optional) |
| APOLLO_API_KEY | app.apollo.io | 60 enrichments/month | Lead enrichment (optional) |

You do NOT need all of these on day one. Start with just ANTHROPIC_API_KEY. Add others as you install modules.

---

## Folder Structure

```
.
+-- CLAUDE.md                  # The brain. Claude reads this every session.
+-- GETTING-STARTED.md         # You are here
+-- HISTORY.md                 # Changelog. Updated by /commit.
+-- .env                       # Your API keys go here (never share this file)
+-- .claude/
|   +-- commands/              # Slash commands (type / to see them all)
+-- context/                   # Your business context (Claude's knowledge of YOU)
|   +-- business-info.md       # What your business does
|   +-- personal-info.md       # Who you are
|   +-- strategy.md            # Your priorities and goals
|   +-- task-audit.md          # Your automation scoreboard
|   +-- funnel.md              # Your sales pipeline
+-- data/                      # Your database lives here
+-- scripts/                   # Automation scripts (added by modules)
+-- outputs/                   # Everything Claude produces for you
+-- plans/                     # Implementation plans
+-- reference/                 # Templates, scripts, and guides
+-- module-installs/           # AIOS modules (install with /install)
+-- docs/                      # System documentation (auto-maintained)
```

---

## Commands Available

These are ready to use from day one:

| Command | What It Does |
|---------|-------------|
| /prime | Start every session with this. Claude reads your context and is ready to work. |
| /install | Install an AIOS module from module-installs/ |
| /create-plan | Plan before you build. Creates a detailed plan in plans/ |
| /implement | Execute a plan step by step |
| /commit | Save your work, update docs, and add to changelog |
| /brainstorm | Scan your business for automation opportunities |
| /task-audit | Map all recurring tasks and score them for automation |
| /demo scanner | Scan any business website and generate an AI Readiness Report |
| /demo content | Generate a week of brand-matched social media content |
| /demo leads | Find 10 real prospects in any industry and location |
| /demo competitor | Full competitive analysis with SWOT and gap analysis |
| /outreach | Complete prospect research, report, and email sequence |
| /roi-calc | Calculate ROI for client proposals |
| /client-setup | Scaffold a new client workspace |
| /explore | Shape an idea into a scoped feature |
| /share | Package a system for sharing |

---

## The Five Layers

Your AIOS builds one layer at a time. Each layer is independently valuable.

1. Context - Your AI understands your business (Day 1)
2. Data - Your AI sees your numbers in real-time (Day 4-5)
3. Intelligence - Your AI watches everything and synthesises a daily brief (Day 5)
4. Automate - Audit every task, automate them one by one (Week 2+)
5. Build - Use freed bandwidth for growth (Ongoing)

---

## Three Rules

1. Just Ask. If you can describe it in plain English, Claude can build it. Do not self-censor.
2. Talk, Don't Type. Use voice input. Hold FN, speak for 60 seconds, let Claude format it.
3. Layers, Not Leaps. One layer at a time. Each independently valuable. Do not skip ahead.

---

## Need Help?

This kit was built by ForeShiloh (Daniel Kiing, Sheffield, UK).

- Email: {{YOUR_EMAIL}}
- Website: foreshiloh.com

---

ForeShiloh - You dream, we build. AI powers them both.
