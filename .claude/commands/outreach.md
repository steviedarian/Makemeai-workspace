# Outreach

> Full prospect outreach pipeline. Takes a company name, researches them, finds contacts, runs an AI assessment, generates a branded PDF report, drafts personalised emails, and adds everything to the CRM. One command, complete outreach package.

## Variables

company: $ARGUMENTS (company name and location, e.g., "Zen Golf Studio Sheffield" or "Empire Aviation Dubai")

---

## Instructions

You are running the **ForeShiloh outreach pipeline**. This is a fully automated prospect research and outreach package builder. The goal is to produce everything Daniel needs to reach out to a prospect with a "wow factor" first impression.

### Critical Rules

- **No em dashes anywhere.** Not in emails, reports, or any output. Use commas, full stops, or rewrite.
- **Be specific.** Generic research is worthless. Find real names, real numbers, real pain points.
- **Show your homework.** Every report and email must demonstrate deep knowledge of the prospect's business.
- **Speed matters.** Use parallel agents where possible. The whole pipeline should complete in under 10 minutes.
- **Never guess email addresses.** Mark unverified emails clearly. Provide backup contact routes.
- **ForeShiloh brand standards.** Dark theme (#060608), gold (#D4A843), Playfair Display + DM Sans fonts. Strapline: "You dream, we build. AI powers them both."
- **Sign off as:** {{YOUR_NAME}}, {{YOUR_TITLE}}, {{YOUR_COMPANY}}
- **Calendly link:** {{YOUR_CALENDLY_LINK}}
- **Email:** {{YOUR_EMAIL}}

---

## Pipeline Stages

### Stage 1: RESEARCH (parallel agents)

Launch these in parallel:

**Agent A: Company Intel**
- What the company does, their size, revenue, employee count
- Current tech stack and digital presence (website quality, social media, booking systems)
- Google review count and rating
- Competitors and market position
- Pain points visible from outside (reviews, complaints, outdated systems)
- Any recent news, changes, or events

**Agent B: Contact Discovery**
- Find the decision-maker: Owner, MD, Commercial Director, Head of Digital, or CTO
- Get their full name, job title, email address, LinkedIn profile
- Check Companies House for directors
- Find backup contacts (2-3 alternatives)
- Determine email format (e.g., firstname.lastname@company.com)
- Check the company website contact page for direct routes

**Agent C: Website Scan**
- Run the scanner engine on their website if accessible: `from apps.scanner.scanner_engine import scan; results = scan(url)`
- If the scanner fails (Cloudflare blocking, etc.), do a manual assessment of the 6 categories:
  - Website Quality (out of 10)
  - Digital Presence (out of 10)
  - Automation (out of 10)
  - Content (out of 10)
  - Customer Experience (out of 10)
  - Technology (out of 10)
- Calculate an overall score out of 100

**Present findings to Daniel.** Summarise the company, key contact, score, and top 3 pain points. Ask if he wants to proceed or adjust anything before generating the report.

---

### Stage 2: AI ASSESSMENT REPORT

Generate a branded ForeShiloh HTML report. Use the template pattern from existing reports in `outputs/assessments/`.

**Use the demo scanner output** for CSS and structure reference:
Run `/demo scanner` on any business first to see the report format.

**Report structure:**
1. Cover page with ForeShiloh branding, company name, date
2. Executive Summary (personalised to the contact, reference specific business details)
3. AI Readiness Score with ring graphic (conic-gradient, matching score percentage)
4. Category breakdown (6 categories with bar charts)
5. Competitive landscape or key challenge section (industry-specific)
6. AI Opportunities (5-7, each with: description, estimated financial impact, deployment timeline, priority tier)
7. Total Impact Summary (aggregate savings/revenue uplift)
8. ForeShiloh Approach (three-step process)
9. Why Now section (4 reasons specific to their situation)
10. Next Steps with Calendly CTA
11. Contact footer

**Required CSS at top of style block:**
```css
@page { margin: 0; }
@media print {
  body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
```

**Financial estimates must be specific and justified.** Base them on industry benchmarks, company size, and identified pain points. Never use vague language like "significant savings."

Save to: `outputs/assessments/{date}-{company-slug}-ai-assessment.html`

---

### Stage 3: PDF GENERATION

Convert the HTML to PDF using Chrome headless:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="outputs/assessments/{date}-{company-slug}-ai-assessment.pdf" "outputs/assessments/{date}-{company-slug}-ai-assessment.html"
```

Verify the PDF was created and report the file size.

---

### Stage 4: EMAIL DRAFTS

Write a 3-email sequence:

**Email 1: Initial Outreach**
- Subject: Short, specific, references their business
- Open with something specific about their company (a number, a challenge, a recent event)
- Reference the attached report briefly
- One clear CTA: book a call or reply
- Under 150 words

**Email 2: Follow-up (3 days later)**
- Subject: Re: original subject
- Acknowledge they are busy
- Add one new specific insight or data point not in email 1
- Reattach the report
- Under 100 words

**Email 3: Final follow-up (7 days later)**
- Subject: Different angle
- Change the framing (e.g., competitor angle, cost-of-inaction, time-sensitive opportunity)
- Last touch, no pressure
- Under 100 words

---

### Stage 5: CRM ENTRY

Add to the CRM database (`data/data.db`):

1. **Company** in `crm_companies` (name, domain, type='prospect', industry, city, employees, revenue, notes)
2. **Contact** in `crm_contacts` (first_name, last_name, company_id, email, job_title, division='architecture', notes with backup contacts)
3. **Deal** in `crm_deals` (name, company_id, contact_id, division='architecture', stage_id=13 [Lead], amount, currency, probability=0.1, notes)
4. **Activity** in `crm_activities` (type='note', subject='AI Assessment Report Created', body with score and key details)

---

### Stage 6: SEND TOOL (if multiple prospects)

If Daniel is running `/outreach` for multiple companies in one session, offer to generate a consolidated send tool HTML file (copy/paste email tool with Gmail links, sent tracking, category filters). Follow the pattern in `outputs/outreach/`.

---

## Output Summary

After completing the pipeline, present:

```
## Outreach Package Ready

**Company:** {name}
**Contact:** {name} ({title}) - {email}
**Backup contacts:** {list}
**AI Score:** {score}/100
**Estimated Impact:** {range}

### Files Created
- PDF Report: outputs/assessments/{file}.pdf
- HTML Report: outputs/assessments/{file}.html

### CRM
- Company #{id}, Deal #{id}, Contact #{id}

### Email Sequence
- Email 1: {subject line}
- Email 2: {subject line}
- Email 3: {subject line}

### Recommended Approach
{1-2 sentences on best way to approach this specific prospect}
```

Open the PDF for Daniel to review before sending.
