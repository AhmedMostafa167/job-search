"""Deeplight AI — Applied AI Engineer, Agentic Systems. Dubai, full-time, individual visa sponsorship. LinkedIn job
4480956223, posted 2026-10-19, seen 2026-10-24. UAE AI and data consultancy for enterprise and financial-services
clients (deeplight.ai, registered 2021).
Asks: agents, multi-agent frameworks, tool calling and state management you built yourself; Python with pytest, code
review and Git; commercial and open-weight LLM APIs, prompt design, structured-output validation, handling model and
tool failures; evaluation on representative task sets, failure-mode analysis, regression testing, tracing; trade-offs
between quality, reliability, latency and cost. Edge: LangGraph, MCP, Docker, AWS/Azure, banking clients.
No MCP, AWS/Azure or banking claimed. The interview walks through a system you built: lead with the Shopping
Assistant agent and its evaluation.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS
from cv_content import SKILLS as _BASE_SKILLS

FILE_STEM = "Ahmed_Dorra_CV_Deeplight"

TITLE = "Applied AI Engineer — Agentic Systems (LangGraph · Tool Calling · Evaluation)"

SUMMARY = (
    "AI engineer building LLM agents end to end in Python: LangGraph agents with tool calling, conversation state "
    "and long-term memory in PostgreSQL, structured outputs validated with Pydantic, and the code-graded evaluation, "
    "tracing and guardrails that show whether each change works. On a 12,730-product shopping assistant, a revised "
    "prompt raised agent task success from 7 to 12 of 12 tasks with 29% fewer paid rerank calls, and moving price "
    "limits inside search lifted on-target results from 70% to 100%. Published researcher and Computer Science "
    "teaching assistant, used to explaining technical decisions to mixed audiences."
)

SKILLS = [
    ("Agents & LLM Systems", "LangGraph (stateful agents, Postgres checkpointer), LangChain, tool calling, "
     "multi-step workflows with conditional routing and bounded retries, conversational and long-term memory, "
     "structured output (Pydantic), prompt engineering and versioning, RAG with hybrid search (PostgreSQL full-text "
     "+ pgvector, Reciprocal Rank Fusion), cross-encoder reranking; Groq, Cohere, Anthropic, OpenAI and Hugging Face "
     "models"),
    ("Evaluation & Observability", "code-graded agent evaluation (task sets × repeated runs), comparing prompt "
     "versions on the same tasks, labelled retrieval test sets with 95% confidence intervals, LLM-as-a-judge, RAGAS, "
     "guardrails, Langfuse (tracing, prompt management, experiments), MLflow, Prometheus, Grafana"),
    ("Engineering", "Python, pytest, GitHub Actions (CI), Git, FastAPI, SQL, PostgreSQL, SQLAlchemy, Alembic, "
     "Docker, Docker Compose, Nginx, Gradio, Hugging Face Spaces"),
    _BASE_SKILLS[3],
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "Tool-using LLM agent with memory, evaluated task by task"
PROJECTS[0]["bullets"] = [
    "Built a LangGraph agent that answers shoppers by calling a hybrid retrieval pipeline over 12,730 products "
    "(PostgreSQL full-text + pgvector HNSW, Reciprocal Rank Fusion, Cohere reranking); conversation state lives in a "
    "LangGraph Postgres checkpointer and each customer's lasting preferences are stored as typed facts in PostgreSQL.",
    "Designed a code-graded agent evaluation (12 tasks × 3 runs, logged to Langfuse and MLflow): prompt v2 passed 12 "
    "of 12 tasks vs 7 with 29% fewer paid rerank calls; v3 moved price and rating limits inside the search call, "
    "lifting matching results from 70% to 100% (57/81 → 48/48) with 15% fewer paid searches.",
    "Measured retrieval stage by stage on 127 labelled queries with 95% confidence intervals: hybrid top-10 recall "
    "72% vs 56% keyword and 41% vector; reranking lifted right-product-first from 23% to 43% (40-query subset); an "
    "HNSW index cut median vector search from 35 ms to 3.1 ms.",
    "Added input and memory-write guardrails (0 of 21 legitimate facts refused; a prices-grounded check passed in "
    "25 of 25 applicable runs), Langfuse tracing and prompt versioning, Prometheus/Grafana monitoring, 104 "
    "automated tests and GitHub Actions CI.",
]

COVER_LETTER = {
    "date": "24 October 2026",
    "to": ["Hiring Team, Deeplight AI", "Applied AI Engineer – Agentic Systems, Dubai"],
    "greeting": "Dear Deeplight Hiring Team,",
    "paragraphs": [
        "I'm applying for the Applied AI Engineer – Agentic Systems role in Dubai. Your posting asks candidates to "
        "walk through a system they built, and to explain the implementation choices, the evaluation and the "
        "limits. That is how I already work, so here is the short version.",
        "My main project is a Shopping Assistant: a LangGraph agent that serves a 12,730-product catalogue by "
        "calling a hybrid retrieval pipeline (PostgreSQL full-text search plus pgvector, fused and then reranked). "
        "Conversation state sits in a LangGraph Postgres checkpointer, and each customer's lasting preferences are "
        "stored as typed facts in PostgreSQL, with guardrails on what the agent may write to memory.",
        "I judged every change by measurement. I built a code-graded evaluation of 12 tasks, each run 3 times and "
        "logged to Langfuse and MLflow. A revised prompt took the agent from 7 to 12 of 12 tasks while making 29% "
        "fewer paid rerank calls. When about 30% of results still broke the customer's price or rating limits, I moved "
        "those limits inside the search call, and matching results rose from 70% to 100%. On the "
        "retrieval side, an HNSW index cut median vector-search latency from 35 ms to 3.1 ms. Quality, cost and "
        "latency were each measured, so the trade-offs were explicit.",
        "This work was done on my own projects rather than for clients, and I haven't yet used MCP or deployed on "
        "AWS or Azure; I'd expect to learn those quickly. As a Computer Science teaching assistant I led 50 lab "
        "sessions for more than 600 students, which is good practice for explaining the why behind a design. I'm "
        "based in Egypt and ready to relocate to Dubai.",
    ],
    "closing": "Sincerely,",
}
