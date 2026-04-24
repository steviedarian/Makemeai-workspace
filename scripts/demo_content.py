"""
Demo B: Content Machine

Takes a business name and website/About page URL.
Generates a full week of social media content (5 posts) in under 60 seconds.
Shows prospects what 5-10 hours of work looks like done in a minute.

Usage:
    python scripts/demo_content.py "Business Name" "https://their-website.com/about"

Designed to be run by Claude Code via /demo content command.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent


def generate_content_plan(name: str, url: str) -> dict:
    """
    Generate a week's content plan from public business info.
    Returns a structured plan dict.

    NOTE: Claude Code does the actual web scraping and content generation.
    This script structures the output.
    """
    plan = {
        "business_name": name,
        "source_url": url,
        "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "brand_voice": "",
        "target_audience": "",
        "posts": []  # List of {day, platform, type, caption, hashtags, notes}
    }
    return plan


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


def generate_content_html(plan: dict) -> str:
    """Generate a branded HTML content plan."""
    payment_link = load_payment_link()
    posts_html = ""
    for i, post in enumerate(plan.get("posts", []), 1):
        platform_colors = {
            "LinkedIn": "#0a66c2",
            "Instagram": "#e1306c",
            "Facebook": "#1877f2",
            "TikTok": "#000000",
            "X/Twitter": "#1da1f2"
        }
        color = platform_colors.get(post.get("platform", ""), "#6c63ff")

        posts_html += f"""
    <div class="post-card">
      <div class="post-header">
        <div>
          <span class="day-badge">Day {post.get('day', i)}</span>
          <span class="platform-badge" style="background: {color};">{post.get('platform', 'Social')}</span>
          <span class="type-badge">{post.get('type', 'Post')}</span>
        </div>
      </div>
      <div class="post-caption">{post.get('caption', '')}</div>
      <div class="post-hashtags">{post.get('hashtags', '')}</div>
      {f'<div class="post-notes">{post.get("notes", "")}</div>' if post.get("notes") else ''}
    </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Content Plan | {plan['business_name']} | ForeShiloh</title>
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
  .subtitle {{ font-size: 14px; color: var(--text-dim); margin-bottom: 12px; }}
  .brand-info {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 32px; }}
  .brand-info h3 {{ font-family: 'Space Grotesk', sans-serif; font-size: 14px; color: var(--gold); margin-bottom: 8px; }}
  .brand-info p {{ font-size: 13px; color: var(--text-dim); }}
  .post-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 16px; transition: border-color 0.3s; }}
  .post-card:hover {{ border-color: rgba(255,255,255,0.15); }}
  .post-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }}
  .day-badge {{ font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: var(--gold); margin-right: 10px; }}
  .platform-badge {{ display: inline-block; font-size: 10px; font-weight: 700; color: #fff; padding: 3px 10px; border-radius: 100px; margin-right: 8px; }}
  .type-badge {{ display: inline-block; font-size: 10px; font-weight: 600; color: var(--text-dim); border: 1px solid var(--border); padding: 3px 10px; border-radius: 100px; }}
  .post-caption {{ font-size: 14px; color: var(--text); line-height: 1.8; margin-bottom: 12px; white-space: pre-wrap; }}
  .post-hashtags {{ font-size: 12px; color: var(--gold); opacity: 0.7; }}
  .post-notes {{ font-size: 12px; color: var(--text-dim); font-style: italic; margin-top: 8px; padding-top: 8px; border-top: 1px solid var(--border); }}
  .time-saved {{ text-align: center; margin: 32px 0; padding: 32px; border: 1px solid rgba(212,168,67,0.2); border-radius: 12px; background: rgba(212,168,67,0.03); }}
  .time-saved .big {{ font-family: 'Space Grotesk', sans-serif; font-size: 48px; font-weight: 700; color: var(--gold-bright); }}
  .time-saved p {{ font-size: 14px; color: var(--text-dim); margin-top: 8px; }}
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
    .post-card {{ background: #f8f8f8; border: 1px solid #ddd; }}
  }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="wordmark"><span class="fore">FORE</span><span class="shiloh">SHILOH</span></div>
    <div style="text-align: right; font-size: 11px; color: var(--text-dim);">Content Plan<br>{plan['generated_date']}</div>
  </div>

  <h1>7-Day Content Plan</h1>
  <div class="subtitle">{plan['business_name']}</div>

  <div class="brand-info">
    <h3>Brand Voice</h3>
    <p>{plan.get('brand_voice', 'Extracted from website')}</p>
    <h3 style="margin-top: 12px;">Target Audience</h3>
    <p>{plan.get('target_audience', 'Identified from business context')}</p>
  </div>

  {posts_html}

  <div class="time-saved">
    <div class="big">5-10 hours saved</div>
    <p>This content plan was generated in under 60 seconds from your public website. Imagine what's possible with full access to your brand assets, analytics, and content calendar.</p>
  </div>

  <div class="cta">
    <h3>Imagine what we could do with full access.</h3>
    <p>This content plan used only your public website. With access to your brand assets, analytics, and content calendar, we can build an AI content engine that produces weeks of on-brand content while you sleep.</p>
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


def save_report(plan: dict, html: str):
    """Save the content plan as HTML."""
    output_dir = WORKSPACE_ROOT / "outputs" / "demos"
    output_dir.mkdir(parents=True, exist_ok=True)

    safe_name = plan["business_name"].lower().replace(" ", "-").replace("'", "")
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-content-{safe_name}.html"
    filepath = output_dir / filename

    filepath.write_text(html)
    return str(filepath)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/demo_content.py 'Business Name' 'https://website.com/about'")
        print("\\nDesigned to be run BY Claude Code via /demo content command.")
        sys.exit(1)

    name = sys.argv[1]
    url = sys.argv[2]
    plan = generate_content_plan(name, url)
    print(json.dumps(plan, indent=2))
