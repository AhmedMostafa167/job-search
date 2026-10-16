"""Junior AI Engineer (0–2 yrs), Cairo, full-time — via QSource (sourceqs.com), client unnamed. Seen 2026-10-16.

Classic ML junior role: data prep, training, evaluation, Python libs, integration, documentation.
Lead with the ML lifecycle; VISIONEER (training) moves up. No TensorFlow (PyTorch/sklearn cover the "plus").
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_JuniorAI"

TITLE = "AI Engineer — Machine Learning & LLM Applications"

SUMMARY = (
    "AI engineer working across the machine-learning lifecycle in Python: preparing and validating data, "
    "fine-tuning and training models with PyTorch and Hugging Face, evaluating them on labelled test sets, and "
    "integrating them into applications through APIs. Built a 12,730-product AI shopping assistant where measured "
    "changes raised right-product-ranked-first from 23% to 43%; fine-tuned Stable Diffusion with LoRA (published "
    "2025). As a Computer Science teaching assistant, documenting and explaining technical work is routine."
)

SKILLS = [
    ("Machine Learning & Deep Learning", "PyTorch, scikit-learn, Hugging Face Transformers, Diffusers, LoRA "
     "fine-tuning, XGBoost, neural networks and CNNs, model evaluation (labelled test sets, confidence intervals)"),
    ("Data", "pandas, NumPy, SQL, PostgreSQL, data cleaning and validation (Pydantic), spaCy, NLTK"),
    ("Experiments & MLOps", "MLflow, DVC, Langfuse, Docker, Docker Compose, GitHub Actions (CI), pytest, "
     "Prometheus, Grafana"),
    ("LLM Applications", "LangGraph, LangChain, retrieval-augmented generation (RAG), hybrid search (pgvector), "
     "rerankers, agents and tool calling, prompt engineering, RAGAS"),
    ("Integration", "Python, FastAPI, SQLAlchemy, Alembic, Gradio, Hugging Face Spaces, Nginx"),
]

_shop, _research, _visioneer = copy.deepcopy(_BASE_PROJECTS)
_shop["tagline"] = "AI product search with evaluation and monitoring"
_shop["bullets"] = [
    "Built the data pipeline for a 12,730-product catalogue: pandas loaders for five file formats, row-level "
    "validation with Pydantic (invalid rows dropped with per-row error reports), then embedding into PostgreSQL "
    "with pgvector for hybrid search and Cohere reranking.",
    "Measured retrieval stage by stage on 127 labelled queries with 95% confidence intervals: hybrid top-10 recall "
    "72% vs 56% keyword and 41% vector; reranking lifted right-product-first from 23% to 43% (40-query subset); "
    "an HNSW index cut median vector-search latency from 35 ms to 3.1 ms.",
    "Designed a code-graded evaluation of the LangGraph agent (12 tasks × 3 runs, tracked in Langfuse and MLflow): "
    "a revised prompt passed 12 of 12 tasks vs 7 with 29% fewer paid API calls.",
    "Integrated the models into a FastAPI service with long-term user memory and guardrails, deployed with Docker "
    "Compose, covered by 104 automated tests, GitHub Actions CI and Prometheus/Grafana monitoring; documented each "
    "experiment and its result in an improvement log.",
]
_visioneer["bullets"] = [
    "Fine-tuned Stable Diffusion v1.5 with LoRA (PyTorch, Hugging Face Diffusers) on ~12k captioned floor plans to "
    "generate furnished 2D layouts from text prompts; a teammate trained the companion schematic model, and both "
    "were served to an Android AR app. Published in Machine Graphics & Vision (2025).",
]
PROJECTS = [_shop, _visioneer, _research]
