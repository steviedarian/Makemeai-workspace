# Data Access Reference

> DataOS — MakeMeAI Consulting Ltd
> Database: `data/data.db` (SQLite)
> Load this file when you need to query business data or understand the database structure.

---

## How to Query the Database

```python
import sqlite3
conn = sqlite3.connect("data/data.db")
conn.row_factory = sqlite3.Row
rows = conn.execute("SELECT * FROM youtube_daily ORDER BY date DESC LIMIT 7").fetchall()
for row in rows:
    print(dict(row))
conn.close()
```

Run live queries using: `py -3 -c "import sqlite3; ..."` from the workspace root.
Or run the collection script: `py -3 scripts/collect.py`

---

## Connected Data Sources

| Source | Table(s) | Collection Script | What It Tracks |
|--------|----------|-------------------|----------------|
| YouTube Data API | `youtube_daily`, `youtube_videos` | `scripts/collect_youtube.py` | MakeMeAI channel subscribers, views, video performance |
| FX Rates (ECB) | `fx_rates` | `scripts/collect_fx_rates.py` | USD to GBP and other currencies, daily |

---

## Table Schemas

### youtube_daily
Daily snapshot of the MakeMeAI YouTube channel.

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | Snapshot date (YYYY-MM-DD), primary key |
| subscribers | INTEGER | Total subscriber count at time of collection |
| total_views | INTEGER | Cumulative total views on the channel |
| total_videos | INTEGER | Total number of videos published |
| views_30d | INTEGER | Sum of views on videos published in last 30 days |
| videos_published_30d | INTEGER | Number of videos published in last 30 days |
| collected_at | TEXT | UTC timestamp of collection |

### youtube_videos
Individual video records, refreshed daily for videos published in last 30 days.

| Column | Type | Description |
|--------|------|-------------|
| video_id | TEXT | YouTube video ID, primary key |
| title | TEXT | Video title |
| published_date | TEXT | Date video was published (YYYY-MM-DD) |
| views | INTEGER | Total views at last collection |
| likes | INTEGER | Total likes at last collection |
| comments | INTEGER | Total comments at last collection |
| duration | TEXT | ISO 8601 duration (e.g. PT5M30S) |
| last_updated | TEXT | Date of last collection update |

### fx_rates
Daily exchange rates from the European Central Bank via Frankfurter API.

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | Rate date (YYYY-MM-DD) |
| currency | TEXT | Target currency code (GBP, EUR, etc.) |
| rate | REAL | Exchange rate from USD |
| base | TEXT | Base currency (always USD) |
| collected_at | TEXT | UTC timestamp of collection |

### leads
Prospect records from the outreach and demo system.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Auto-incremented ID |
| name | TEXT | Contact name |
| email | TEXT | Email address |
| company_name | TEXT | Business name |
| company_url | TEXT | Website URL |
| industry | TEXT | Business sector |
| source | TEXT | How lead was sourced |
| raw_score | INTEGER | AI readiness score from scanner |
| bant_total | INTEGER | BANT qualification score |
| lead_status | TEXT | Current status in pipeline |
| priority_tier | TEXT | A/B/C tier classification |
| notes | TEXT | Free-text notes |
| created_at | TEXT | When lead was added |

### collection_log
Audit trail of every collection run.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Auto-incremented ID |
| collected_at | TEXT | UTC timestamp |
| source | TEXT | Collector name (youtube, fx_rates, etc.) |
| status | TEXT | success, skipped, error, or exception |
| reason | TEXT | Error message or skip reason |
| records_written | INTEGER | How many rows were written |

---

## Common Queries

### Latest YouTube snapshot
```sql
SELECT date, subscribers, total_views, total_videos
FROM youtube_daily
ORDER BY date DESC
LIMIT 1;
```

### Subscriber growth over last 30 days
```sql
SELECT date, subscribers,
       subscribers - LAG(subscribers) OVER (ORDER BY date) as daily_change
FROM youtube_daily
ORDER BY date DESC
LIMIT 30;
```

### Month-over-month subscriber comparison
```sql
SELECT
    strftime('%Y-%m', date) as month,
    MAX(subscribers) as end_subs,
    MIN(subscribers) as start_subs,
    MAX(subscribers) - MIN(subscribers) as growth
FROM youtube_daily
GROUP BY month
ORDER BY month DESC;
```

### Top performing videos
```sql
SELECT title, views, likes, comments, published_date
FROM youtube_videos
ORDER BY views DESC
LIMIT 10;
```

### Current GBP/USD rate
```sql
SELECT rate, date FROM fx_rates
WHERE currency = 'GBP'
ORDER BY date DESC
LIMIT 1;
```

### Collection health (last 7 days)
```sql
SELECT source, status, records_written, collected_at
FROM collection_log
ORDER BY collected_at DESC
LIMIT 20;
```

### Pipeline leads by status
```sql
SELECT lead_status, COUNT(*) as count
FROM leads
GROUP BY lead_status
ORDER BY count DESC;
```

---

## Data Collection

Run all collectors manually:
```bash
py -3 scripts/collect.py
```

Run a specific collector:
```bash
py -3 scripts/collect.py --sources youtube
py -3 scripts/collect.py --sources fx_rates
```

Regenerate key-metrics.md without collecting:
```bash
py -3 scripts/generate_metrics.py
```

Collection logs are written to `collection_log` table in the database.

---

## Adding New Data Sources

Create a new `scripts/collect_SOURCENAME.py` following the pattern in `scripts/examples/`.
The orchestrator (`scripts/collect.py`) auto-discovers any `collect_*.py` file in the scripts directory.

Priority sources to add when ready:
- **Stripe** -- add when MakeMeAI starts billing clients (`scripts/examples/stripe.py` is ready)
- **Piano channel YouTube** -- add `YOUTUBE_CHANNEL_ID_PIANO` to .env and create a second collector
- **Google Analytics** -- add when GA4 is set up on makemeai.tech
