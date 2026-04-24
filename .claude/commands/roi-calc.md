# /roi-calc -- AI ROI Calculator

> Calculate and present the ROI of AI opportunities using the proven 3-part formula: A (Time Cost) + B (Lost Revenue) + C (Freed Capacity) = Total Impact.
> Generates a branded ForeShiloh HTML report for Architecture client proposals.

## How It Works

The ROI model has 3 components per opportunity:
- **Section A** (always): Cost of Inefficiency -- time wasted x people x 260 days x hourly rate
- **Section B** (if applicable): Lost Revenue -- revenue walking out the door due to the problem
- **Section C** (if applicable): Freed Capacity Revenue -- new revenue from reinvested saved time

**Key rule:** Never double-count. If the time saving IS the revenue fix (like speed-to-lead), don't use both B and C.

## Flow

### Step 1: Client Details
Ask for:
- Client/company name
- Website (optional)
- Which departments or areas were audited

### Step 2: Opportunities
For each AI opportunity identified (aim for 3-5 top priorities):

1. **Name and description** of the opportunity
2. **Department** it belongs to
3. **Which sections apply** (use this decision tree):
   - A only = just time savings, no revenue impact (e.g. automated reporting)
   - A + B = time savings AND revenue is leaking today (e.g. speed-to-lead, slow quotes)
   - A + C = time savings AND freed time enables NEW revenue work (e.g. RFP generator frees AMs for prospecting)
   - A + B + C = all three, but B and C must measure DIFFERENT revenue streams (e.g. AI customer success: B=churn prevention, C=upsells)

4. **Section A data** (always):
   - Hours wasted per person per day
   - Number of people doing this task
   - Loaded hourly cost (benchmarks: GBP 15-20/hr admin, GBP 30-40/hr specialist, GBP 50-75/hr manager)
   - Source (where did this number come from -- interview quote, CRM data, finance)
   - Rationale (why this is conservative)

5. **Section B data** (if applicable):
   - Volume affected per month (leads, orders, tickets, etc.)
   - Percent lost due to the problem
   - Value per unit
   - Source and rationale

6. **Section C data** (if applicable):
   - Additional activities per month the team could do with freed time
   - Conversion rate on those activities
   - Value per conversion
   - Source and rationale

7. **Solution costs:**
   - Implementation cost (ForeShiloh build quote)
   - Annual tool/licence cost

### Step 3: Executive Summary
Write a 2-3 paragraph executive summary that:
- Frames the total as cost of inaction ("This costs your business GBP X every year you don't fix it")
- Highlights the top 2-3 opportunities by impact
- Shows the math transparently
- Is conservative -- use the low end of any range
- Mentions intangibles (faster response, reduced burnout, scale without hiring)

### Step 4: Generate Report
```python
import sys
sys.path.insert(0, ".")
from scripts.roi_calculator import create_report, create_opportunity, generate_report_html, save_report, save_json

# Create report
report = create_report(client_name="...", client_website="...")

# Add opportunities (repeat for each)
opp = create_opportunity(name="...", description="...", department="...", sections="A+B")
opp["section_a"]["hours_per_person_per_day"] = ...
opp["section_a"]["num_people"] = ...
opp["section_a"]["loaded_hourly_cost"] = ...
opp["section_a"]["source"] = "..."
opp["section_a"]["rationale"] = "..."
# Fill B and C as applicable...
opp["implementation_cost"] = ...
opp["annual_tool_cost"] = ...
report["opportunities"].append(opp)

# Set executive summary
report["executive_summary"] = "..."

# Generate and save
html = generate_report_html(report)
html_path = save_report(report, html)
json_path = save_json(report)
print(f"Report saved to {html_path}")
```

### Step 5: Present
- Tell Daniel the total annual impact, investment, and ROI
- Open the HTML report: `open {html_path}`
- Mention the JSON is saved for future editing

## Quick Reference: Common Opportunities

| Opportunity | Sections | Why |
|---|---|---|
| AI RFP/Proposal Generator | A + C | Time saved, team reinvests into meetings |
| Speed-to-Lead Autoresponder | A + B | Leads going cold, revenue walking out |
| After-Hours AI Receptionist | A + B | Missed calls = missed jobs |
| AI Customer Success Agent | A + B + C | B=churn, C=upsells (different streams) |
| Invoice/AP Automation | A only | Time saved, no revenue impact |
| AI Quote Generator | A + B | Slow quotes, prospects go to competitors |
| Automated Reporting | A only | Hours saved on manual reporting |
| AI Scheduling/Booking | A + B | Scheduling gaps = empty revenue slots |
| AI Chatbot for Support | A + B + C | B=churn from slow resolution, C=outreach |
| Content Automation | A + C | Time saved, team runs more campaigns |

## Hourly Rate Benchmarks (GBP)

| Role | Loaded Hourly Cost |
|---|---|
| Admin/receptionist | GBP 15-20 |
| Skilled worker/specialist | GBP 30-40 |
| Manager/senior | GBP 50-75 |
| Director/executive | GBP 80-120 |

## Presentation Tips
- Be conservative. Use low end of ranges.
- Show math: "2 hrs x 8 people x 260 days x GBP 40/hr = GBP 166,400"
- Frame as cost of inaction: "This costs you GBP X every year you don't fix it"
- Stack opportunities: "Across all 3, you're leaving GBP X on the table"
- Source everything. Every number needs a citation.

## Notes
- Currency defaults to GBP but can be changed per opportunity
- The HTML report includes print-friendly CSS for PDF export
- JSON output allows re-running or adjusting numbers later
- This pairs with /demo scanner (for initial wow) and /client-setup (for full onboarding)
