"""Raya Holding — Junior AI Engineer (0–2 yrs), New Cairo. Email mohamed_rasheed@rayacorp.com, subject = job title.
Seen 2026-10-16. Asks: Python, APIs, LLMs, RAG, AI workflows; LangChain/LangGraph/n8n a plus.
No n8n on the CV (not used). Lead with RAG + LangGraph workflows + FastAPI APIs.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Raya"

TITLE = "AI Engineer — LLM Systems (RAG · Agents · AI Workflows)"

SUMMARY = (
    "AI engineer building LLM applications end to end in Python: RAG pipelines with hybrid search and reranking, "
    "LangGraph agents and multi-step AI workflows, served through FastAPI APIs on PostgreSQL, with the evaluation, "
    "guardrails and monitoring that show whether each change works. On a 12,730-product shopping assistant, raised "
    "right-product-ranked-first from 23% to 43% and agent task success from 7 to 12 of 12 tasks. Published "
    "researcher and Computer Science teaching assistant."
)

SKILLS = [
    ("LLMs, RAG & AI Workflows", "LangGraph, LangChain, retrieval-augmented generation (RAG), hybrid search "
     "(PostgreSQL full-text + pgvector, Reciprocal Rank Fusion), cross-encoder reranking, agents and tool calling, "
     "multi-step workflows with conditional routing, conversational memory, prompt engineering, structured output "
     "(Pydantic), Chroma, Groq, Cohere"),
    ("APIs & Backend", "Python, FastAPI (REST APIs), SQL, PostgreSQL, SQLAlchemy, Alembic, Git, Docker, "
     "Docker Compose, GitHub Actions (CI), pytest, Nginx, Gradio, Hugging Face Spaces"),
    ("Evaluation & LLMOps", "Langfuse (tracing, prompt management, experiments), MLflow, DVC, RAGAS, "
     "LLM-as-a-judge, code-graded agent evaluation, guardrails, Prometheus, Grafana"),
    ("Data & Machine Learning", "pandas, NumPy, scikit-learn, XGBoost, PyTorch, Hugging Face Transformers, "
     "Diffusers, LoRA, spaCy, NLTK"),
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "LLM agent and RAG service behind a FastAPI API"
PROJECTS[0]["bullets"][0] = (
    "Built a LangGraph agent, served through a FastAPI REST API on PostgreSQL, that searches a 12,730-product "
    "catalogue with hybrid retrieval (PostgreSQL full-text + pgvector HNSW, Reciprocal Rank Fusion, Cohere "
    "reranking) and remembers each customer's lasting preferences across conversations."
)
