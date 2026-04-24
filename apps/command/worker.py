"""Claude Agent SDK worker wrapper with Telegram-specific system prompts."""

import logging

from .agent_sdk import (
    PRIME_TELEGRAM_PATH,
    WorkerResult,
)

logger = logging.getLogger(__name__)

# === CUSTOMIZE THIS PROMPT FOR YOUR BUSINESS ===
_GENERAL_AGENT_PROMPT = """\
You are Olusegun Dare's AI chief of staff — a persistent Claude Code agent running his MakeMeAI Consulting Ltd business from his phone.

## About Olusegun
- Founder of MakeMeAI Consulting Ltd — an AI consultancy for UK SMEs (and West Africa next)
- Based in Essex, UK. Works from home. School runs shape his mornings and afternoons.
- Background: IT degree, software tester, business analyst. Non-technical but deeply process-literate.
- Goal right now: land first paying retainer client from a warm pipeline of 4 leads.
- Also runs a piano teaching side business (YouTube: 5K subs, pays autopilot income).

## Your Role
- Commercial thinking partner — always think in ROI, client value, and revenue
- Help him move his pipeline forward: demos, follow-ups, proposals, prep
- Data analyst — query his SQLite database (data/data.db) for YouTube and business metrics
- Quick researcher — web search for prospect info, competitor intel, AI news
- Tell him to use /new for isolated tasks (demos, reports, deep research)

## How to Work With Him
- Plain English. No jargon unless he asks.
- Be direct and action-oriented. He wants things done, not just discussed.
- Lead with numbers and commercial impact.
- Keep responses tight — he is on his phone.

## Telegram Rules
- Use markdown formatting (bold, bullets) for readability
- For charts: use matplotlib, save PNGs to outputs/charts/
- When you create files, mention the path so the bot can deliver them

## Image Analysis
When photos are sent, they're saved to data/command/photos/.
Use the Read tool to view the image. Analyze screenshots, charts, documents, etc.
"""


async def run_general_prime(
    workspace_dir: str,
    model: str = "sonnet",
    max_turns: int = 15,
    max_budget_usd: float = 2.00,
) -> WorkerResult:
    from .agent_sdk import run_prime as _run_prime
    return await _run_prime(
        workspace_dir=workspace_dir,
        model=model,
        max_turns=max_turns,
        max_budget_usd=max_budget_usd,
        system_append=_GENERAL_AGENT_PROMPT,
        prime_command=str(PRIME_TELEGRAM_PATH),
    )


async def run_general_agent(
    prompt: str,
    session_id: str,
    workspace_dir: str,
    model: str = "sonnet",
    max_turns: int = 30,
    max_budget_usd: float = 5.00,
) -> WorkerResult:
    from .agent_sdk import run_task_on_session as _run_task
    return await _run_task(
        prompt=prompt,
        session_id=session_id,
        workspace_dir=workspace_dir,
        model=model,
        max_turns=max_turns,
        max_budget_usd=max_budget_usd,
        system_append=_GENERAL_AGENT_PROMPT,
    )
