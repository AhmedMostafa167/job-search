"""ActAI (BJAK's AI product company; agent-first mobile communication app) — LLM Application Engineer (Lisbon or
Zurich; LinkedIn 4452403635 / 4452404665) and Applied Machine Learning Engineer (Singapore, entry level; LinkedIn
4482697928). Seen 2026-11-02. One CV covers both.
LLM Application Engineer asks: LLM apps and agent workflows; reasoning, planning, memory, tool use, multi-step
execution; reliable orchestration; integrating LLMs with APIs, databases and search; prompting, context engineering,
structured outputs, tool calling; evaluation frameworks and datasets; optimise quality, latency and cost;
observability, tracing, experimentation. Stack: Python, LLM APIs, agent frameworks, vector databases, PyTorch/JAX.
Applied ML asks: classification, retrieval, ranking, personalisation; embeddings, hybrid search and reranking.
Not claimed: JAX, distributed systems, mobile apps, personalisation models.
"""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _GENERAL_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_ActAI"

TITLE = "LLM Application Engineer — Agent Workflows, Retrieval & Evaluation, Tuned for Quality, Latency and Cost"

SUMMARY = (
    "AI engineer who turns probabilistic LLM output into reliable, measured product behaviour. Built a LangGraph "
    "agent with tool calling, long-term memory, structured outputs and bounded retries over 12,730 products, with "
    "hybrid retrieval (PostgreSQL full-text + pgvector, Reciprocal Rank Fusion, cross-encoder reranking). Builds the "
    "evaluation sets: 127 labelled queries showed 72% top-10 recall for hybrid search vs 41% vector-only, "
    "reranking moved the right product to first place from 23% to 43%, and a 12-task agent suite (3 runs each) "
    "drove a prompt rewrite from 7 to 12 of 12 tasks with 29% fewer paid rerank calls. Cut median vector-search "
    "latency from 35 ms to 3.1 ms with an HNSW index. Langfuse tracing, 104 tests, CI; PyTorch."
)

SKILLS = [
    ("Agent Workflows", "LangGraph, LangChain, multi-step agents, tool calling, memory and state, structured output "
     "(Pydantic), context engineering, prompt engineering and versioning, bounded retries and self-correction, "
     "guardrails; LLM APIs (OpenAI-compatible, Anthropic, Groq, Cohere, Hugging Face open-weight models)"),
    ("Retrieval & Ranking", "embeddings, pgvector (HNSW), Chroma, PostgreSQL full-text and BM25, hybrid search with "
     "Reciprocal Rank Fusion, cross-encoder reranking, retrieval evaluation (recall@k, first-place rate)"),
    ("Evaluation & Observability", "evaluation datasets and code-graded task suites, labelled test sets with 95% "
     "confidence intervals, regression checks across prompt versions, LLM-as-a-judge, RAGAS, Langfuse tracing, "
     "MLflow, Prometheus, Grafana; latency and paid-call cost tracking"),
    ("Engineering & ML", "Python, FastAPI (REST APIs), SQL, PostgreSQL, Docker, GitHub Actions (CI), pytest; "
     "PyTorch, Hugging Face Transformers, scikit-learn, XGBoost, LoRA fine-tuning"),
]

_shop, _research, _visioneer = copy.deepcopy(_GENERAL_PROJECTS)
_shop["tagline"] = "LLM agent with memory, tools and hybrid retrieval, evaluated for quality, latency and cost"
_shop["bullets"][2] = (
    "Designed a code-graded agent evaluation (12 tasks × 3 runs, logged to Langfuse and MLflow): prompt v2 passed "
    "12 of 12 tasks vs 7 with 29% fewer paid rerank calls; v3 moved price and rating limits inside search, lifting "
    "matching results from 70% to 100% (57/81 → 48/48) with 15% fewer paid searches."
)
_visioneer["bullets"] = [
    "With a colleague, fine-tuned Stable Diffusion v1.5 with LoRA (PyTorch, Hugging Face Diffusers) on ~12k "
    "captioned floor-plan images to generate furnished 2D layouts from text prompts; a teammate trained the "
    "companion schematic model, and both were served to an Android AR app. Published in Machine Graphics & "
    "Vision (2025).",
]
PROJECTS = [_shop, _research, _visioneer]
