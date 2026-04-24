# Client Setup

> Scaffold a new AIOS workspace for a ForeShiloh Architecture client. Creates the full workspace structure, runs an interactive discovery interview, and generates all context files ready for building.

## Variables

client_name: $ARGUMENTS (the client's business name, e.g., "ranger-wifi" or "crystal-academy")

---

## Instructions

You are setting up a **client AIOS workspace** for ForeShiloh's Architecture division. Daniel Kiing is the operator -- he manages this workspace on behalf of the client. The client never touches this workspace directly.

This command follows Tyler Banks' proven process: context first, always. The discovery interview captures everything needed to start building automations the same day.

### Critical Rules

- **This is an interview, not a form.** Ask questions conversationally. Let Daniel talk (he may be dictating via voice). Don't rush.
- **STOP between each stage.** Present what you've captured, confirm it's right, then move on.
- **Use the 5 discovery questions** for pain points -- these are non-negotiable. They drive the entire engagement.
- **Fill templates with real answers, not placeholders.** Every `{{PLACEHOLDER}}` in the templates must be replaced with actual content from the interview.
- **Be thorough on pain points.** This is where the money is. Dig deep. Ask follow-ups. The pain point file drives the automation roadmap.
- **Keep it simple for Daniel.** He may be doing this with a client in the room. No jargon, no technical details in the interview questions.

---

## Stage 1: SETUP -- Create the Workspace

**Goal:** Create the client workspace folder structure.

**Actions:**

1. Sanitise the client name for use as a folder name (lowercase, hyphens, no spaces)
2. Create `clients/{client-name}/` by copying the entire `reference/client-template/` structure
3. Copy `.env.example` to the client workspace
4. **Security hardening:** Copy `reference/claude-code-security-settings.json` into the client workspace as `.claude/settings.json`. This applies the standard deny rules (blocks reading .env, credentials, destructive git, rm -rf, sudo, DROP TABLE, and settings self-modification). The client template CLAUDE.md already includes security hard rules.
5. Confirm the structure was created

**Present:**

```
Created workspace for {client_name}:
  clients/{client-name}/
    CLAUDE.md
    .env.example
    context/ (6 template files ready)
    scripts/ (config.py, db.py)
    plans/ (automation roadmap template)
    outputs/
    data/

Ready to start the discovery interview. This has 11 stages -- I'll ask questions, you answer (voice or text), and I'll build the context files as we go.
```

**Proceed to Stage 2 automatically** (no STOP needed here -- just confirmation that files were created).

---

## Stage 2: BUSINESS OVERVIEW -- Understand the Client

**Goal:** Fill out `context/business-info.md` and `context/personal-info.md`.

**Ask these questions (adapt to conversation flow):**

### About the Business
1. What's the company name and what do they do? (one sentence)
2. What industry are they in?
3. Where are they based?
4. How many people work there?
5. Roughly how much revenue do they do? (range is fine -- under 100K, 100K-500K, 500K-1M, 1M-5M, 5M+)
6. How do they make money? What are their main products or services?
7. Who are their customers?
8. How does work currently flow in the business? (walk me through a typical day/week)

### About the Contact
9. Who's the main contact? Name and role.
10. How tech-savvy are they? (non-technical / basic / intermediate / technical)
11. How do they prefer to communicate? (email, WhatsApp, Slack, phone)
12. Anyone else involved in decisions?

**After answers:**

- Write `context/business-info.md` with real content (replace all placeholders)
- Write `context/personal-info.md` with real content
- Present a summary: "Here's what I've captured about {company}. Anything to add or correct?"

**STOP and wait for confirmation.**

---

## Stage 3: PAIN POINT DISCOVERY -- The Core of the Engagement

**Goal:** Fill out `context/pain-points.md` using Tyler Banks' 5 discovery questions.

This is the most important stage. Take your time here.

**Say to Daniel:**

```
Now the important part -- the pain points. This drives everything we build.
Let's go through their top 3 problems. For each one, I need answers to 5 specific questions.

Pain Point 1 -- what's the biggest thing causing them pain in their business right now?
```

**For EACH pain point (do at least 3), ask the 5 questions:**

1. **What is the pain point?** (describe it)
2. **How much is it costing them?** (time per week AND money per month)
3. **How long have they had this problem?**
4. **What does the business look like if they don't fix this?**
5. **If money and technology weren't a problem, what would the perfect solution look like?**

**After each pain point, also ask:**
- Can we automate this? (your assessment)
- What tools/APIs would we need?
- How would you rank this vs the others?

**After all pain points:**

- Write `context/pain-points.md` with full detail on all pain points
- Rank them by ROI (cost x ease of automation)
- Present the ranking: "Here's how I'd prioritise these. #1 has the highest ROI because..."

**STOP and wait for confirmation on the ranking.**

---

## Stage 4: BASELINE METRICS -- Measure Before You Automate

**Goal:** Capture quantifiable baseline data for every pain point BEFORE automation. This is critical for proving ROI later. Write `context/baseline-metrics.md`.

**Say to Daniel:**

```
Before we talk about goals, let's lock in the numbers as they are right now.
For each pain point we just captured, I need to know how things look TODAY so
we can prove the ROI once we automate.
```

**For EACH pain point from Stage 3, ask:**

1. **Hours per week** -- How many hours per week does the team spend on this task? (total across all people involved)
2. **Error rate / rework** -- How often does this go wrong? (e.g., "about 1 in 5 invoices need correcting", "we lose maybe 2 leads a week to slow follow-up")
3. **Current cost** -- What does this cost right now? (staff hours x hourly rate, or direct costs like software fees, outsourcing, lost revenue)
4. **Volume processed** -- How many units flow through this process? (leads/week, invoices/month, emails/day, orders/week, etc.)
5. **Customer response time** -- How long does a customer wait for the outcome of this process? (e.g., "quotes take 48 hours", "support replies within 24 hours on a good day")

**Also ask once (not per pain point):**

6. What's the fully loaded cost of one staff hour? (salary + overhead, or just their hourly rate if they're contractors)
7. Are there any seasonal peaks when these problems get worse?

**After answers:**

- Write `context/baseline-metrics.md` using this structure:

```markdown
# Baseline Metrics

> Captured: {{DATE}}
> These metrics represent the state BEFORE any AIOS automation.
> Used for ROI measurement after each automation phase.

## Staff Cost Basis

- Fully loaded hourly rate: {{RATE}}
- Seasonal notes: {{NOTES}}

## Pain Point 1: {{NAME}}

| Metric | Value | Notes |
|--------|-------|-------|
| Hours/week | {{VALUE}} | {{WHO_DOES_IT}} |
| Error/rework rate | {{VALUE}} | {{DESCRIPTION}} |
| Monthly cost | {{VALUE}} | {{CALCULATION}} |
| Volume processed | {{VALUE}} | {{UNIT_AND_PERIOD}} |
| Customer response time | {{VALUE}} | {{CONTEXT}} |

## Pain Point 2: {{NAME}}

(same table)

## Pain Point 3: {{NAME}}

(same table)

## Summary

| Pain Point | Monthly Cost | Hours/Month | Error Rate |
|------------|-------------|-------------|------------|
| {{PP1}} | {{COST}} | {{HOURS}} | {{RATE}} |
| {{PP2}} | {{COST}} | {{HOURS}} | {{RATE}} |
| {{PP3}} | {{COST}} | {{HOURS}} | {{RATE}} |
| **Total** | **{{TOTAL}}** | **{{TOTAL}}** | |
```

- Present: "Here are the baseline numbers I've captured. These become our scoreboard for proving ROI. Anything to adjust?"

**STOP and wait for confirmation.**

---

## Stage 5: STRATEGY & KPIs -- Goals and Success Metrics

**Goal:** Fill out `context/strategy.md` and `context/current-data.md`.

**Ask:**

1. What are their top 3 priorities right now?
2. What KPIs do they currently track? (if any -- many small businesses don't formally track KPIs)
3. What does success look like in 90 days?
4. What does success look like in 12 months?
5. Any revenue targets?
6. What key metrics should we measure to prove the automations are working?

**Also capture current state:**

7. What are their current numbers? (leads/month, revenue, customers, team size -- whatever's relevant)
8. What's their biggest constraint right now? (time, money, people, tech)
9. How many hours per week do they spend on admin/manual work?

**After answers:**

- Write `context/strategy.md` with real content
- Write `context/current-data.md` with real content
- Present: "Here's the strategy and baseline metrics I've captured."

**STOP and wait for confirmation.**

---

## Stage 6: TOOLS & INTEGRATIONS -- What They Use

**Goal:** Fill out `context/integrations.md` and prepare `.env`.

**Ask:**

1. What software and tools do they currently use? (CRM, email, accounting, social media, project management, etc.)
2. For each tool: do they have API access or can they get it?
3. Where do they store files? (Google Drive, Dropbox, local, Notion, etc.)
4. Do they have a website? What platform?
5. What social media accounts are active?
6. Any existing automations? (Zapier, Make, n8n, etc.)

**After answers:**

- Write `context/integrations.md` with the full tool inventory
- Identify which API keys we need to get from them
- Note which tools we can connect to immediately vs. which need setup
- Create `.env` from `.env.example` with the relevant keys uncommented (values still blank -- Daniel fills these in with the client)

**Present:** "Here's the full tool inventory. We need API keys for {list}. I've prepared the .env file."

**STOP and wait for confirmation.**

---

## Stage 7: BUSINESS HIERARCHY MIND MAP -- Map the Organisation

**Goal:** Create `context/business-hierarchy.md` capturing the full organisational structure, process flows, stakeholders, tool stack usage, and communication channels. This document becomes the blueprint for understanding how work actually moves through the business -- where it flows, where it gets stuck, and where automation will have the most impact.

**Say to Daniel:**

```
Now let's map out how the business actually works day to day.
I need to understand who does what, how work flows between people,
and how they communicate. This helps us spot automation opportunities
we might have missed and avoid building things that break existing workflows.
```

**Ask these questions (adapt to conversation flow):**

### Org Chart & Decision Makers
1. Walk me through the team structure -- who reports to whom?
2. Who are the key decision makers? (not just the boss -- who actually decides how things get done day to day?)
3. Are there any external people who are critical to operations? (accountant, VA, freelancers, agencies)

### Process Flows
4. What are the 3-5 main business processes? (e.g., "lead comes in > quote sent > job booked > work done > invoice sent > payment chased")
5. For each process: who touches it, and where are the handoffs between people?
6. Where do things get stuck or bottlenecked most often?

### Stakeholders & Their Pain Points
7. For each key person in the business: what's their biggest frustration? What takes up most of their time?
8. Who interacts with customers most? What does that interaction look like?

### Tool Stack Usage (building on Stage 6)
9. Let's map every tool to its actual usage. For each tool from Stage 6, confirm: who uses it, how often, and is it the right tool or a workaround?
10. Are there any tools people have stopped using or only half-use?

### Communication Channels
11. How does the team communicate internally? (email, Slack, Teams, WhatsApp group, phone calls, in person)
12. How do they communicate with customers? (same question)
13. Is there a "source of truth" for information, or do things live in people's heads?

**After answers:**

- Write `context/business-hierarchy.md` using this structure:

```markdown
# Business Hierarchy

> Captured: {{DATE}}
> Organisation map, process flows, stakeholders, tool stack, and communication channels.

## Org Chart

| Person | Role | Reports To | Key Responsibilities |
|--------|------|-----------|---------------------|
| {{NAME}} | {{ROLE}} | {{MANAGER}} | {{RESPONSIBILITIES}} |

### External Contributors
- {{NAME}} -- {{ROLE}} ({{RELATIONSHIP}}, e.g., "freelance bookkeeper, 5hrs/week")

## Key Decision Makers

| Decision Area | Person | Notes |
|--------------|--------|-------|
| {{AREA}} | {{NAME}} | {{CONTEXT}} |

## Process Flows

### Process 1: {{NAME}} (e.g., "Lead to Sale")
1. {{STEP}} -- owned by {{PERSON}} -- tools: {{TOOLS}}
2. {{STEP}} -- owned by {{PERSON}} -- tools: {{TOOLS}}
3. ...
**Bottleneck:** {{WHERE_AND_WHY}}
**Handoff risks:** {{DESCRIPTION}}

### Process 2: {{NAME}}
(same structure)

### Process 3: {{NAME}}
(same structure)

## Stakeholder Pain Points

| Person | Role | Biggest Frustration | Time Sink |
|--------|------|-------------------|-----------|
| {{NAME}} | {{ROLE}} | {{FRUSTRATION}} | {{HOURS_PER_WEEK}} |

## Tool Stack Map

| Tool | Purpose | Used By | Frequency | API Available | Notes |
|------|---------|---------|-----------|--------------|-------|
| {{TOOL}} | {{PURPOSE}} | {{WHO}} | {{FREQUENCY}} | {{YES/NO}} | {{NOTES}} |

### Underused / Abandoned Tools
- {{TOOL}} -- {{WHY_UNDERUSED}}

## Communication Channels

### Internal
| Channel | Used For | By Whom | Frequency |
|---------|----------|---------|-----------|
| {{CHANNEL}} | {{PURPOSE}} | {{WHO}} | {{FREQUENCY}} |

### Customer-Facing
| Channel | Used For | Volume |
|---------|----------|--------|
| {{CHANNEL}} | {{PURPOSE}} | {{VOLUME}} |

### Source of Truth
- **Current:** {{DESCRIPTION}} (e.g., "mostly in Sarah's head and a shared Google Sheet")
- **Ideal:** {{WHAT_IT_SHOULD_BE}}
```

- Present: "Here's the full business map. This shows where work flows, where it gets stuck, and where the automation opportunities are. Anything to add or correct?"

**STOP and wait for confirmation.**

---

## Stage 8: AI CHAMPIONS -- Identify Internal Advocates

**Goal:** Identify the team members most likely to champion AI adoption. Write `context/champions.md`. These are the people who get the first quick wins, provide feedback during rollout, and drive adoption across the team. Enthusiasm spreads from champions, not from company-wide mandates. If the rollout strategy is "everyone start using this on Monday", it will fail.

**Say to Daniel:**

```
Before we build the roadmap, I need to know who on the team is going to
champion this internally. AI adoption fails when it's forced on everyone
at once. It works when one or two enthusiastic people start using it,
see the results, and pull others in naturally.
```

**Ask these questions:**

1. Who on the team is most tech-curious? (already experimenting with ChatGPT, automations, spreadsheet formulas, anything like that)
2. Who is most frustrated with manual processes? (frustration = motivation to adopt)
3. Is there anyone who actively resists new technology? (important to know who NOT to start with)
4. Who has the most influence over how the team works day to day? (not necessarily the boss)
5. If you could only show ONE person the first automation and have them spread the word, who would it be?

**After answers:**

- Write `context/champions.md` using this structure:

```markdown
# AI Champions

> Captured: {{DATE}}
> Team members identified as AI adoption champions for training and rollout.
> These people get the first quick wins and drive adoption across the team.

## Primary Champion

- **Name:** {{NAME}}
- **Role:** {{ROLE}}
- **Why chosen:** {{REASON}} (e.g., "already uses ChatGPT for email drafting, most frustrated with manual invoicing")
- **Tech comfort:** {{LEVEL}} (non-technical / basic / intermediate / technical)
- **First quick win:** {{WHAT_THEY_GET_FIRST}} (to be confirmed in capstone stage)
- **Contact:** {{EMAIL_OR_PHONE}}

## Secondary Champion(s)

- **Name:** {{NAME}}
- **Role:** {{ROLE}}
- **Why chosen:** {{REASON}}
- **Tech comfort:** {{LEVEL}}
- **Best use case for them:** {{SUGGESTION}}

## Adoption Risks

| Person | Concern | Mitigation |
|--------|---------|------------|
| {{NAME}} | {{CONCERN}} (e.g., "resistant to change", "worried about job security") | {{APPROACH}} |

## Training Follow-Up Plan

- [ ] Primary champion gets first quick win during onboarding (Stage 10)
- [ ] Schedule 30-min walkthrough with primary champion in week 1
- [ ] Secondary champions introduced in week 2-3
- [ ] Full team exposure only after champions are comfortable and advocating
- [ ] Revisit champion list at 30-day check-in (people surprise you)
```

- Present: "Here are the AI champions I've identified. {{PRIMARY_CHAMPION}} gets the first quick win. Anyone to add or adjust?"

**STOP and wait for confirmation.**

---

## Stage 9: AUTOMATION ROADMAP -- The Build Plan

**Goal:** Generate `plans/automation-roadmap.md` based on pain points, tools, strategy, business hierarchy, and AI champions.

**Actions (no more questions needed -- generate from what we have):**

1. Take the top 3 pain points from Stage 3
2. **Apply the "Build Three" rule:** Only automate the top 3 workflows first. Do not expand until the team is actually using them in production. Resist the temptation to plan 10 modules -- pick the 3 that deliver the most ROI and get them working before adding anything else.
3. For each of the 3, design the module(s) that would solve it
4. Map which APIs/tools are needed (from Stage 6)
5. Cross-reference with the business hierarchy (Stage 7) -- ensure the automation targets the right process flows and handoff points
6. Estimate time to first value
7. Calculate ROI: cost of pain point vs. monthly fee
8. **Assign the AI Champion** from Stage 8 -- the primary champion gets the first quick win. Reference their specific pain point and preferred workflow.
9. Write `plans/automation-roadmap.md` with real content -- include the Build Three constraint, the AI Champion, and process flow references from the business hierarchy

**Present the roadmap:**

```
Here's the automation roadmap for {client}:

BUILD THREE RULE: We only automate 3 workflows first. No expansion until these are in production and the team is actually using them.

AI CHAMPION: {name} ({role}) -- gets the first quick win. They'll drive adoption across the team.

Phase 1 (Month 1): {pain point 1}
  - Module 1: {description}
  - Module 2: {description}
  - Module 3: {description}
  - Expected result: {outcome}
  - AI Champion's first win: {specific deliverable for the champion}

Phase 2 (Month 2): {pain point 2}
  ...

Phase 3 (Month 3): {pain point 3}
  ...

Total monthly cost of these pain points to {client}: {amount}
ForeShiloh monthly fee: {amount}
ROI for client: {X}x

Time to first value: {estimate}
```

**STOP and wait for confirmation.**

---

## Stage 10: CAPSTONE QUICK WIN -- The "Aha Moment"

**Goal:** End every client onboarding with ONE tangible, working automation the client can see and use immediately. This is the moment that turns a plan into belief. The client walks away from setup having already experienced what the AIOS can do -- not just heard about it.

**Say to Daniel:**

```
Last step before we wrap up. Every onboarding should end with something
the client can actually see and use TODAY -- not just a plan for the future.

Let's build one quick win right now. Something small but real.
```

**Ask Daniel:**

```
What's one thing this client spends too much time on every single week?
Something repetitive, tedious, or frustrating that they'd love to never
do manually again.
```

**Wait for the answer, then:**

1. **Assess the quick win** -- is it achievable in this session with the tools and access we have? Good candidates:
   - Query their CRM or database from the workspace and surface insights they normally dig for manually
   - Auto-generate a report they currently spend hours compiling (weekly sales summary, project status, invoice tracker)
   - Pull data from multiple tools into one consolidated view
   - Create a template or workflow that eliminates a repetitive manual step
   - Set up a monitoring alert for something they currently check manually

2. **If the quick win is achievable now:** Use `/explore` to scope and build it interactively. Walk Daniel through the process so he can demo it to the client. Build it inside the client workspace (`clients/{client-name}/`).

3. **If the quick win needs API keys or access we don't have yet:** Design exactly what it will look like, save the exploration doc, and mark it as "ready to build once we have {keys/access}". The client should still see the plan and understand what they'll get.

4. **Document the quick win** in `plans/capstone-quick-win.md`:

```markdown
# Capstone Quick Win

> Built during onboarding: {{DATE}}
> The first tangible automation delivered to {{CLIENT_NAME}}.

## What Was Built

{{DESCRIPTION}}

## Problem It Solves

{{WHAT_THEY_USED_TO_DO_MANUALLY}}

## Who Benefits

- **Primary:** {{AI_CHAMPION_NAME}} ({{ROLE}})
- **Also:** {{OTHER_BENEFICIARIES}}

## How It Works

{{PLAIN_ENGLISH_EXPLANATION}}

## Time Saved

- **Before:** {{HOURS_PER_WEEK}} per week doing this manually
- **After:** {{NEW_TIME}} (automated / on-demand / instant)

## Status

- [ ] Built and working
- [ ] Demoed to client
- [ ] AI Champion trained on it
- [ ] Handed off for daily use

## Files

- {{LIST_OF_FILES_CREATED}}

## Next Enhancement

{{WHAT_WOULD_MAKE_THIS_EVEN_BETTER}}
```

5. **Present the result:**

```
Here's your first quick win for {client}:

{DESCRIPTION}

This replaces {X hours/week} of manual work. {AI_CHAMPION} can start
using this immediately.

I've saved the details in plans/capstone-quick-win.md. This is the kind
of result we'll deliver across all three phases of the roadmap.
```

**STOP and wait for confirmation.**

---

## Stage 11: SUMMARY & NEXT STEPS

**Goal:** Finalise the workspace and confirm everything's ready.

**Actions:**

1. Update `CLAUDE.md` in the client workspace -- replace all remaining placeholders with real data
2. Review all context files -- confirm nothing was missed (now includes business-hierarchy.md and champions.md)
3. Present final summary:

```
Client AIOS workspace for {client} is ready.

What's been created:
  - Full context layer (8 files with real business data)
  - Pain point discovery (3 pain points ranked by ROI)
  - Business hierarchy map (org chart, process flows, communication channels)
  - AI Champions identified ({primary_champion} leads adoption)
  - Automation roadmap (3 phases, {X} modules planned)
  - Integration inventory ({X} tools mapped, {X} API keys needed)
  - Capstone quick win ({description} -- already working)
  - Database framework ready
  - .env prepared for API keys

Next steps:
  1. Collect API keys from {client} for: {list}
  2. Open the client workspace: cd clients/{client-name}
  3. Get the AI Champion their next quick win (capstone was the first -- keep the momentum)
  4. Build the 3 core automations (Build Three rule -- no expansion until these are in production)
  5. Schedule 30-min walkthrough with {primary_champion} in week 1
  6. First value should be visible within {timeframe}

The workspace is at: clients/{client-name}/
Run /prime from inside that folder to load the client context.
```

---

## Quality Standards

- Every context file must have REAL content, not placeholders
- Pain points must include cost estimates (time and money)
- Business hierarchy must map actual process flows with named people and tools
- Champions file must identify at least one primary champion with a clear first quick win
- Capstone quick win must be tangible -- something the client can see, touch, and use
- Automation roadmap must have concrete modules, not vague descriptions
- The ROI calculation must show clear value (client cost of problems vs. ForeShiloh fee)
- Integration inventory must clearly show what API keys are needed and their status
