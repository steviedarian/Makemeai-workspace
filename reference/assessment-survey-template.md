# AI Readiness Assessment Survey -- Question Template

**Division:** ForeShiloh Solutions
**Purpose:** Pre-engagement questionnaire sent to client employees. AI analyzes responses to identify the top 2-3 processes to optimize.
**Method:** Based on Matteo's approach (Liam Ottley / AAA Accelerator) -- automated assessment before any consulting work begins.
**Time to complete:** 10-15 minutes per respondent
**Recommended:** Send to 3-8 employees across different roles/departments for best coverage.

---

## How to Use This Template

1. Generate the survey: `python scripts/assessment_survey.py generate --client "Client Name"`
2. Send the HTML file to the client (email attachment or hosted link)
3. Each employee fills it out and exports their response as JSON
4. Collect all JSON responses into a single array
5. Run analysis: `python scripts/assessment_survey.py analyze responses.json --report`
6. Send the analysis prompt to Claude to get structured recommendations
7. Render the branded report with `generate_report_html()`

---

## Survey Questions

### Q1: Role Context
**Question:** What is your job title and which department do you work in?

**Why this matters:** Establishes who is answering and what part of the business they see. Different roles surface different bottlenecks. Operations and admin roles tend to have the most automatable work.

**What to look for in answers:**
- Coordination-heavy roles (operations, admin, account management) -- these have the most automation potential
- Roles that bridge multiple departments -- these people see system-wide friction
- Anyone who describes their role as "a bit of everything" -- usually drowning in manual work

---

### Q2: Daily Workflow
**Question:** Walk us through a typical work day. What are the first 3 things you do when you start, and what takes up most of your afternoon?

**Why this matters:** Surfaces the actual daily rhythm. Morning tasks are often data-gathering or status-checking (highly automatable). Afternoon blocks reveal where deep work gets interrupted.

**What to look for in answers:**
- Repetitive morning routines: checking dashboards, pulling reports, reading emails to extract information
- Afternoons lost to meetings or chasing updates from colleagues
- Patterns like "I start by..." followed by data gathering from multiple sources
- Any mention of "catching up" or "checking in" -- these are information flow problems

---

### Q3: Repetitive Tasks
**Question:** Which tasks do you do every single day or week that feel like they could run on autopilot? List as many as you can think of.

**Why this matters:** Direct identification of automation candidates. People know what feels repetitive -- they just do not know it can be automated. This is the most valuable question in the survey.

**What to look for in answers:**
- Data entry (moving information from one system to another)
- Report generation (pulling numbers, formatting, distributing)
- Status updates (telling people what happened, where things stand)
- Invoice processing, scheduling, email sorting
- Anything described as "boring" or "tedious" -- automation gold
- Tasks that happen on a fixed schedule (daily, weekly, monthly)

---

### Q4: Time Allocation
**Question:** Roughly what percentage of your week is spent on: (a) repetitive admin/data tasks, (b) communication and coordination, (c) creative or strategic work, (d) meetings?

**Why this matters:** Quantifies the problem. This is the number you put in front of the CEO. If someone spends 60% on admin and coordination, that is 60% recoverable bandwidth.

**What to look for in answers:**
- Admin above 40% is a red flag -- the person is an expensive data processor
- Communication/coordination above 25% means the business is paying people to be messengers
- Creative/strategic below 20% means the business is losing its most valuable human output
- Meeting time above 30% combined with high coordination time -- the business has a trust/visibility problem

---

### Q5: Tools and Systems
**Question:** List all the software tools, apps, and systems you use in a typical week.

**Why this matters:** Maps the tech stack. Integration points between tools are where automation lives. Manual data transfer between systems is the number one automation opportunity in most businesses.

**What to look for in answers:**
- Multiple disconnected tools (data lives in spreadsheets AND a CRM AND email)
- Manual exports and imports between systems
- Copy-pasting between systems (the clearest automation signal)
- Spreadsheets used as databases -- a sign the business has outgrown its tools
- Any tool mentioned by multiple people as frustrating

---

### Q6: Information Flow
**Question:** How do you currently get the information you need to do your job? Do you have to ask colleagues, check multiple systems, or search through emails/documents?

**Why this matters:** Reveals information bottlenecks. If people spend time hunting for data, an AI layer that surfaces the right info at the right time creates immediate value.

**What to look for in answers:**
- Chasing colleagues for updates (dependency bottleneck)
- Searching through email threads (information trapped in communication)
- Checking 3+ systems to get a complete picture (fragmented data)
- Waiting for someone to send a report (gatekeeper bottleneck)
- "I just ask [person's name]" -- that person is a single point of failure

---

### Q7: Bottlenecks
**Question:** What is the single biggest thing that slows you down or frustrates you in your daily work? Be specific.

**Why this matters:** Emotional pain points drive buy-in. The thing that frustrates someone most is often the thing they will champion getting fixed. This question finds your internal advocates.

**What to look for in answers:**
- Waiting for approvals (process bottleneck -- automate routing)
- Manual data entry (classic automation target)
- Switching between too many tools (integration opportunity)
- Unclear processes (documentation + automation opportunity)
- Information silos ("I never know what the other team is doing")
- Repetitive reporting ("I spend every Monday morning building the same report")

---

### Q8: Communication Overhead
**Question:** How much time per day do you spend on internal communication just to coordinate work or get status updates?

**Options:** Less than 30 minutes / 30 min to 1 hour / 1 to 2 hours / 2 to 3 hours / More than 3 hours

**Why this matters:** Communication overhead is one of the biggest hidden costs in any business. Automated status updates, summaries, and smart routing can reclaim hours per person per day.

**What to look for in answers:**
- Anything above 1 hour is a strong signal
- 2+ hours means the business is paying people to be messengers instead of doing their actual job
- If most respondents say 2+ hours, the business has a systemic coordination problem -- fix this first
- Compare with Q6 -- high communication time + poor information access = compounding waste

---

### Q9: Data and Reporting
**Question:** Do you create or update any reports, spreadsheets, or dashboards regularly? If yes, describe what they are and how often.

**Why this matters:** Report generation is one of the easiest automation wins. If someone spends 2 hours building a weekly report from multiple sources, that can often be fully automated in a single sprint.

**What to look for in answers:**
- Weekly or monthly reports pulled from multiple sources
- Manual chart updates or slide deck number refreshes
- Copying figures from one system into another
- Reports that go to leadership (high visibility = high impact when automated)
- Any report described as "taking ages" or "painful"

---

### Q10: Decision Making
**Question:** Are there decisions in your role that follow a clear pattern or set of rules? For example: "If X happens, I always do Y."

**Why this matters:** Rule-based decisions are prime automation targets. If the logic can be described as if-then, it can be automated. This question surfaces hidden decision trees that people follow without realising.

**What to look for in answers:**
- Routing enquiries to the right person based on criteria
- Approving or rejecting based on thresholds
- Categorising incoming requests
- Prioritising tasks by urgency or client tier
- Any "I always..." or "the rule is..." language

---

### Q11: Customer/Client Interaction
**Question:** Do you handle customer or client enquiries? If yes, what percentage of questions are repetitive?

**Why this matters:** Repetitive customer queries are a textbook use case for AI assistants and automated responses. High repetition rates mean fast ROI.

**What to look for in answers:**
- Repetition above 30% -- strong candidate for AI-assisted responses
- FAQ-style queries (same questions, same answers)
- Status check requests ("where is my order/project/invoice?")
- Onboarding questions asked by every new client
- If multiple respondents mention the same questions, that is a certainty signal

---

### Q12: Process Gaps
**Question:** Is there anything you currently do manually that you suspect a computer could handle? Even if you are not sure how -- just describe the task.

**Why this matters:** Lets people surface opportunities they have noticed but never actioned. Often the best ideas come from the people doing the work every day.

**What to look for in answers:**
- Any task described as "tedious", "boring", "time-consuming"
- Tasks that involve following a checklist or template
- Data transformation tasks (reformatting, cleaning, combining)
- Anything that starts with "I wish..." -- these are feature requests in disguise

---

### Q13: Impact Assessment
**Question:** If you could magically get back 2 hours every day, what would you spend that time on instead?

**Why this matters:** Reveals what the business is missing out on because people are stuck in operational work. This frames the ROI story for the client and shows the CEO what their team WOULD do if freed up.

**What to look for in answers:**
- Strategic planning, client relationships, training, product development
- Creative work, innovation, process improvement
- "Actually thinking about how to improve things" -- the business is too busy doing to improve
- Personal development or team mentoring -- signs of a culture-first employee

---

### Q14: Scale Challenges
**Question:** What breaks first when work volume increases? Where do things fall through the cracks?

**Why this matters:** Identifies processes that do not scale. These are the highest-impact automation targets because they directly limit growth. Fixing them removes the ceiling.

**What to look for in answers:**
- Onboarding delays when new clients come in fast
- Missed follow-ups or dropped tasks under pressure
- Quality drops (mistakes increase with volume)
- Overtime and burnout signals
- Hiring pressure ("we need another person for this")
- Anything that gets worse under load is a scaling bottleneck

---

### Q15: Quick Wins
**Question:** If we could fix just ONE thing about how you work tomorrow, what would make the biggest difference to your day?

**Why this matters:** Identifies the emotional priority. The "one thing" question cuts through noise and surfaces what matters most to each individual. This often becomes the pilot project.

**What to look for in answers:**
- The answer to this question often has built-in champion support
- Look for convergence -- if 3 people name the same thing, that is your pilot
- Simple answers are good ("just make the weekly report automatic") -- they are achievable
- Complex answers ("redesign our whole workflow") suggest deeper problems to explore

---

## Scoring Framework

When analyzing responses, score each candidate process on:

| Criterion | What it measures | 10 = Best |
|-----------|-----------------|-----------|
| Repetitiveness | How repetitive and predictable is the task? | Identical every time |
| Ease of mapping | How clearly can the process steps be defined? | Crystal clear steps |
| Time to optimize | How quickly could this be automated? | Days, not months |
| Visible impact | How noticeable will the improvement be? | Everyone feels it |
| Scale benefit | Does fixing this help when volume grows? | Removes a ceiling |

**Total score out of 50.** Take the top 2-3 and build the engagement around them.

---

## Tips for Best Results

- Send to 3-8 employees across different roles and departments
- Include at least one person from operations, one client-facing, one back-office
- Emphasise confidentiality -- honest answers matter more than polished ones
- Do NOT send to just the CEO/owner -- they often have a different view from the team
- The best insights come from people who do the actual work, not people who manage the work
