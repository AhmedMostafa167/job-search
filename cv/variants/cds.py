"""CDS Solutions (Creative Digital Solutions; Odoo Gold Partner, Nasr City, Cairo) — Junior Applied AI Engineer.
Posted 2026-10-29 on cds-solutions.co (Odoo careers page, job 31) and LinkedIn. Junior or fresh graduate.
Asks: build, test and deploy web applications with AI-assisted development (Claude Code, Cursor, Codex); agentic
coding, AI agents and automated workflows; frontend/backend frameworks, APIs, databases, cloud; LLM and AI API
integrations with business systems; Git, debugging; personal projects or GitHub a big plus. JavaScript/TypeScript
is "a plus".
Claude Code is real (this repo, the CV builder, the portfolio and the Research Assistant were built with it from his
designs). Not claimed: JavaScript/TypeScript, Cursor, Codex, OpenCode, cloud platforms beyond Hugging Face Spaces,
Odoo.
"""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _GENERAL_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_CDS"

TITLE = "Applied AI Engineer — LLM Apps & AI Agents, Built with AI-Assisted Development (Python · Claude Code)"

SUMMARY = (
    "Applied AI engineer who designs AI applications and builds them fast with AI coding agents (Claude Code): "
    "LangGraph agents with tool calling and RAG, served through FastAPI REST APIs on PostgreSQL, packaged with "
    "Docker and shipped through GitHub Actions CI. Checks every change with tests and measurements: on a "
    "12,730-product assistant, a revised prompt raised agent task success from 7 to 12 of 12 tasks with 29% fewer "
    "paid rerank calls, backed by 104 automated tests. Designed a research agent built with Claude Code and live on "
    "Hugging Face Spaces. Computer Science graduate and teaching assistant in Giza; teaches a starter MLOps course "
    "(FastAPI, Docker, MLflow) to about 500 students."
)

SKILLS = [
    ("AI-Assisted Development", "Claude Code (agentic coding from a written design: implementation, tests, "
     "refactoring, debugging), reviewing AI-written code against tests, prompt and spec writing, Git and GitHub"),
    ("LLM Apps & Agents", "LangGraph, LangChain, agents and tool calling, retrieval-augmented generation (RAG), "
     "hybrid search (PostgreSQL full-text + pgvector), reranking, structured output (Pydantic), guardrails; LLM "
     "APIs (Anthropic, OpenAI, Groq, Cohere, Hugging Face)"),
    ("Backend, APIs & Deployment", "Python, FastAPI (REST APIs, JSON), SQL, PostgreSQL, SQLAlchemy, Alembic, Docker, "
     "Docker Compose, GitHub Actions (CI), pytest, Nginx, Gradio web UIs, Hugging Face Spaces"),
    ("Testing & Monitoring", "pytest unit and integration tests, code-graded agent evaluation, labelled test sets, "
     "Langfuse tracing, Prometheus, Grafana, MLflow; ML with PyTorch, Hugging Face Transformers and scikit-learn"),
]

_shop, _research, _visioneer = copy.deepcopy(_GENERAL_PROJECTS)
_shop["tagline"] = "LLM agent web service: FastAPI API, PostgreSQL, Docker, CI"
_research["bullets"][0] = (
    "Designed a self-correcting research agent over arXiv and the web (query rewriting, hybrid retrieval, relevance "
    "grading, cited answers, a reflection step with a bounded retry) and built it with Claude Code; structured "
    "outputs for each decision."
)
_visioneer["bullets"] = [
    "With a colleague, fine-tuned Stable Diffusion v1.5 with LoRA (PyTorch, Hugging Face Diffusers) on ~12k "
    "captioned floor-plan images to generate furnished 2D layouts from text prompts; a teammate trained the "
    "companion schematic model, and both were served to an Android AR app. Published in Machine Graphics & "
    "Vision (2025).",
]
PROJECTS = [_shop, _research, _visioneer]
