"""Masaj Co. — AI Engineer. Kuwait, full-time (LinkedIn level: mid-senior; no years stated). LinkedIn job 4479908850,
posted 2026-10-18, seen 2026-10-24. Masaj is a Kuwaiti wellness-at-home booking app (trymasaj.com, registered 2021;
careers on Zoho Recruit).
Asks: AI features on OpenAI, Claude and other LLM APIs; chatbots, agents and workflows; Python and FastAPI backend
APIs; prompt engineering, RAG and vector databases; optimising accuracy, performance and cost; Git, databases,
cloud deployment. Preferred: production AI apps. Consumer app in Kuwait, so mention native Arabic.
No cloud provider claimed beyond Docker and Hugging Face Spaces.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS
from cv_content import SKILLS as _BASE_SKILLS

FILE_STEM = "Ahmed_Dorra_CV_Masaj"

TITLE = "AI Engineer — LLM Chatbots, Agents & FastAPI Backends"

SUMMARY = (
    "AI engineer building LLM-powered features end to end: chatbots and tool-using agents on LLM APIs (Groq, "
    "Cohere, Anthropic, OpenAI), RAG with hybrid search over PostgreSQL and pgvector, and FastAPI backends with "
    "tests, CI and monitoring. Tunes for accuracy, speed and cost, not just demos: on a 12,730-product shopping "
    "assistant, a revised prompt raised agent task success from 7 to 12 of 12 tasks with 29% fewer paid rerank "
    "calls, and an HNSW index cut median vector search from 35 ms to 3.1 ms. Native Arabic speaker with "
    "professional English; open to relocating to Kuwait."
)

SKILLS = [
    ("LLM Apps & Chatbots", "LLM APIs (Groq, Cohere, Anthropic, OpenAI, Hugging Face), chatbots and agents with "
     "tool calling (LangGraph, LangChain), conversational memory, prompt engineering and versioning, structured "
     "output (Pydantic), guardrails"),
    ("RAG & Vector Search", "retrieval-augmented generation, embeddings, pgvector (HNSW), Chroma, hybrid search "
     "(PostgreSQL full-text + vectors, Reciprocal Rank Fusion), BM25, cross-encoder reranking"),
    ("Backend & Deployment", "Python, FastAPI (REST APIs), SQL, PostgreSQL, SQLAlchemy, Alembic, Git, Docker, "
     "Docker Compose, GitHub Actions (CI), pytest, Prometheus, Grafana, Nginx, Hugging Face Spaces"),
    ("Evaluation & Cost", "code-graded agent tests, labelled retrieval test sets, latency benchmarking, tracking "
     "paid API calls, Langfuse (tracing, prompt management), MLflow, RAGAS"),
    _BASE_SKILLS[3],
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "LLM chatbot with long-term memory, behind a FastAPI API"
PROJECTS[0]["bullets"][0] = (
    "Built a LangGraph chatbot agent, served through a FastAPI REST API on PostgreSQL, that searches a 12,730-product "
    "catalogue with hybrid retrieval (PostgreSQL full-text + pgvector HNSW, Reciprocal Rank Fusion, Cohere reranking) "
    "and remembers each customer's lasting preferences across conversations."
)
