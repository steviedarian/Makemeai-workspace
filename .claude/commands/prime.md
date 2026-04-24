# Prime

> Read the context files and summarize your understanding of this workspace.

## Step 1: Read Memory First (Source of Truth)

Memory files override any older context files. When there is a conflict between memory and context/task-audit/plans, **memory wins**.

Read ALL memory files in the memory directory to get the latest state of:
- Project status (outreach, pipeline, key milestones, etc.)
- User preferences and feedback
- Reference pointers

Then read:

./context
./context/group/key-metrics.md
./HISTORY.md (latest 2 entries only)
./docs/_index.md

## Step 2: Cross-Check and Reconcile

Before summarising, cross-check these common conflict points:
- **Dates:** Confirm today's date with the user if the system clock seems off. Never assume.
- **Compliance status:** Memory file is authoritative, not task-audit.md.
- **Personal context:** Check memory for any personal context that affects work schedule.
- **Coaching calls:** Check memory for cancellations or reschedules.
- **Project evolution:** Check HISTORY.md for features that evolved beyond their original plan (e.g. chatbot became AI receptionist).
- **Plans folder:** Plans show what was *planned*, not what *is*. Always verify against memory and HISTORY.md before listing as active.

## On-Demand Loading

These files are NOT read during /prime but loaded when a task requires deep detail:

- `reference/data-access.md` — Full table schemas, SQL query examples, collection scripts
- Individual docs from `docs/` — find the right one via `docs/_index.md`
- `ai-docs/README.md` — **AI Landscape Reference** — Living documentation of the best AI models across 10 categories (text, code, vision, image gen, image edit, search, video gen, image-to-video, TTS, STT). Updated daily by automated scanner. When building anything that uses AI models, or when you need to know the current best model for any category — load this first, then drill into `ai-docs/{category}/state-of-the-art.md` for full rankings, pricing, integration code, and tips.

## Step 3: Summary

After reading, provide:

1. **Date check** — State the date you believe it is and ask the user to confirm if there is any doubt
2. A brief summary of who I am, what this workspace is for and what your role is
3. Your understanding of the workspace structure and the purpose of each section/file
4. What commands are available
5. A summary of my/our current strategies and priorities — **sourced from memory files first, then strategy.md**
6. **Data status** — Review key-metrics.md data freshness. Flag anything stale (>2 days old). Note you can run live SQL queries against `data/data.db` for deeper analysis.
7. **Memory conflicts** — Flag any conflicts found between memory and older files (task-audit.md, plans/, context/) so they can be resolved
8. Confirmation you're ready to help me with pursuing these goals through use of this workspace
