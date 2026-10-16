"""Miraal Tech (MIRAALTECH LTD, UK) — AI Engineer Intern, 6-month paid remote. Seen 2026-10-16.

Their products: AI patient chat bot, AI call agent, healthcare software for UK + GCC clinics.
Lean on conversational AI, grounding, guardrails, testing before release, native Arabic (GCC).
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Miraal"

TITLE = "AI Engineer — Conversational AI & LLM Systems (Chatbots · Agents · RAG)"

SUMMARY = (
    "AI engineer building conversational LLM applications end to end in Python: chatbots and tool-using agents "
    "with memory, RAG over domain data, and the guardrails, grounding checks and evaluation that keep answers "
    "correct before release. On a 12,730-product conversational assistant, raised agent task success from 7 to 12 "
    "of 12 tasks and right-product-ranked-first from 23% to 43%. Native Arabic speaker; published researcher "
    "(EEG signal classification for brain–computer interfaces; LoRA fine-tuning of Stable Diffusion)."
)

SKILLS = [
    ("LLMs & Conversational AI", "LangGraph, LangChain, chatbots, agents and tool calling, conversational memory, "
     "retrieval-augmented generation (RAG), prompt engineering, structured output (Pydantic), guardrails, Groq, "
     "Cohere"),
    ("NLP", "Hugging Face Transformers, embeddings, rerankers (Cohere, cross-encoder), hybrid search (PostgreSQL "
     "full-text + pgvector), spaCy, NLTK, Chroma"),
    ("Evaluation & Monitoring", "code-graded agent evaluation, LLM-as-a-judge, Langfuse (tracing, prompt "
     "management), MLflow, DVC, RAGAS, Prometheus, Grafana"),
    ("Backend & Deployment", "Python, SQL, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, Docker Compose, "
     "GitHub Actions (CI), pytest, Nginx, Gradio, Hugging Face Spaces"),
    ("Machine Learning", "PyTorch, Diffusers, LoRA, scikit-learn, XGBoost, pandas, NumPy"),
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "Conversational AI assistant with tool calling and long-term memory"
PROJECTS[0]["bullets"][3] = (
    "Added input and memory-write guardrails (0 of 21 legitimate facts refused), a code check that every price "
    "the agent states comes from a tool result (25 of 25 applicable runs), Langfuse tracing and prompt "
    "versioning, Prometheus/Grafana monitoring, 104 automated tests and GitHub Actions CI."
)
