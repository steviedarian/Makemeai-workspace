# AI Audit ROI Calculator -- Reference Guide

> Source: Morningside AI webinar (8 April 2026). Template provided as Google Sheets.

## The Formula

**Total Annual Impact = Section A + Section B + Section C**

### Section A -- Cost of Inefficiency (always fill this in)

Every AI opportunity starts with wasted time.

```
Time wasted per person per day x # people x 260 days/year x loaded hourly cost
= Annual Cost of Inefficiency
```

Example: 2 hrs/day x 8 SDRs x 260 days x $40/hr = $166,400/year wasted

### Section B -- Lost Revenue (only if revenue is leaking TODAY)

Test: "Even if the team were perfectly efficient, would money still be leaking?"
- If YES: fill in Section B
- If NO (just a time problem): skip

```
Volume affected per month x % lost x value per unit x 12 months
= Annual Lost Revenue
```

Example: 800 leads/month x 30% lost to slow response x $375/lead x 12 = $1,080,000/year

### Section C -- Freed Capacity Revenue (only if saved time enables NEW revenue work)

Test: "Can I point to a specific activity the team will now have time to do?"
- If YES: fill in Section C
- If the time saving IS the revenue fix (like speed-to-lead): skip (would double-count with B)

```
Additional activities per month x conversion rate x value per conversion x 12 months
= Annual Revenue from Freed Capacity
```

Example: 20 extra meetings/month x 25% close rate x $1,500/deal x 12 = $90,000/year

## Quick Reference: Common AI Opportunities

| AI Opportunity | Sections | Why |
|---|---|---|
| AI RFP/Proposal Generator | A + C | Time saved, AMs reinvest into meetings/prospecting |
| Speed-to-Lead Autoresponder | A + B | Leads going cold, revenue walking out the door |
| After-Hours AI Receptionist | A + B | Missed calls = missed jobs |
| AI Customer Success Agent | A + B + C | B = churn prevention, C = freed CSMs run upsells |
| Invoice/AP Automation | A only | Time saved, no revenue impact |
| AI Quote Generator | A + B | Slow quotes = prospects go to competitors |
| Automated Reporting/Dashboards | A only | Hours saved on manual reporting |
| AI Scheduling/Booking | A + B | No-shows and scheduling gaps = empty revenue slots |
| AI Chatbot for Support | A + B + C | B = churn from slow resolution, C = proactive outreach |
| Social Media/Content Automation | A + C | Time saved, marketing runs more campaigns |

## Where the Numbers Come From

| Data Point | Source |
|---|---|
| Time wasted per day | Stakeholder interview ("I spend about 2 hours every morning on this") |
| Number of people affected | Stakeholder interview ("Our whole team of 8 does this") |
| Loaded hourly cost | HR/Finance, or benchmarks: $20-30/hr admin, $40-50/hr specialist, $75-100/hr manager |
| Volume of leads/calls/orders | Stakeholder interview ("We get about 800 leads a month") |
| % lost due to problem | Stakeholder interview ("We probably lose 30% because we're too slow") |
| Value per lead/call/order | Annual customer value or average deal size -- ask Finance or Sales |
| Additional activities from saved time | Stakeholder interview ("If reps didn't have to do CRM updates, they could make 20 more calls a week") |
| Conversion rate | Stakeholder or CRM data ("We close about 25% of qualified meetings") |
| Implementation cost | Vendor quote or your own scope estimate |
| Tool/license cost | Vendor pricing page or quote |

## Presentation Tips

1. **Be conservative.** Use the low end of any range. If the conservative number still compels, it's solid. Underpromise, overdeliver.
2. **Show your math.** Don't just say "$166,000 wasted." Show: "2 hrs x 8 people x 260 days x $40/hr = $166,400." Transparency builds trust.
3. **Stack the opportunities.** Show individual ROI for each, then total: "Across all 3, you're leaving $250,000 on the table annually against an $80,000 investment."
4. **Frame as cost of inaction.** "This problem costs you $166,000 every year you don't fix it." More motivating than "you could save $166,000."
5. **Include intangibles.** Faster customer response, reduced burnout, ability to scale without hiring.
6. **Source everything.** When a CFO asks "where did this come from?" -- point to the Source column.

## Calculator Structure (Google Sheets)

1. **Instructions** -- How to use the template
2. **Opportunity Overview** -- List ALL opportunities, score on Impact/Frequency/Time/People/Benefits/Cost
3. **Summary Dashboard** -- Auto-rolls up all opportunities into one executive view
4. **Opp tabs** -- One per prioritised opportunity with Section A + B + C calculations

Colour legend:
- BLUE = Input cells (you fill these in)
- WHITE = Auto-calculated (formulas, don't edit)
- GRAY = Metadata (Definition, Source, Rationale)

## Engagement Phases (Morningside Model)

1. **Discovery (Weeks 1-3):** 20-30 stakeholder interviews. Deeply understand workflows, time sinks, inefficiencies.
2. **Analysis & Prioritisation (Weeks 4-6):** Identify 15-30 AI opportunities. Impact vs Effort matrix. Pick top 3-5.
3. **Packaging & Storytelling (Weeks 7-9):** Executive presentation, phased roadmap, mini prototypes.
