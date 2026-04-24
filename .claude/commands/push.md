# Push

> Back up the current workspace to GitHub. Run at the end of every session to keep your work safe.

## Instructions

You are backing up the MakeMeAI workspace to GitHub. Follow these steps exactly.

### Step 1: Check what changed

Run:
```
git status --short
```

If there are no changes (clean working tree), tell the user: "Nothing new to push — your workspace is already up to date on GitHub." Stop here.

### Step 2: Stage all changes

```
git add .
```

### Step 3: Write the commit message

Look at the staged changes and write a clear one-line summary of what happened this session. Examples:
- "Add GP surgery demo report and healthcare research"
- "Install Daily Brief module, update strategy context"
- "Add 3 new Essex leads, update pipeline in current-data.md"

Keep it factual and specific. No generic messages like "update files".

### Step 4: Commit

```
git commit -m "<your message here>"
```

### Step 5: Push

```
git push origin master
```

### Step 6: Confirm

Tell the user:
- What was committed (brief summary of changes)
- The commit message used
- That the backup is live at: https://github.com/steviedarian/Makemeai-workspace

If the push fails with an authentication error, tell the user to check that GITHUB_TOKEN in their .env file is still valid (tokens can expire or be revoked). They can generate a new one at github.com/settings/tokens.

## What is NOT pushed (kept private by .gitignore)
- `.env` — API keys stay on your machine only
- `credentials/` — Google service account files
- `data/*.db` — the database (rebuilt by the pipeline)
- `data/command/` — bot session logs
- `.venv/` — Python environment (reinstallable)
