"""MigrationIT — AI Engineer, Cairo (Zoho Recruit job 586058000030469269, posted 2026-10-28). 0-2 years.
Asks: Python components connecting apps to AI models, services and databases; prompt development, model API
integration, structured outputs and validation of model responses; RAG (document preparation, chunking, embeddings);
multi-step workflows with tool calls, state, retries, error handling and human review; evaluation test cases
(relevance, factual consistency, response time, failure scenarios); support (failed API calls, retrieval problems);
HTTP/REST, JSON, exception handling, SQL, vector search; LangChain/LangGraph; Git, testing, logs; AI coding assistants
used responsibly. Preferred: chatbot or document Q&A project, FastAPI, Docker, cloud, guardrails and monitoring.
Every core ask matches. Not claimed: n8n, cloud platforms, human-review queues, fallbacks.
"""
from variants.general import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_MigrationIT"

TITLE = "AI Engineer — LLM Integration, RAG Pipelines & Evaluation (Python · FastAPI · LangGraph)"

SUMMARY = (
    "AI engineer who connects applications to LLMs in Python: model API integration with Pydantic-validated "
    "structured outputs, RAG pipelines (document chunking, embeddings, hybrid vector search, reranking), and "
    "LangGraph workflows with tool calls, state and bounded retries, served through FastAPI REST APIs on "
    "PostgreSQL in Docker. Writes test cases before trusting a change: on a 12,730-product assistant, labelled "
    "queries measured relevance (72% top-10 recall), a grounding check confirmed quoted prices in 25 of 25 runs, "
    "and an index change cut median search time from 35 ms to 3.1 ms. 104 automated tests, guardrails, tracing and "
    "monitoring. Computer Science graduate (2024) based in Giza."
)

SKILLS = [
    ("LLM Integration", "LLM APIs (Anthropic, OpenAI, Groq, Cohere, Hugging Face), prompt engineering and "
     "versioning, structured output and response validation (Pydantic), input guardrails, LangGraph, LangChain, "
     "tool calling, multi-step workflows with state and bounded retries"),
    ("Retrieval (RAG)", "document chunking, embeddings, pgvector (HNSW), Chroma, PostgreSQL full-text and BM25, "
     "hybrid search with Reciprocal Rank Fusion, cross-encoder reranking"),
    ("Evaluation & Monitoring", "test cases on labelled data with 95% confidence intervals, code-graded evaluation, "
     "grounding checks, LLM-as-a-judge, RAGAS, latency measurement, Langfuse tracing, Prometheus, Grafana, MLflow"),
    ("Backend & Tools", "Python, FastAPI (REST APIs, JSON), SQL, PostgreSQL, SQLAlchemy, Alembic, Git, Docker, "
     "Docker Compose, GitHub Actions (CI), pytest, logging; PyTorch, Hugging Face Transformers, scikit-learn"),
]
