"""Unifonic — Tech Internship Program, Cairo 2026 (fresh graduates; software, data, AI/ML, QA, DevOps), on-site.
unifonic.com/en/careers/tech-internship-program-cairo-2026, HubSpot form on the page. Seen 2026-10-18.
Saudi-founded (2006) AI-native customer-experience platform; Agentic Studio = goal-driven AI agents over WhatsApp,
SMS, voice. Cairo office: Cairo Festival City, New Cairo. Lead with the customer-facing conversational agent,
its memory, guardrails, feedback and evaluation; mention native Arabic (MENA/GCC). No speech/voice claims.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Unifonic"

TITLE = "AI Engineer — Conversational AI Agents (LLMs · RAG · Evaluation)"

SUMMARY = (
    "AI engineer building customer-facing conversational agents end to end: tool-using LangGraph agents that "
    "remember each customer across conversations, retrieval over a real catalogue, and the guardrails, evaluation, "
    "tracing and monitoring that show whether each change helps. On a 12,730-product shopping assistant, raised "
    "agent task success from 7 to 12 of 12 tasks and right-product-ranked-first from 23% to 43%. Native Arabic "
    "speaker; published researcher and Computer Science teaching assistant."
)

SKILLS = [
    ("Conversational AI & Agents", "LangGraph, LangChain, agents and tool calling, multi-turn conversation state "
     "(Postgres checkpointer), long-term customer memory, prompt engineering and versioning, structured output "
     "(Pydantic), guardrails, retrieval-augmented generation (RAG), hybrid search, reranking, Groq, Cohere, Chroma"),
    ("Evaluation & Observability", "code-graded agent evaluation, LLM-as-a-judge, RAGAS, Langfuse (tracing, "
     "prompt management, user-feedback scores), MLflow, DVC, Prometheus, Grafana"),
    ("Backend & DevOps", "Python, FastAPI (REST APIs), SQL, PostgreSQL, SQLAlchemy, Alembic, Docker, Docker Compose, "
     "GitHub Actions (CI), pytest, Nginx, Gradio, Hugging Face Spaces"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA, scikit-learn, XGBoost, pandas, NumPy, "
     "spaCy, NLTK"),
]

_shop, _research, _visioneer = copy.deepcopy(_BASE_PROJECTS)
_shop["tagline"] = "Customer-facing conversational agent with long-term memory"
_shop["bullets"] = [
    "Built a LangGraph agent, served through a FastAPI API, that holds multi-turn shopping conversations over a "
    "12,730-product catalogue (hybrid search + Cohere reranking) and remembers each customer's lasting preferences "
    "across conversations as typed facts in PostgreSQL, separating them from one-off requests.",
    "Designed a code-graded agent evaluation (12 tasks × 3 runs, logged to Langfuse and MLflow): prompt v2 passed "
    "12 of 12 tasks vs 7 with 29% fewer paid searches; v3 moved price and rating limits inside search, lifting "
    "on-target results from 70% to 100%.",
    "Added input and memory-write guardrails tested with hostile tasks (0 of 21 legitimate facts refused) and a "
    "check that every price in a reply comes from search results (25 of 25 applicable runs).",
    "Traced conversations in Langfuse with customer feedback recorded as a score on the trace; monitored with "
    "Prometheus/Grafana; 104 pytest tests and GitHub Actions CI; reranking lifted right-product-first from 23% to 43%.",
]
PROJECTS = [_shop, _research, _visioneer]
