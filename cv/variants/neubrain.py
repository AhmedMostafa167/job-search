"""Neubrain Solutions (Maharashtra, India; B2B growth and sales outsourcing with AI agents) — AI Engineer, 0-2 years,
100% remote, work from anywhere. LinkedIn post seen 2026-10-30; apply by email to contact@neubrain.in with resume and
GitHub/portfolio.
Asks: build and deploy LLM-powered features; design RAG pipelines, agents and prompt workflows; fine-tune, evaluate
and optimise models for quality and cost; strong Python; ML/DL basics (PyTorch, TensorFlow or scikit-learn); LLMs,
APIs, LangChain or LlamaIndex; personal projects count. Nice to have: vector databases, cloud, MLOps, model evaluation.
Leads with the shipped agent and its quality-and-cost measurements. Not claimed: TensorFlow, LlamaIndex, cloud
platforms beyond Hugging Face Spaces.
"""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _GENERAL_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Neubrain"

TITLE = "AI Engineer — LLM Features, RAG Pipelines & Agents, Evaluated for Quality and Cost (Python)"

SUMMARY = (
    "AI engineer who ships LLM-powered features in Python: RAG pipelines, LangGraph agents with tool calling, and "
    "prompt workflows, served through FastAPI in Docker with tests, tracing and monitoring. Optimises for quality "
    "and cost with measurements: on a 12,730-product assistant, a revised prompt raised agent task success from 7 "
    "to 12 of 12 tasks with 29% fewer paid rerank calls, moving price limits inside search lifted matching results "
    "from 70% to 100% with 15% fewer paid searches, and hybrid retrieval reached 72% top-10 recall vs 41% vector "
    "alone. LoRA fine-tuning of Stable Diffusion (published 2025); teaches a starter MLOps course to about 500 "
    "students. Based in Egypt, working remotely."
)

SKILLS = [
    ("LLM Features & Agents", "LangGraph, LangChain, agents and tool calling, prompt engineering and versioning, "
     "structured output (Pydantic), guardrails, conversational memory; LLM APIs (Anthropic, OpenAI, Groq, Cohere, "
     "Hugging Face)"),
    ("RAG & Vector Databases", "pgvector (HNSW), Chroma, PostgreSQL full-text and BM25, hybrid search with "
     "Reciprocal Rank Fusion, cross-encoder reranking, document chunking and embeddings"),
    ("Evaluation & MLOps", "labelled test sets with 95% confidence intervals, code-graded agent evaluation, paid-call "
     "counts per task, LLM-as-a-judge, RAGAS, Langfuse tracing, MLflow, DVC, Prometheus, Grafana, GitHub Actions "
     "(CI)"),
    ("ML & Backend", "Python, PyTorch, Hugging Face Transformers, Diffusers, LoRA fine-tuning, scikit-learn, "
     "XGBoost, pandas, FastAPI (REST APIs), SQL, PostgreSQL, Docker, pytest, Gradio, Hugging Face Spaces"),
]

_shop, _research, _visioneer = copy.deepcopy(_GENERAL_PROJECTS)
_shop["tagline"] = "LLM agent with RAG, shipped behind a FastAPI API and tuned for quality and cost"
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
