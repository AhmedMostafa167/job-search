"""Pass Technology — AI Engineer, LLM & AI Agents, for Sanad (AI personal-assistant platform). Cairo, remote.
Wuzzuf posting (listed as "tech technology"), posted 2026-10-05, seen 2026-10-24. No company website found
(passtechnology.com is a parked domain for sale).
Asks: Python, LLMs and AI agents, OpenAI or other LLM APIs, RAG with embeddings and vector databases, LangChain or
LangGraph, production APIs with FastAPI, tool calling and structured outputs; builds conversational memory and
user-context systems, guardrails and AI evaluation. Plus: Qdrant, PostgreSQL, LangMem, OpenRouter, AWS, SSE/WebSockets.
Close match to the Shopping Assistant's memory design. No Qdrant, LangMem, OpenRouter, AWS or SSE claimed.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS
from cv_content import SKILLS as _BASE_SKILLS

FILE_STEM = "Ahmed_Dorra_CV_PassTechnology"

TITLE = "AI Engineer — LLM Agents, RAG & Conversational Memory"

SUMMARY = (
    "AI engineer building LLM assistants end to end in Python: LangGraph agents with tool calling and structured "
    "outputs, RAG with hybrid search over PostgreSQL and pgvector, conversational memory and per-user context, "
    "FastAPI services, and the guardrails and evaluation that keep answers reliable. On a 12,730-product shopping "
    "assistant, raised agent task success from 7 to 12 of 12 tasks and right-product-ranked-first from 23% to 43%; "
    "its memory keeps each customer's lasting preferences as typed facts in PostgreSQL, next to a LangGraph Postgres "
    "checkpointer for conversation state. Native Arabic speaker; Computer Science teaching assistant."
)

SKILLS = [
    ("LLM Agents & Memory", "LangGraph, LangChain, agents and tool calling, multi-step workflows, structured output "
     "(Pydantic), conversation state (LangGraph Postgres checkpointer), long-term user facts in PostgreSQL, prompt "
     "engineering and versioning, input and memory-write guardrails"),
    ("RAG & Search", "retrieval-augmented generation, embeddings, hybrid search (PostgreSQL full-text + pgvector "
     "HNSW, Reciprocal Rank Fusion), BM25, cross-encoder reranking, Chroma; Groq, Cohere, Anthropic and OpenAI APIs"),
    ("Evaluation & LLMOps", "code-graded agent evaluation, labelled retrieval test sets with 95% confidence "
     "intervals, LLM-as-a-judge, RAGAS, Langfuse (tracing, prompt management, experiments), MLflow, DVC"),
    ("Backend & Deployment", "Python, FastAPI, SQL, PostgreSQL, SQLAlchemy, Alembic, Docker, Docker Compose, "
     "GitHub Actions (CI), pytest, Prometheus, Grafana, Nginx, Gradio, Hugging Face Spaces"),
    _BASE_SKILLS[3],
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "LLM assistant with long-term memory, behind a FastAPI API"
PROJECTS[0]["bullets"] = [
    "Built a LangGraph agent, served through FastAPI, that searches a 12,730-product catalogue with tool calls to "
    "hybrid retrieval (PostgreSQL full-text + pgvector HNSW, Reciprocal Rank Fusion, Cohere reranking).",
    "Designed its memory: a LangGraph Postgres checkpointer for conversation state, plus each customer's lasting "
    "preferences stored as typed facts in PostgreSQL (capped at 50 per user) and recalled in later conversations, "
    "with guardrails on memory writes that refused 0 of 21 legitimate facts.",
    "Designed a code-graded agent evaluation (12 tasks × 3 runs, logged to Langfuse and MLflow): prompt v2 passed "
    "12 of 12 tasks vs 7 with 29% fewer paid rerank calls; moving price limits inside search lifted on-target "
    "results from 70% to 100%. Retrieval: hybrid top-10 recall 72% vs 56% keyword and 41% vector (127 labelled "
    "queries).",
    "Added Langfuse tracing and prompt versioning, Prometheus/Grafana monitoring, 104 automated tests and GitHub "
    "Actions CI.",
]
