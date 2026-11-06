"""Capgemini Egypt — Software Engineer (GenAI), Cairo. careers.capgemini.com job 1453382933, new on 2026-11-02.
"Preferably at least 2 years" (stretch on years).
Asks: secure, scalable, reliable software services; AI-driven solutions within application architecture guidelines;
code quality, performance and security tuning; LLMs integrated with external knowledge sources; RAG architectures;
embeddings, semantic search, vector databases; Python (JS/TS a plus); LangChain and LangGraph; RESTful APIs and
backend services; Git (GitFlow). Nice: AI/ML training and deployment services; speech-to-text / text-to-speech.
Leads with the RAG service and its measured retrieval and latency. Not claimed: JavaScript/TypeScript, GitFlow by name,
speech (STT/TTS), cloud AI services.
"""
from variants.migrationit import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_Capgemini_GenAI"

TITLE = "Generative AI Software Engineer — LLMs, RAG & LangGraph Services (Python · FastAPI)"

SUMMARY = (
    "Software engineer who builds generative AI services in Python: LLMs connected to external knowledge through RAG "
    "(document chunking, embeddings, semantic and hybrid search on pgvector and PostgreSQL full-text, reranking) and "
    "LangGraph/LangChain workflows with tool calling, served through FastAPI REST APIs on PostgreSQL in Docker. "
    "Builds for reliability and performance: Pydantic-validated outputs, input guardrails, 104 automated tests, "
    "GitHub Actions CI, tracing and monitoring; hybrid retrieval reached 72% top-10 recall vs 41% vector-only on 127 "
    "labelled queries, and an HNSW index cut median vector-search latency from 35 ms to 3.1 ms. Computer Science "
    "graduate and teaching assistant in Giza; native Arabic speaker with professional English."
)

SKILLS = [
    ("LLMs & RAG", "RAG architectures, document chunking, embeddings, semantic search, vector databases (pgvector "
     "HNSW, Chroma), PostgreSQL full-text and BM25, hybrid search with Reciprocal Rank Fusion, cross-encoder "
     "reranking; LLM APIs (Anthropic, OpenAI, Groq, Cohere, Hugging Face)"),
    ("LangChain & LangGraph", "LangGraph workflows and agents, LangChain, tool calling, structured output and "
     "response validation (Pydantic), prompt engineering and versioning, guardrails, bounded retries"),
    ("Backend Services", "Python, FastAPI (RESTful APIs, JSON), SQL, PostgreSQL, SQLAlchemy, Alembic, Docker, "
     "Docker Compose, Nginx, Git and GitHub, GitHub Actions (CI), pytest, logging"),
    ("Quality & Performance", "labelled test sets with 95% confidence intervals, code-graded evaluation, latency "
     "measurement and tuning, Langfuse tracing, Prometheus, Grafana, MLflow; PyTorch, Hugging Face Transformers"),
]
