"""Smarterminds — AI Engineer Intern (paid, 3–6 months, full-time offer possible), Giza office (Sheikh Zayed).
Applied through their own ATS: smarterminds.smarterats.com/careers/262, posted 2026-10-14. Seen 2026-10-17.
Belgian embedded/automotive software firm (Brugge, est. 2018); the SmarterAI team builds SmarterATS (AI hiring tool).
Asks: built one AI thing and can explain it; connect LLMs to product workflows (prompts, API calls, judging output).
Stack is JavaScript, HTML/CSS, React, SQL, REST APIs (TS/Next/Node a bonus): none of the JS side is claimed.
Lead with prompts → API → evaluation, SQL/PostgreSQL and REST APIs.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Smarterminds"

TITLE = "AI Engineer — LLM Product Features (Prompts · APIs · Evaluation)"

SUMMARY = (
    "AI engineer who builds LLM features into real products end to end: writing and versioning prompts, calling "
    "model APIs from a FastAPI REST backend on PostgreSQL, and checking with automated evaluations whether the "
    "output is actually good before it ships. On a 12,730-product shopping assistant, a revised prompt took agent "
    "task success from 7 to 12 of 12 tasks, and reranking raised right-product-ranked-first from 23% to 43%. "
    "Published researcher and Computer Science teaching assistant."
)

SKILLS = [
    ("LLM Features", "prompt engineering and versioning (Langfuse prompt management), LLM APIs (Groq, Cohere), "
     "structured output (Pydantic), agents and tool calling (LangGraph, LangChain), retrieval-augmented generation "
     "(RAG), hybrid search, reranking, conversational memory"),
    ("Output Evaluation", "code-graded evaluation, LLM-as-a-judge, RAGAS, labelled test sets with confidence "
     "intervals, guardrails, Langfuse tracing and experiments, MLflow"),
    ("APIs & Databases", "Python, FastAPI (RESTful APIs), SQL, PostgreSQL (full-text search, pgvector, indexing), "
     "SQLAlchemy, Alembic migrations, pytest, Git, GitHub Actions (CI)"),
    ("Deployment & UI", "Docker, Docker Compose, Nginx, Gradio, Hugging Face Spaces, Prometheus, Grafana"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA, scikit-learn, pandas, NumPy"),
]

_shop, _research, _visioneer = copy.deepcopy(_BASE_PROJECTS)
_shop["tagline"] = "LLM shopping assistant: prompts, API and evaluation"
_shop["bullets"] = [
    "Built an AI shopping assistant end to end: a LangGraph agent behind a FastAPI REST API on PostgreSQL that "
    "searches 12,730 products (full-text + pgvector, Cohere reranking), stores each customer's lasting preferences "
    "as typed facts, and powers a Gradio storefront demo that calls the API.",
    "Versioned the agent's prompts in Langfuse and promoted a new version only after a code-graded evaluation "
    "(12 tasks × 3 runs): v2 passed 12 of 12 tasks vs 7 with 29% fewer paid rerank calls; v3 moved price and rating "
    "limits inside search, lifting on-target results from 70% to 100% with 15% fewer paid searches.",
    "Checked whether the output could be trusted: every price in a reply had to come from search results (25 of 25 "
    "applicable runs passed), memory-write guardrails refused 0 of 21 legitimate facts, and retrieval was measured "
    "on 127 labelled queries (hybrid top-10 recall 72% vs 56% keyword).",
    "Covered the service with 104 pytest tests and GitHub Actions CI; deployed with Docker Compose and "
    "Prometheus/Grafana monitoring; an HNSW index cut median vector search from 35 ms to 3.1 ms.",
]
PROJECTS = [_shop, _research, _visioneer]
