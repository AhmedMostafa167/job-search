"""Henkel — AI Engineer (req. 89184, posted 2026-10-05) and Software Developer – GEN AI Solutions (req. 89134), New
Cairo, hybrid. Cornerstone portal. Both posts share one profile, so one CV covers both.
Asks: 3-4 yrs (stretch); generative models for text, image, audio and multimodal; fine-tune LLMs and diffusion
models; prompt strategies; RLHF experiments; PyTorch/TensorFlow; LLMs, transformers, diffusion; NLP, computer vision;
Docker/Kubernetes; GenAI apps; chatbots integrated with third-party services via REST APIs; C#/.NET; Power BI;
Azure Cognitive Services and Azure OpenAI (plus); 89134 also Databricks.
Leads with the LLM chatbot behind a REST API, then VISIONEER (diffusion LoRA fine-tuning, the rare match). Not
claimed: TensorFlow, Kubernetes, C#/.NET, Power BI, Azure, Databricks, RLHF, audio.
"""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _GENERAL_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Henkel_GenAI"

TITLE = "AI Engineer — Generative AI: LLM Applications & Diffusion Fine-Tuning (PyTorch · Hugging Face)"

SUMMARY = (
    "AI engineer who builds generative AI end to end in Python. Fine-tuned Stable Diffusion with LoRA on ~12k "
    "captioned images for text-to-floor-plan generation (published 2025), and builds LLM applications: a LangGraph "
    "chatbot agent with RAG, tool calling and structured outputs, served through a FastAPI REST API in Docker with "
    "tests, tracing and monitoring. Designs prompts and judges them with measurements: on a 12,730-product "
    "assistant, a revised prompt raised agent task success from 7 to 12 of 12 tasks with 29% fewer paid rerank "
    "calls, and reranking raised right-product-ranked-first from 23% to 43%. Computer Science teaching assistant."
)

SKILLS = [
    ("Generative AI", "LLMs and transformers (Hugging Face Transformers), Stable Diffusion, Hugging Face Diffusers, "
     "LoRA fine-tuning, prompt engineering, structured output (Pydantic), guardrails, Groq, Cohere"),
    ("LLM Applications", "LangGraph, LangChain, chatbots and agents with tool calling, retrieval-augmented "
     "generation (RAG), hybrid search (PostgreSQL full-text + pgvector), cross-encoder reranking, Chroma"),
    ("ML & Evaluation", "PyTorch, scikit-learn, XGBoost, pandas, NumPy, spaCy, NLTK; labelled test sets with "
     "confidence intervals, code-graded evaluation, LLM-as-a-judge, RAGAS, Langfuse, MLflow, DVC"),
    ("Backend & Deployment", "Python, FastAPI (REST APIs), SQL, PostgreSQL, SQLAlchemy, Git, Docker, "
     "Docker Compose, GitHub Actions (CI), pytest, Prometheus, Grafana, Gradio, Hugging Face Spaces"),
]

_shop, _research, _visioneer = copy.deepcopy(_GENERAL_PROJECTS)
_shop["tagline"] = "LLM chatbot agent with RAG behind a FastAPI REST API"
_visioneer["tagline"] = "Diffusion model fine-tuning: text-to-floor-plan generation with AR (2024)"
_visioneer["stack"] = "PyTorch · Stable Diffusion v1.5 · Hugging Face Diffusers · LoRA · Android · ARCore"
_visioneer["bullets"] = [
    "With a colleague, fine-tuned Stable Diffusion v1.5 with LoRA (PyTorch, Hugging Face Diffusers) on ~12k "
    "captioned floor-plan images to generate furnished 2D layouts from text prompts; a teammate trained the "
    "companion schematic model, and both were served to an Android AR app. Published in Machine Graphics & "
    "Vision (2025).",
]
PROJECTS = [_shop, _visioneer, _research]
