"""Arabic.AI (Tarjama&) — AI Engineer, remote Egypt. Posted 2026-10-15.

Same facts as the base CV; wording and order mirror the posting: agentic workflows, tool calling,
short-term + long-term memory, embeddings/rerankers, evaluation of accuracy/latency/cost,
experiments, failure modes, observability, documentation. Memory is NOT vector-based — don't claim it.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_ArabicAI"

TITLE = "AI Engineer — Agentic LLM Systems (Agents · RAG · Evaluation)"

SUMMARY = (
    "AI engineer building agentic LLM systems end to end: tool-using agents with short- and long-term memory, "
    "RAG with embeddings and rerankers, and the evaluation, observability and guardrails that show whether each "
    "change works. On a 12,730-product shopping assistant, raised right-product-ranked-first from 23% to 43%, "
    "agent task success from 7 to 12 of 12 tasks with 29% fewer paid rerank calls, and cut vector-search latency "
    "from 35 ms to 3.1 ms. Native Arabic speaker; published researcher in generative vision (LoRA fine-tuning of "
    "Stable Diffusion) and quantum machine learning."
)

SKILLS = [
    ("Agents & LLM Systems", "LangGraph, LangChain, agentic workflows, tool calling, short-term and long-term "
     "memory, structured prompting, structured output (Pydantic), prompt engineering and versioning, Groq, Cohere"),
    ("RAG & Retrieval", "embeddings, rerankers (Cohere, cross-encoder), hybrid search (PostgreSQL full-text + "
     "pgvector HNSW, Reciprocal Rank Fusion), BM25, Chroma"),
    ("Evaluation & Observability", "Langfuse (tracing, experiments), MLflow, DVC, LLM-as-a-judge, code-graded "
     "agent evaluation, offline A/B comparison of prompt versions, accuracy/latency/cost benchmarking, "
     "failure-mode analysis, guardrails, Prometheus, Grafana, RAGAS"),
    ("Backend & Deployment", "Python, SQL, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, Docker Compose, "
     "GitHub Actions (CI), pytest, Nginx, Gradio, Hugging Face Spaces"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers (text-to-image), LoRA, scikit-learn, "
     "XGBoost, pandas, NumPy, spaCy, NLTK"),
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "Tool-using shopping agent with short- and long-term memory"
PROJECTS[0]["bullets"] = [
    "Built a LangGraph tool-calling agent over a 12,730-product catalogue: hybrid retrieval (PostgreSQL full-text "
    "+ pgvector HNSW embeddings, Reciprocal Rank Fusion) with Cohere reranking; short-term conversation state in a "
    "Postgres checkpointer and long-term customer preferences as typed facts the agent reads and writes via tools.",
    "Measured retrieval stage by stage on 127 labelled queries with 95% confidence intervals: hybrid top-10 recall "
    "72% vs 56% keyword and 41% vector; reranking lifted right-product-first from 23% to 43% (40-query subset); "
    "an HNSW index cut median vector-search latency from 35 ms to 3.1 ms.",
    "Designed a code-graded agent evaluation (12 tasks × 3 runs) and tested each prompt version as a candidate in "
    "Langfuse before promotion: v2 fixed two failure modes and passed 12 of 12 tasks vs 7 with 29% fewer paid "
    "rerank calls; v3 moved price and rating limits inside search, lifting matching results from 70% to 100%.",
    "Added input and memory-write guardrails (0 of 21 legitimate facts refused), Langfuse tracing and prompt "
    "versioning, Prometheus/Grafana monitoring, 104 automated tests, GitHub Actions CI, and documentation of the "
    "pipeline, agent workflow and evaluation process.",
]
PROJECTS[2]["tagline"] = "Text-to-image floor-plan generation with AR visualisation (2024)"
