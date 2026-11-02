"""Valeo Egypt — Graduate In Training Program (GIT), AI Engineer, Cairo, on-site. Workday REQ2026081151,
posted 2026-09-15. Seen 2026-10-17. Asks: Python, REST APIs, FastAPI/Flask/Django, pytest, unit + API tests,
UI for AI models, docs, deployment; PyTorch + LangChain/LlamaIndex interest; GCP/AWS a plus.
Wants 2025/2026 graduates (he's 06/2024, military service 01/2025-01/2026). No HTML/CSS/JS/TS or cloud claimed.
Lead with Python APIs, testing, the Gradio storefront UI, docs and the HNSW latency fix.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Valeo"

TITLE = "AI Engineer — Python, APIs & Generative AI"

SUMMARY = (
    "Computer Science graduate building AI applications in Python end to end: FastAPI REST APIs, LangChain and "
    "LangGraph components, user-facing UIs that call the models, and the tests, documentation and monitoring that "
    "keep them running. On a 12,730-product shopping assistant, covered the service with 104 pytest tests and CI, "
    "found and fixed a search bottleneck (35 ms to 3.1 ms median), and raised agent task success from 7 to 12 of "
    "12 tasks. With a colleague, fine-tuned Stable Diffusion with LoRA in PyTorch (published 2025); Computer Science teaching assistant."
)

SKILLS = [
    ("Backend & APIs", "Python, FastAPI (REST APIs), Pydantic, SQL, PostgreSQL, SQLAlchemy, Alembic, httpx, Git"),
    ("Testing & Quality", "pytest (unit and API route tests), GitHub Actions (CI), code-graded evaluation, "
     "Langfuse tracing, Prometheus, Grafana"),
    ("Generative AI", "LangChain, LangGraph, retrieval-augmented generation (RAG), hybrid search (pgvector), "
     "cross-encoder reranking, agents and tool calling, prompt engineering, structured output, Chroma, Groq, "
     "Cohere, RAGAS"),
    ("Deep Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA fine-tuning, scikit-learn, pandas, NumPy"),
    ("Deployment & UI", "Docker, Docker Compose, Nginx, Hugging Face Spaces, Gradio (web UIs for AI models), "
     "MLflow, DVC"),
]

_shop, _research, _visioneer = copy.deepcopy(_BASE_PROJECTS)
_shop["tagline"] = "AI service with a FastAPI API, a storefront UI, tests and CI"
_shop["stack"] = ("Python · FastAPI · LangGraph · LangChain · PostgreSQL · pgvector · pytest · GitHub Actions · "
                  "Gradio · Docker · Prometheus · Grafana")
_shop["bullets"] = [
    "Built a LangGraph agent served through a FastAPI REST API on PostgreSQL that searches a 12,730-product "
    "catalogue with hybrid retrieval (full-text + pgvector, Cohere reranking) and remembers each customer's lasting "
    "preferences across conversations.",
    "Built the user-facing demo: a Gradio storefront that calls the API over HTTP and shows the recommended "
    "products as cards next to the chat.",
    "Wrote 104 pytest tests (retrieval, guardrails, prompts and the chat and feedback API routes, including their "
    "error responses) run by GitHub Actions CI; profiled vector search and added an HNSW index, cutting median "
    "latency from 35 ms to 3.1 ms.",
    "Measured each change before keeping it: hybrid top-10 recall 72% vs 56% keyword (127 labelled queries); "
    "a revised agent prompt passed 12 of 12 tasks vs 7. Deployed with Docker Compose and Prometheus/Grafana "
    "monitoring, and documented the architecture, API, evaluation and setup.",
]
_research["bullets"] = [
    "Designed a self-correcting LangGraph workflow: query rewriting, hybrid retrieval (Chroma + BM25), relevance "
    "grading, cited generation and a reflection step with a bounded retry, using structured outputs for each decision.",
    "Served through a FastAPI API and a Gradio UI and deployed live on Hugging Face Spaces; a provider factory "
    "switches between Groq, Hugging Face, Anthropic and OpenAI with one setting.",
]
PROJECTS = [_shop, _research, _visioneer]
