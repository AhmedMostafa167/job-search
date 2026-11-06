"""General CV for referrals: a friend forwards it to roles we haven't seen (AI, ML, LLM/GenAI, Python backend).
Broader than the base CV: LLM applications, ML/DL and backend each get a skills line; the Shopping Assistant
leads with the FastAPI service so it reads well for both AI and backend readers.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV"

TITLE = "AI Engineer — LLM Applications, Machine Learning & Python Backends"

SUMMARY = (
    "AI engineer who builds AI products end to end in Python: LLM applications (RAG, agents and their evaluation), "
    "model fine-tuning with PyTorch and Hugging Face, and the FastAPI services, tests and monitoring that run them. "
    "On a 12,730-product shopping assistant, raised right-product-ranked-first from 23% to 43% and agent task "
    "success from 7 to 12 of 12 tasks. Published researcher (LoRA fine-tuning of Stable Diffusion; quantum machine "
    "learning), Computer Science teaching assistant, and native Arabic speaker with professional English."
)

SKILLS = [
    ("LLM Applications", "LangGraph, LangChain, retrieval-augmented generation (RAG), hybrid search (PostgreSQL "
     "full-text + pgvector), cross-encoder reranking, agents and tool calling, conversational memory, prompt "
     "engineering, structured output (Pydantic), guardrails, Groq, Cohere, Chroma"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA fine-tuning, scikit-learn, XGBoost, "
     "pandas, NumPy, spaCy, NLTK"),
    ("Evaluation & MLOps", "labelled test sets with confidence intervals, code-graded evaluation, LLM-as-a-judge, "
     "RAGAS, Langfuse (tracing, prompt management), MLflow, DVC, Prometheus, Grafana"),
    ("Backend & Deployment", "Python, FastAPI (REST APIs), SQL, PostgreSQL, SQLAlchemy, Alembic, Git, Docker, "
     "Docker Compose, GitHub Actions (CI), pytest, Nginx, Gradio, Hugging Face Spaces"),
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "LLM agent and RAG service behind a FastAPI API"
PROJECTS[0]["bullets"][0] = (
    "Built a LangGraph agent, served through a FastAPI REST API on PostgreSQL, that searches a 12,730-product "
    "catalogue with hybrid retrieval (PostgreSQL full-text + pgvector HNSW, Reciprocal Rank Fusion, Cohere "
    "reranking) and remembers each customer's lasting preferences across conversations."
)
