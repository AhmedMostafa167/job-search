"""Akvelon — Middle AI / ML Engineer (remote: Georgia/Armenia/Egypt/Ukraine), PeopleForce job 248126, seen 2026-11-02
via freehire. Akvelon: 20+ years, 1,200+ engineers, remote-first; US stakeholders, available until 10 AM Pacific.
Asks: LLM and RAG solutions, agent workflows with orchestration and function calling, MCP integrations; agent
harnesses, sub-agents, state, tools, failure recovery; Codex/Claude Code/Cursor in real work incl. configuring
instructions, tools and quality controls; Python or TS/JS, Git, CI/CD; back end, APIs, databases; architecture;
one cloud platform (Azure/AWS/GCP); external API integration; unit/integration/e2e tests; evals, tracing and feedback
loops; agent governance (permissions, autonomy limits, human-in-the-loop, audit). Nice: presales, workshops, training.
Claude Code configuration is real: this repo's CLAUDE.md instructions and the SessionStart hook in
.claude/settings.json. Not claimed: MCP, cloud platforms (only Hugging Face Spaces), TypeScript/JavaScript, presales,
human-in-the-loop queues.
"""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _GENERAL_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Akvelon"

TITLE = "AI Engineer — Agentic AI, LLM & RAG Applications, and Coding-Agent Workflows (Python · Claude Code)"

SUMMARY = (
    "AI engineer who builds agentic LLM applications in Python and runs real development work through coding "
    "agents. Built a LangGraph agent with tool calling, hybrid RAG and long-term memory behind a FastAPI REST API "
    "on PostgreSQL, with guardrails, bounded retries, 104 automated tests, GitHub Actions CI, Langfuse tracing and a "
    "code-graded evaluation suite (12 tasks × 3 runs) that drives every change: a revised prompt raised task "
    "success from 7 to 12 of 12 with 29% fewer paid rerank calls. Designs agents and builds them with Claude Code, "
    "configured through written project instructions, setup hooks and tests. Teaches Computer Science and a starter "
    "MLOps course to about 500 students, and mentors learners in the MLOps MENA community."
)

SKILLS = [
    ("Agentic AI & LLM Apps", "LangGraph and LangChain agent workflows, orchestration, tool and function calling, "
     "agent state and memory, structured output (Pydantic), bounded retries and self-correction, guardrails; RAG "
     "with hybrid search (PostgreSQL full-text + pgvector), reranking, Chroma; LLM APIs (Anthropic, OpenAI, Groq, "
     "Cohere, Hugging Face)"),
    ("Coding Agents", "Claude Code in day-to-day development: project instruction files, session setup hooks, "
     "implementation from a written design, reviewing agent-written code against tests, Git and GitHub"),
    ("Evals, Testing & Tracing", "code-graded agent evaluation, labelled test sets with 95% confidence intervals, "
     "LLM-as-a-judge, RAGAS, pytest unit and integration tests, Langfuse tracing and prompt versioning, MLflow, "
     "Prometheus, Grafana"),
    ("Back End & Delivery", "Python, FastAPI (REST APIs, JSON), SQL, PostgreSQL, SQLAlchemy, Alembic, Docker, "
     "Docker Compose, GitHub Actions (CI), Nginx, Gradio, Hugging Face Spaces; PyTorch, Hugging Face Transformers"),
]

_shop, _research, _visioneer = copy.deepcopy(_GENERAL_PROJECTS)
_shop["tagline"] = "Agentic LLM service: tools, memory, guardrails, evals and tracing"
_research["bullets"][0] = (
    "Designed a self-correcting research agent over arXiv and the web (query rewriting, hybrid retrieval, relevance "
    "grading, cited answers, a reflection step with a bounded retry) and built it with Claude Code; structured "
    "outputs for each decision."
)
_visioneer["bullets"] = [
    "With a colleague, fine-tuned Stable Diffusion v1.5 with LoRA (PyTorch, Hugging Face Diffusers) on ~12k "
    "captioned floor-plan images to generate furnished 2D layouts from text prompts; a teammate trained the "
    "companion schematic model, and both were served to an Android AR app. Published in Machine Graphics & "
    "Vision (2025).",
]
PROJECTS = [_shop, _research, _visioneer]
