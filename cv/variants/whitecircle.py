"""White Circle — AI Red Team Engineer. Global remote, full-time. Ashby job d2c5f461, published 2026-07-06, open on
2026-10-27. AI safety/guardrails startup (Paris/NY), investors include leaders at OpenAI, Anthropic, Hugging Face.
Asks: adversarial testing of LLM systems (chatbots, RAG, agents, tool calling); attack library with regression tests
and scoring rubrics; clear reproducible reports; background in QA automation, AppSec, pentest or bug bounty; strong
Python; API/web testing; LLM abuse vectors (prompt injection, jailbreaks, data leakage, tool misuse, excessive
agency, token-cost exhaustion). Plus: Burp, Postman, Playwright, pytest; LangChain/LangGraph; LLM-as-judge; OWASP
LLM Top 10; eval pipelines and CI-friendly tests. Gap: no security or red-team background claimed; frame as the
builder of guardrails and regression evals who now wants to break such systems. No Burp, Postman or Playwright claimed.
Built on the Plata (evaluation-first) variant.
"""
from variants.plata import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_WhiteCircle"

TITLE = "AI Red Team / Evaluation Engineer — LLM Agents, RAG & Guardrails"

SUMMARY = (
    "AI engineer who builds LLM agents and RAG pipelines and then tests where they fail: input and memory-write "
    "guardrails that treat user text as untrusted, a grounding check that the agent's prices come from retrieved "
    "data (passed in 25 of 25 applicable runs), code-graded task suites repeated across runs, LLM-as-a-judge, and "
    "pytest regression tests in CI (104 tests). On a 12,730-product assistant, found that about 30% of results broke "
    "the user's price or rating limits and fixed it at the tool level (70% to 100% on target). Writes results up as "
    "reproducible before-and-after logs. Two peer-reviewed publications; based in Egypt, remote."
)
COVER_LETTER = None
