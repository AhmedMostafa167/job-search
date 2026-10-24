"""Applied Innovation Center (AIC), MCIT — Junior R&D Engineer (job code R&D003), NLP, 0–2 yrs, Cairo/Giza, on-site.
Apply on aic.gov.eg/careers/3 (name, email, PDF CV); LinkedIn applications closed. Seen 2026-10-19.
Project: Arabic speech-to-speech machine translation (ASR + MT + TTS); AIC also built the Karnak Arabic LLM.
Asks: ML/DL theory and practice, state-of-the-art NLP, PyTorch, Python, Git, Linux, databases, literature reviews,
benchmarking, documentation, English + Arabic. No speech, MT, TensorFlow or Linux claimed.
Lead with research and evaluation rigour, fine-tuning, publications and native Arabic.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_AIC"

TITLE = "AI Engineer — NLP, LLMs & Deep Learning Research"

SUMMARY = (
    "Computer Science graduate and published researcher working on deep learning and language models in Python and "
    "PyTorch: fine-tuning with LoRA, building LLM and retrieval systems, and benchmarking them carefully, with "
    "labelled test sets, 95% confidence intervals and stage-by-stage comparisons. On a 12,730-product "
    "search system, measured hybrid retrieval at 72% top-10 recall vs 56% keyword and 41% vector, and reranking "
    "lifted the right answer to first place from 23% to 43%. Native Arabic speaker; Computer Science teaching "
    "assistant used to documenting and presenting technical work."
)

SKILLS = [
    ("Deep Learning & NLP", "PyTorch, Hugging Face Transformers, Diffusers, LoRA fine-tuning, large language models, "
     "retrieval-augmented generation (RAG), embeddings and hybrid search, cross-encoder reranking, LangGraph, "
     "LangChain, spaCy, NLTK, neural networks and CNNs"),
    ("Evaluation & Benchmarking", "labelled test sets with 95% confidence intervals, recall at 1/3/10, ablations "
     "across system stages and query types, latency benchmarking, code-graded evaluation, LLM-as-a-judge, RAGAS, "
     "MLflow, DVC, Langfuse"),
    ("Data", "pandas, NumPy, data cleaning and row-level validation (Pydantic), SQL, PostgreSQL, pgvector, Chroma"),
    ("Software Engineering", "Python, FastAPI, SQLAlchemy, Alembic, Git, GitHub Actions (CI), pytest, Docker, "
     "Docker Compose, Prometheus, Grafana, Gradio, Hugging Face Spaces"),
    ("Machine Learning", "scikit-learn, XGBoost, quantum machine learning (variational autoencoders), LDA"),
]

_shop, _research, _visioneer = copy.deepcopy(_BASE_PROJECTS)
_shop["tagline"] = "Retrieval and LLM agent system, benchmarked stage by stage"
_shop["bullets"] = [
    "Built a language search and agent system over 12,730 products: pandas loaders for five file formats with "
    "row-level Pydantic validation, embeddings in PostgreSQL/pgvector, keyword + vector retrieval fused with "
    "Reciprocal Rank Fusion, cross-encoder reranking, and a LangGraph agent on top.",
    "Benchmarked each stage on 127 labelled queries with 95% confidence intervals and broke results down by how "
    "queries were phrased: hybrid top-10 recall 72% vs 56% keyword and 41% vector; reranking lifted right-answer-"
    "first from 23% to 43% (40-query subset); an HNSW index cut median search latency from 35 ms to 3.1 ms.",
    "Designed a code-graded evaluation of the agent (12 tasks × 3 runs): a revised prompt passed 12 of 12 tasks vs "
    "7; moving constraints inside search lifted on-target results from 70% to 100%.",
    "Kept an improvement log of every measured change (before-and-after numbers, findings and the decision "
    "taken); 104 automated tests and CI.",
]
_research["bullets"][0] = (
    "Designed a self-correcting LangGraph workflow for literature questions over arXiv and the web: query "
    "rewriting, hybrid retrieval, relevance grading, cited generation and a reflection step with a bounded retry."
)
PROJECTS = [_shop, _visioneer, _research]
