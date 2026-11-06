"""General CV: Python backend developer with AI features."""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _G

FILE_STEM = "Ahmed_Dorra_CV_General_Python_Backend"
TITLE = "Python Backend Engineer — FastAPI, PostgreSQL, Docker & AI Services"
SUMMARY = (
    "Python backend engineer who ships AI-powered services: FastAPI REST APIs on PostgreSQL (SQLAlchemy, Alembic "
    "migrations), data ingestion and validation with Pydantic, Docker Compose deployments, GitHub Actions CI with "
    "104 automated tests, and Prometheus/Grafana monitoring. Added LLM features (RAG, tool-using agents) behind "
    "those services and measured their latency, cost and accuracy. Teaches Operating Systems to 700+ students. "
    "Native Arabic speaker; open to relocation and remote work."
)
SKILLS = [
    ("Backend", "Python, FastAPI (REST APIs), SQL, PostgreSQL, SQLAlchemy, Alembic, Pydantic, pytest, Git"),
    ("Deployment & Monitoring", "Docker, Docker Compose, GitHub Actions (CI), Nginx, Prometheus, Grafana, "
     "Hugging Face Spaces, Langfuse tracing"),
    ("AI Features", "LangGraph, LangChain, RAG, hybrid search (PostgreSQL full-text + pgvector), agents and tool "
     "calling, structured output, guardrails, MLflow, DVC"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, scikit-learn, pandas, NumPy"),
]
PROJECTS = copy.deepcopy(_G)
