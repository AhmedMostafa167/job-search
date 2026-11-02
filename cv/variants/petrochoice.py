"""Petrochoice Integrated Services — AI Engineer (oil & gas), Egypt only. hr.Petrochoice@gmail.com, subject "AI Engineer".
Seen 2026-10-16. Small Maadi firm (est. 2023). Asks: data collection + training in CV or NLP, YOLO, system design,
MLOps/FastAPI, Docker, deploy local + cloud. Gap: YOLO / object detection — not on the CV, don't claim it.
Lead with vision training (VISIONEER first) and deployment.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Petrochoice"

TITLE = "AI Engineer — Model Training & Deployment (Computer Vision · NLP · LLMs)"

SUMMARY = (
    "AI engineer who trains models and ships them: fine-tuned Stable Diffusion with LoRA on ~12k images for "
    "floor-plan generation (published 2025), and builds production AI services with FastAPI and Docker, run "
    "locally with Docker Compose and deployed in the cloud on Hugging Face Spaces, with monitoring and CI. On a "
    "12,730-product AI assistant, measured changes raised right-product-ranked-first from 23% to 43% and cut "
    "vector-search latency from 35 ms to 3.1 ms. Computer Science teaching assistant (neural networks and CNNs)."
)

SKILLS = [
    ("Computer Vision & Deep Learning", "PyTorch, Hugging Face Diffusers, Stable Diffusion, LoRA fine-tuning, "
     "CNNs, Hugging Face Transformers, scikit-learn, XGBoost"),
    ("MLOps & Deployment", "FastAPI, Docker, Docker Compose, GitHub Actions (CI), pytest, MLflow, DVC, "
     "Prometheus, Grafana, Nginx, Gradio, Hugging Face Spaces"),
    ("NLP & LLMs", "Hugging Face Transformers, spaCy, NLTK, embeddings, rerankers, LangGraph, LangChain, "
     "retrieval-augmented generation (RAG), agents and tool calling, Langfuse, RAGAS"),
    ("Data & Backend", "Python, SQL, PostgreSQL, pgvector, SQLAlchemy, Alembic, pandas, NumPy, "
     "data validation (Pydantic)"),
]

_shop, _research, _visioneer = copy.deepcopy(_BASE_PROJECTS)
_visioneer["tagline"] = "Computer vision: text-to-floor-plan image generation with AR (2024)"
_visioneer["stack"] = "PyTorch · Stable Diffusion v1.5 · Hugging Face Diffusers · LoRA · Android · ARCore"
_visioneer["bullets"] = [
    "With a colleague, fine-tuned Stable Diffusion v1.5 with LoRA (PyTorch, Hugging Face Diffusers) on ~12k "
    "captioned floor-plan "
    "images to generate furnished 2D layouts from text prompts; a teammate trained the companion schematic model, "
    "and both were served to an Android AR app. Published in Machine Graphics & Vision (2025).",
]
_shop["tagline"] = "AI service designed, deployed and monitored end to end"
_shop["bullets"] = [
    "Designed the system architecture and built the data pipeline for a 12,730-product catalogue: pandas loaders for "
    "five file formats, row-level validation with Pydantic, embedding into PostgreSQL/pgvector, hybrid retrieval "
    "with reranking, and a LangGraph agent with long-term user memory.",
    "Served it as a FastAPI service packaged with Docker Compose, with Prometheus/Grafana monitoring, Langfuse "
    "tracing, 104 automated tests and GitHub Actions CI.",
    "Measured each stage on 127 labelled queries with 95% confidence intervals: reranking lifted right-product-first "
    "from 23% to 43%; an HNSW index cut median vector-search latency from 35 ms to 3.1 ms; a code-graded agent "
    "evaluation (12 tasks × 3 runs) showed a revised prompt passing 12 of 12 tasks vs 7.",
]
PROJECTS = [_visioneer, _shop, _research]
