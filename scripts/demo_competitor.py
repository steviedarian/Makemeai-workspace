"""
Demo D: Competitive Analysis

Takes a business website and competitor URLs. Scrapes publicly available info
and generates a branded competitive analysis report with SWOT, comparison matrix,
gap analysis, opportunity scoring, and quick win recommendations.

Usage:
    python scripts/demo_competitor.py "Business Name" "https://their-website.com"

This is a SALES DEMO tool. Run it before or during a prospect meeting
to create an instant "wow" moment. Takes < 3 minutes.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent


def analyse_competitors(name: str, website: str, competitors: list = None) -> dict:
    """
    Analyse a business against its competitors using publicly available information.
    Returns a structured report dict.

    NOTE: This script is designed to be run by Claude Code, which has
    web search and web fetch capabilities. The script structures the
    output - Claude does the actual research.
    """
    report = {
        "business_name": name,
        "website": website,
        "scan_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "competitors": competitors or [],
        "client_profile": {
            "services": [],
            "pricing": "",
            "usps": [],
            "social_media": {},
            "reviews": {"rating": 0, "count": 0, "sentiment": ""}
        },
        "competitor_profiles": [],
        "swot": {
            "strengths": [],
            "weaknesses": [],
            "opportunities": [],
            "threats": []
        },
        "comparison_matrix": [],
        "gap_analysis": [],
        "opportunity_score": 0,
        "quick_wins": [],
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


def generate_report_html(report: dict) -> str:
    """Generate a branded HTML report from competitive analysis results."""
    payment_link = load_payment_link()

    # SWOT quadrants
    def swot_items(items, icon, color):
        html = ""
        for item in items:
            html += f'<div class="swot-item"><span style="color:{color};font-weight:700;margin-right:8px;">{icon}</span> {item}</div>\n'
        return html

    strengths_html = swot_items(report["swot"].get("strengths", []), "&#9650;", "#22c55e")
    weaknesses_html = swot_items(report["swot"].get("weaknesses", []), "&#9660;", "#ef4444")
    opportunities_html = swot_items(report["swot"].get("opportunities", []), "&#10003;", "#3b82f6")
    threats_html = swot_items(report["swot"].get("threats", []), "!", "#f59e0b")

    # Comparison matrix
    matrix_rows = ""
    for row in report.get("comparison_matrix", []):
        cells = ""
        for i, cell in enumerate(row):
            tag = "th" if i == 0 else "td"
            cells += f"<{tag}>{cell}</{tag}>"
        matrix_rows += f"<tr>{cells}</tr>\n"

    # Build matrix header from competitor names
    matrix_header = f"<th>Feature</th><th>{report['business_name']}</th>"
    for comp in report.get("competitor_profiles", []):
        matrix_header += f"<th>{comp.get('name', 'Competitor')}</th>"

    # Gap analysis
    gaps_html = ""
    for gap in report.get("gap_analysis", []):
        gaps_html += f'<div class="gap-item"><span class="gap-icon">&#9679;</span> {gap}</div>\n'

    # Quick wins
    wins_html = ""
    for i, win in enumerate(report.get("quick_wins", []), 1):
        wins_html += f'<div class="win-item"><span class="win-num">{i}</span> {win}</div>\n'

    # Opportunity score
    opp_score = report.get("opportunity_score", 0)
    score_color = "#ef4444" if opp_score < 40 else "#f59e0b" if opp_score < 70 else "#22c55e"

    # Competitor count
    comp_count = len(report.get("competitor_profiles", []))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Competitive Analysis | {report['business_name']} | ForeShiloh</title>
<link href="https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Space+Grotesk:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #060608; --card: #111118; --border: rgba(255,255,255,0.07);
    --gold: #D4A843; --gold-bright: #F5C842; --text: #d4d4d8;
    --text-bright: #fafafa; --text-dim: rgba(255,255,255,0.38);
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'DM Sans', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; padding: 40px; }}
  .container {{ max-width: 960px; margin: 0 auto; }}
  .wordmark {{ font-family: 'Julius Sans One', sans-serif; letter-spacing: 8px; font-size: 12px; }}
  .wordmark .fore {{ color: rgba(255,255,255,0.5); }}
  .wordmark .shiloh {{ color: var(--gold); }}
  .header {{ display: flex; justify-content: space-between; align-items: center; padding-bottom: 24px; border-bottom: 1px solid var(--border); margin-bottom: 32px; }}
  .header-right {{ text-align: right; font-size: 11px; color: var(--text-dim); }}
  h1 {{ font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 600; color: var(--text-bright); margin-bottom: 8px; }}
  h2 {{ font-family: 'Space Grotesk', sans-serif; font-size: 20px; font-weight: 600; color: var(--text-bright); margin-bottom: 16px; }}
  .subtitle {{ font-size: 14px; color: var(--text-dim); margin-bottom: 32px; }}
  .card {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 20px; }}
  .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}

  /* Score ring */
  .score-ring {{ width: 120px; height: 120px; border-radius: 50%; border: 4px solid {score_color}; display: flex; align-items: center; justify-content: center; flex-direction: column; margin: 0 auto 24px; }}
  .score-num {{ font-family: 'Space Grotesk', sans-serif; font-size: 36px; font-weight: 700; color: {score_color}; }}
  .score-label {{ font-size: 10px; text-transform: uppercase; letter-spacing: 2px; color: var(--text-dim); }}

  /* SWOT */
  .swot-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px; }}
  .swot-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; }}
  .swot-card h3 {{ font-family: 'Space Grotesk', sans-serif; font-size: 16px; font-weight: 600; margin-bottom: 12px; }}
  .swot-item {{ padding: 6px 0; font-size: 13px; display: flex; align-items: flex-start; }}

  /* Comparison table */
  .matrix-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  .matrix-table th {{ font-family: 'Space Grotesk', sans-serif; font-weight: 600; text-align: left; padding: 10px 12px; border-bottom: 2px solid var(--gold); color: var(--gold); font-size: 12px; text-transform: uppercase; letter-spacing: 1px; }}
  .matrix-table td {{ padding: 10px 12px; border-bottom: 1px solid var(--border); }}
  .matrix-table tr:hover td {{ background: rgba(212,168,67,0.03); }}

  /* Gap analysis */
  .gap-item {{ padding: 10px 0; border-bottom: 1px solid var(--border); font-size: 14px; display: flex; align-items: flex-start; gap: 10px; }}
  .gap-icon {{ color: #f59e0b; font-size: 8px; flex-shrink: 0; margin-top: 6px; }}

  /* Quick wins */
  .win-item {{ padding: 12px 0; border-bottom: 1px solid var(--border); font-size: 14px; display: flex; align-items: flex-start; gap: 12px; }}
  .win-num {{ background: var(--gold); color: #000; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px; flex-shrink: 0; }}

  .summary {{ font-size: 15px; color: var(--text); line-height: 1.8; padding: 24px; background: rgba(212,168,67,0.05); border: 1px solid rgba(212,168,67,0.15); border-radius: 12px; margin-top: 32px; }}
  .cta {{ text-align: center; margin-top: 40px; padding: 32px; border: 1px solid rgba(212,168,67,0.2); border-radius: 12px; background: rgba(212,168,67,0.03); }}
  .cta h3 {{ font-family: 'Space Grotesk', sans-serif; color: var(--gold-bright); font-size: 18px; margin-bottom: 8px; }}
  .cta p {{ font-size: 13px; color: var(--text-dim); }}
  .cta-btn {{ display: inline-block; margin-top: 20px; padding: 14px 36px; background: var(--gold); color: #060608; font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: 15px; text-decoration: none; border-radius: 8px; letter-spacing: 0.5px; transition: background 0.2s; }}
  .cta-btn:hover {{ background: var(--gold-bright); }}
  .cta-price {{ font-family: 'Space Grotesk', sans-serif; font-size: 28px; font-weight: 700; color: var(--gold-bright); margin: 12px 0 4px; }}
  .cta-sub {{ font-size: 12px; color: var(--text-dim); margin-bottom: 16px; }}
  .footer {{ text-align: center; margin-top: 40px; padding-top: 24px; border-top: 1px solid var(--border); }}
  .footer p {{ font-size: 11px; color: rgba(255,255,255,0.2); }}
  .section-label {{ font-size: 11px; text-transform: uppercase; letter-spacing: 3px; color: var(--gold); margin-bottom: 16px; }}
  @media print {{
    body {{ background: #fff; color: #1a1a1a; }}
    .card, .swot-card {{ background: #f8f8f8; border: 1px solid #ddd; }}
    :root {{ --text: #1a1a1a; --text-bright: #000; --text-dim: #888; --gold: #8B7226; }}
  }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="wordmark"><span class="fore">FORE</span><span class="shiloh">SHILOH</span></div>
    <div class="header-right">Competitive Analysis<br>{report['scan_date']}</div>
  </div>

  <h1>{report['business_name']}</h1>
  <div class="subtitle">{report['website']} | vs. {comp_count} competitor{"s" if comp_count != 1 else ""}</div>

  <!-- Opportunity Score -->
  <div style="text-align: center; margin-bottom: 32px;">
    <div class="score-ring">
      <div class="score-num">{opp_score}</div>
      <div class="score-label">Opportunity</div>
    </div>
    <p style="font-size: 13px; color: var(--text-dim);">Competitive Opportunity Score out of 100</p>
  </div>

  <!-- SWOT Analysis -->
  <div class="section-label">SWOT Analysis</div>
  <div class="swot-grid">
    <div class="swot-card">
      <h3 style="color: #22c55e;">Strengths</h3>
      {strengths_html}
    </div>
    <div class="swot-card">
      <h3 style="color: #ef4444;">Weaknesses</h3>
      {weaknesses_html}
    </div>
    <div class="swot-card">
      <h3 style="color: #3b82f6;">Opportunities</h3>
      {opportunities_html}
    </div>
    <div class="swot-card">
      <h3 style="color: #f59e0b;">Threats</h3>
      {threats_html}
    </div>
  </div>

  <!-- Comparison Matrix -->
  <div class="card">
    <div class="section-label">Competitor Comparison</div>
    <table class="matrix-table">
      <thead><tr>{matrix_header}</tr></thead>
      <tbody>{matrix_rows}</tbody>
    </table>
  </div>

  <!-- Gap Analysis -->
  <div class="card">
    <div class="section-label">Gap Analysis</div>
    <h2>What Competitors Do That You Don't</h2>
    {gaps_html}
  </div>

  <!-- Quick Wins -->
  <div class="card">
    <div class="section-label">Recommendations</div>
    <h2>Quick Wins</h2>
    {wins_html}
  </div>

  <div class="summary">
    <h2>Summary</h2>
    <p>{report.get('summary', '')}</p>
  </div>

  <div class="cta">
    <h3>Imagine what we could do with full access.</h3>
    <p>This analysis used only public information. With access to your systems, data, and processes, we can build an AI Operating System that turns these gaps into advantages while you sleep.</p>
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
    """Save the report as HTML."""
    output_dir = WORKSPACE_ROOT / "outputs" / "demos"
    output_dir.mkdir(parents=True, exist_ok=True)

    safe_name = report["business_name"].lower().replace(" ", "-").replace("'", "")
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-competitor-{safe_name}.html"
    filepath = output_dir / filename

    filepath.write_text(html)
    return str(filepath)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/demo_competitor.py 'Business Name' 'https://website.com'")
        print("\nBut this script is designed to be run BY Claude Code, not standalone.")
        print("Use: /demo competitor 'Business Name' 'https://website.com'")
        sys.exit(1)

    name = sys.argv[1]
    website = sys.argv[2]
    competitors = sys.argv[3:] if len(sys.argv) > 3 else []
    report = analyse_competitors(name, website, competitors)
    print(json.dumps(report, indent=2))
