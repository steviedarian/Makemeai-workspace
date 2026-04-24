# Demo

> Run a sales demo for a prospect. Generates a branded deliverable in under 5 minutes that creates instant "wow" value. Use before or during prospect meetings.

## Variables

demo_type: $ARGUMENTS (which demo to run: `scanner`, `content`, `leads`, `competitor`, or `all`)

---

## Instructions

You are running a **ForeShiloh sales demo**. The goal is to create instant, tangible value for a prospect using ONLY publicly available information. No API keys from the prospect needed.

These demos are Trojan horses -- they show a small fraction of what the AIOS can do, creating the "holy shit" moment that opens the door to a full engagement.

### Critical Rules

- **Speed matters.** The whole point is showing value in minutes. Don't spend 20 minutes researching. Get to the output fast.
- **Branded output.** Every demo produces a ForeShiloh-branded HTML report saved to `outputs/demos/`.
- **Open it for Daniel.** After generating, open the HTML file so Daniel can show the prospect immediately.
- **End with the hook.** Every report ends with: "This used only public information. Imagine what we could do with full access to your systems."
- **Be conversational.** Daniel may be running this in front of a prospect. Keep your messages clean and professional.

---

## Demo A: Business Intelligence Scanner

**Command:** `/demo scanner`

**What to ask:** Business name and website URL.

**Process:**
1. Ask for the business name and website URL
2. **Web search** the business name -- find their Google reviews, social media profiles, competitor mentions
3. **Web fetch** their website -- analyse the content, messaging, services, calls to action
4. **Assess** these areas and score each 0-10:
   - **Website quality** (mobile-friendly, speed, clarity, CTAs, SEO basics)
   - **Social media presence** (which platforms, posting frequency, engagement)
   - **Online reviews** (Google rating, number of reviews, sentiment)
   - **Content marketing** (blog, video, newsletter, resources)
   - **Automation readiness** (contact forms, booking systems, CRM indicators, chatbots)
   - **Competitor positioning** (how they compare to top 3 local competitors)
5. Calculate an overall **AI Readiness Score** out of 100 (sum of 6 areas, weighted)
6. List **gaps** (what's missing or weak -- be specific)
7. List **opportunities** (what AI could fix -- tie each to time/money saved)
8. Write a **summary** paragraph: where they stand, biggest quick wins, and what the AIOS could do
9. Generate the HTML report using `scripts/demo_scanner.py` functions:
   - Import and call `generate_report_html(report)` with your findings
   - Save with `save_report(report, html)`
10. Open the HTML file for Daniel

---

## Demo B: Content Machine

**Command:** `/demo content`

**What to ask:** Business name and website URL (ideally About page).

**Process:**
1. Ask for the business name and website/About page URL
2. **Web fetch** the page -- extract their brand voice, tone, services, target audience, key messaging
3. **Analyse** the brand:
   - What's their tone? (professional, casual, technical, warm, authoritative)
   - Who are they talking to? (B2B, B2C, local, national)
   - What makes them different? (USP from their messaging)
4. **Generate 5 social media posts** (one per weekday):
   - Mix of platforms (LinkedIn, Instagram, Facebook, X -- pick what's relevant to their business)
   - Mix of content types (educational, behind-the-scenes, testimonial prompt, offer/CTA, industry insight)
   - Each post: platform, content type, full caption (ready to post), hashtags, and a brief note on why this post works
   - Match their brand voice exactly -- this should feel like THEIR content, not generic AI slop
5. Note the **brand voice** and **target audience** in the report header
6. Generate the HTML report using `scripts/demo_content.py` functions
7. Open the HTML file for Daniel

---

## Demo C: Lead Finder

**Command:** `/demo leads`

**What to ask:** Industry and location (e.g. "dental practices" "Sheffield").

**Process:**
1. Ask for the industry and location
2. **Define an ICP** for that industry: what makes a good prospect for AI automation? (size, revenue range, pain points typical to the industry, tech adoption signals)
3. **Web search** for businesses in that industry and location -- find 10 real businesses
4. For each business found:
   - Business name
   - Website URL
   - Estimated size (from website, LinkedIn, reviews)
   - Key contact (owner/manager name if publicly available, otherwise "TBD")
   - **AI Readiness Score** 0-100 based on: website quality, tech adoption signals, review volume (suggests business maturity), social presence, apparent pain points
   - Brief notes on why they're a good prospect
   - Specific AI opportunities for this business (1-3 tags)
5. **Rank** leads by score (highest first)
6. Write a **summary**: how many high-quality prospects found, common opportunities in this market, recommended approach
7. Generate the HTML report using `scripts/demo_leads.py` functions
8. Open the HTML file for Daniel

---

## Demo D: Competitive Analysis

**Command:** `/demo competitor`

**What to ask:** Business name, website URL, and optionally 2-3 competitor URLs.

**Process:**
1. Ask for the business name and website URL
2. Ask for 2-3 competitor URLs. If the prospect doesn't have them (or to save time), say "I'll find them" and **web search** for top competitors in their space (same industry, same location or market segment)
3. **Web fetch** the prospect's website -- extract: services offered, pricing (if visible), unique selling points, calls to action, brand positioning
4. **Web search** the prospect's business -- find: social media profiles, Google reviews (rating + count), any press or mentions
5. For each competitor (2-3):
   - **Web fetch** their website -- extract: services, pricing, USPs, CTAs, brand positioning
   - **Web search** their name -- find: social media presence, Google reviews, any press or mentions
   - Build a profile: name, URL, services, pricing indicators, USPs, social platforms, review rating + count
6. **Build the SWOT analysis** for the prospect's business:
   - **Strengths**: where the prospect beats competitors (better reviews, unique services, stronger brand, pricing advantage)
   - **Weaknesses**: where the prospect falls short (missing services, weaker online presence, fewer reviews, outdated website)
   - **Opportunities**: gaps in the market none of the competitors are filling, underserved customer segments, AI/automation advantages
   - **Threats**: strong competitor moves, market trends working against them, pricing pressure
7. **Build the comparison matrix** -- a table comparing all businesses across:
   - Services offered (list key ones, check/cross for each business)
   - Pricing tier (budget / mid-range / premium, or actual figures if visible)
   - Website quality (score 1-5)
   - Social media presence (which platforms, activity level)
   - Google reviews (rating + count)
   - Online booking/automation (yes/no)
   - Content marketing (blog, video, newsletter)
   - Format each row as a list: [feature_name, client_value, competitor1_value, competitor2_value, ...]
8. **Gap analysis** -- list specific things competitors do that the prospect does not. Be concrete: "Competitor X offers online booking, you don't" not "they have better tech"
9. **Calculate Opportunity Score** 0-100:
   - Market gaps available (0-25): how many gaps exist that no competitor fills well
   - Competitive weaknesses (0-25): how beatable are the competitors in key areas
   - Quick win potential (0-25): how many improvements could be made in under 30 days
   - AI/automation advantage (0-25): how much could AI close the gaps faster than competitors
10. **Quick win recommendations** -- 5 specific, actionable things the prospect could do in the next 30 days to gain ground on competitors. Each should reference a specific gap or weakness found. Prioritise by impact.
11. Write a **summary** paragraph: competitive position overview, biggest vulnerability, biggest opportunity, and what the AIOS could do to close the gaps
12. Generate the HTML report using `scripts/demo_competitor.py` functions:
    - Import and call `generate_report_html(report)` with your findings
    - Save with `save_report(report, html)`
13. Open the HTML file for Daniel

**Time target:** Under 3 minutes. Don't over-research. Fetch each site once, search each name once, then synthesise.

---

## Running All Four

**Command:** `/demo all`

Ask for: Business name, website URL, industry, and location. Optionally, competitor URLs.

Run all four demos in sequence:
1. Scanner (on the prospect's own business)
2. Content (on the prospect's website)
3. Competitor (on the prospect vs. their competitors)
4. Leads (on the prospect's industry + location -- finding them more customers)

This is the full sales demo package. Four branded reports in under 15 minutes.

---

## Output Location

All demos save to `outputs/demos/` with dated filenames:
- `2026-04-03-scanner-{business-name}.html`
- `2026-04-03-content-{business-name}.html`
- `2026-04-03-competitor-{business-name}.html`
- `2026-04-03-leads-{industry}-{location}.html`
