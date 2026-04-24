"""
Demo C: Lead Finder

Takes an industry and location. Finds businesses matching an ICP,
enriches them with basic info, and scores them.

Usage:
    python scripts/demo_leads.py "dental practices" "Sheffield"

Designed to be run by Claude Code via /demo leads command.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent


def find_leads(industry: str, location: str) -> dict:
    """
    Find and score leads in a given industry and location.
    Returns a structured leads report dict.

    NOTE: Claude Code does the actual web research.
    This script structures the output.
    """
    report = {
        "industry": industry,
        "location": location,
        "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "icp_description": "",
        "leads": [],  # List of {name, website, size, contact, score, notes, opportunities}
        "summary": ""
    }
    return report


def load_payment_link():
    """Load the Exploration Month payment link from Stripe config."""
    config_path = WORKSPACE_ROOT / "config" / "stripe_architecture_products.json"
    if config_path.exists():
        with open(config_path) as f:
            config = json.load(f)
        entry = config.get("entry") or config.get("exploration")
        if entry:
            return entry.get("one_off_payment_link", "")
    return ""


def generate_leads_html(report: dict) -> str:
    """Generate a branded HTML leads report."""
    payment_link = load_payment_link()
    leads_html = ""
    for i, lead in enumerate(report.get("leads", []), 1):
        score = lead.get("score", 0)
        score_color = "#ef4444" if score < 40 else "#f59e0b" if score < 70 else "#22c55e"

        opps = ""
        for opp in lead.get("opportunities", []):
            opps += f'<span class="opp-tag">{opp}</span> '

        leads_html += f"""
    <div class="lead-card">
      <div class="lead-header">
        <div>
          <div class="lead-rank">#{i}</div>
          <div class="lead-name">{lead.get('name', 'Unknown')}</div>
          <div class="lead-website">{lead.get('website', '')}</div>
        </div>
        <div class="lead-score" style="border-color: {score_color}; color: {score_color};">{score}</div>
      </div>
      <div class="lead-details">
        <div class="lead-meta">
          <span>Size: {lead.get('size', 'Unknown')}</span>
          <span>Contact: {lead.get('contact', 'TBD')}</span>
        </div>
        <div class="lead-notes">{lead.get('notes', '')}</div>
        <div class="lead-opps">{opps}</div>
      </div>
    </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lead Report | {report['industry']} in {report['location']} | ForeShiloh</title>
<link href="https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Space+Grotesk:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #060608; --card: #111118; --border: rgba(255,255,255,0.07);
    --gold: #D4A843; --gold-bright: #F5C842; --text: #d4d4d8;
    --text-bright: #fafafa; --text-dim: rgba(255,255,255,0.38);
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'DM Sans', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; padding: 40px; }}
  .container {{ max-width: 900px; margin: 0 auto; }}
  .wordmark {{ font-family: 'Julius Sans One', sans-serif; letter-spacing: 8px; font-size: 12px; }}
  .wordmark .fore {{ color: rgba(255,255,255,0.5); }}
  .wordmark .shiloh {{ color: var(--gold); }}
  .header {{ display: flex; justify-content: space-between; align-items: center; padding-bottom: 24px; border-bottom: 1px solid var(--border); margin-bottom: 32px; }}
  h1 {{ font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 600; color: var(--text-bright); margin-bottom: 8px; }}
  .subtitle {{ font-size: 14px; color: var(--text-dim); margin-bottom: 32px; }}
  .icp-box {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 32px; }}
  .icp-box h3 {{ font-family: 'Space Grotesk', sans-serif; font-size: 14px; color: var(--gold); margin-bottom: 8px; }}
  .icp-box p {{ font-size: 13px; color: var(--text-dim); }}
  .lead-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 12px; transition: border-color 0.3s; }}
  .lead-card:hover {{ border-color: rgba(255,255,255,0.15); }}
  .lead-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }}
  .lead-rank {{ font-family: 'Space Grotesk', sans-serif; font-size: 10px; font-weight: 600; letter-spacing: 0.2em; color: var(--gold); text-transform: uppercase; }}
  .lead-name {{ font-family: 'Space Grotesk', sans-serif; font-size: 18px; font-weight: 600; color: var(--text-bright); }}
  .lead-website {{ font-size: 12px; color: var(--text-dim); }}
  .lead-score {{ width: 48px; height: 48px; border-radius: 50%; border: 2px solid; display: flex; align-items: center; justify-content: center; font-family: 'Space Grotesk', sans-serif; font-size: 16px; font-weight: 700; flex-shrink: 0; }}
  .lead-meta {{ display: flex; gap: 24px; font-size: 12px; color: var(--text-dim); margin-bottom: 8px; }}
  .lead-notes {{ font-size: 13px; color: var(--text); margin-bottom: 10px; }}
  .lead-opps {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .opp-tag {{ display: inline-block; font-size: 10px; font-weight: 600; color: var(--gold); border: 1px solid rgba(212,168,67,0.25); padding: 3px 10px; border-radius: 100px; }}
  .summary-box {{ margin-top: 32px; padding: 24px; border: 1px solid rgba(212,168,67,0.2); border-radius: 12px; background: rgba(212,168,67,0.03); }}
  .summary-box h3 {{ font-family: 'Space Grotesk', sans-serif; color: var(--gold-bright); font-size: 16px; margin-bottom: 8px; }}
  .summary-box p {{ font-size: 14px; color: var(--text-dim); line-height: 1.8; }}
  .cta {{ text-align: center; margin-top: 40px; padding: 32px; border: 1px solid rgba(212,168,67,0.2); border-radius: 12px; background: rgba(212,168,67,0.03); }}
  .cta h3 {{ font-family: 'Space Grotesk', sans-serif; color: var(--gold-bright); font-size: 18px; margin-bottom: 8px; }}
  .cta p {{ font-size: 13px; color: var(--text-dim); }}
  .cta-btn {{ display: inline-block; margin-top: 20px; padding: 14px 36px; background: var(--gold); color: #060608; font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: 15px; text-decoration: none; border-radius: 8px; letter-spacing: 0.5px; transition: background 0.2s; }}
  .cta-btn:hover {{ background: var(--gold-bright); }}
  .cta-price {{ font-family: 'Space Grotesk', sans-serif; font-size: 28px; font-weight: 700; color: var(--gold-bright); margin: 12px 0 4px; }}
  .cta-sub {{ font-size: 12px; color: var(--text-dim); margin-bottom: 16px; }}
  .footer {{ text-align: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid var(--border); }}
  .footer p {{ font-size: 11px; color: rgba(255,255,255,0.2); }}
  @media print {{
    body {{ background: #fff; color: #1a1a1a; }}
    .lead-card {{ background: #f8f8f8; border: 1px solid #ddd; }}
  }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="wordmark"><span class="fore">FORE</span><span class="shiloh">SHILOH</span></div>
    <div style="text-align: right; font-size: 11px; color: var(--text-dim);">Lead Report<br>{report['generated_date']}</div>
  </div>

  <h1>{report['industry'].title()} in {report['location'].title()}</h1>
  <div class="subtitle">Top prospects ranked by AI-readiness score</div>

  <div class="icp-box">
    <h3>Ideal Customer Profile</h3>
    <p>{report.get('icp_description', 'Generated from industry analysis')}</p>
  </div>

  {leads_html}

  <div class="summary-box">
    <h3>What This Means</h3>
    <p>{report.get('summary', '')}</p>
  </div>

  <div class="cta">
    <h3>Imagine what we could do with full access.</h3>
    <p>This lead list was built from public data in minutes. With access to your CRM, sales pipeline, and customer data, we can build an AI prospecting engine that finds and scores leads for you automatically.</p>
    <div class="cta-price">&#163;2,500</div>
    <div class="cta-sub">Exploration Month -- one-off. Full AI audit, process mapping, automation roadmap, and a working prototype.</div>
    {"<a href='" + payment_link + "' class='cta-btn' target='_blank'>Get Started</a>" if payment_link else "<p style='margin-top: 16px; color: var(--gold);'>Contact us to get started.</p>"}
  </div>

  <div class="footer">
    <div class="wordmark" style="margin-bottom: 8px;"><span class="fore">FORE</span><span class="shiloh">SHILOH</span></div>
    <p>ForeShiloh Ltd | Sheffield, UK | foreshiloh.com</p>
  </div>
</div>
</body>
</html>"""
    return html


def save_report(report: dict, html: str):
    """Save the leads report as HTML."""
    output_dir = WORKSPACE_ROOT / "outputs" / "demos"
    output_dir.mkdir(parents=True, exist_ok=True)

    safe_name = f"{report['industry']}-{report['location']}".lower().replace(" ", "-")
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-leads-{safe_name}.html"
    filepath = output_dir / filename

    filepath.write_text(html)
    return str(filepath)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/demo_leads.py 'industry' 'location'")
        print("\\nDesigned to be run BY Claude Code via /demo leads command.")
        sys.exit(1)

    industry = sys.argv[1]
    location = sys.argv[2]
    report = find_leads(industry, location)
    print(json.dumps(report, indent=2))
