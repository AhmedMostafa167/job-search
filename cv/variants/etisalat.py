"""Etisalat Egypt (e&) — MLOps Engineer, Cairo (Wuzzuf, row 2026-10-18-etisalat-mlops). Rebuilt 2026-10-29: the
original variant was made in another session and its source isn't in this repo. Tracker notes for the post: serving
APIs, Docker, CI/CD, MLflow, Prometheus/Grafana match; gaps DataRobot, Databricks, Netezza, DataStage, Kubernetes,
cloud. MLOps framing reused from the petrochoice skills. Not claimed: Airflow, Kubernetes, cloud, DataRobot.
"""
from variants.petrochoice import *  # noqa: F401,F403
from variants.petrochoice import SKILLS as _P_SKILLS
from variants.petrochoice import _shop, _research, _visioneer

FILE_STEM = "Ahmed_Dorra_CV_Etisalat"

TITLE = "MLOps / AI Engineer — Model Serving, CI/CD & Monitoring (Python · Docker · MLflow)"

SUMMARY = (
    "AI engineer who takes models from training to monitored service: FastAPI model and LLM services packaged with "
    "Docker and Docker Compose, GitHub Actions CI with 104 automated tests, experiment tracking with MLflow and DVC, "
    "and Prometheus/Grafana monitoring with Langfuse tracing. Measures every release: on a 12,730-product AI "
    "assistant, an HNSW index cut median vector-search latency from 35 ms to 3.1 ms and reranking lifted "
    "right-product-first from 23% to 43%, all checked on labelled data. Fine-tunes models with PyTorch and Hugging "
    "Face (LoRA, published 2025). Computer Science graduate (2024) and teaching assistant, based in Giza."
)

SKILLS = [_P_SKILLS[1], _P_SKILLS[0], _P_SKILLS[2], _P_SKILLS[3]]
PROJECTS = [_shop, _visioneer, _research]
