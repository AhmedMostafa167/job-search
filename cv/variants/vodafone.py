"""Vodafone Egypt — Discover Graduate Program | Technology | Data Intelligence | 2027 (12 months, Giza, hybrid).
opportunities.vodafone.com/job/Giza-Discover-Graduate-Program-Technology-Data-Intelligence-2027/1449718833/
Seen 2026-10-24. Eligibility: 2025/2026/Jan-2027 grads; males who completed military service in 2024 or 2025.
Asks: ML algorithms, statistics, data analysis and visualisation, preprocessing/feature engineering/training/
evaluation, pandas/NumPy/scikit-learn/PyTorch, LLMs, GenAI, agentic AI, tool calling, workflow orchestration,
LangChain/LangGraph, RAG, vector DBs, prompt engineering, APIs/databases/pipelines; evaluation, monitoring,
deployment. Lead with ML + statistics + agents. No TensorFlow or matplotlib-style plotting claimed.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Vodafone"

TITLE = "AI Engineer — Machine Learning, Generative AI & Agentic Systems"

SUMMARY = (
    "AI engineer combining machine learning and data analysis with generative and agentic AI in Python: preparing "
    "and validating data, training and fine-tuning models with PyTorch and Hugging Face, and building tool-calling "
    "LangGraph agents with RAG, judged by statistics rather than impressions. On a 12,730-product shopping assistant, "
    "measured retrieval on 127 labelled queries with 95% confidence intervals and raised agent task success from 7 "
    "to 12 of 12 tasks. Published researcher (LoRA fine-tuning; quantum machine learning on EEG signals), Computer "
    "Science teaching assistant and native Arabic speaker."
)

SKILLS = [
    ("Machine Learning & Data Analysis", "scikit-learn, XGBoost, pandas, NumPy, SQL, statistical evaluation "
     "(labelled test sets, 95% confidence intervals, breakdowns by segment), data cleaning and validation "
     "(Pydantic), Grafana dashboards"),
    ("Deep Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA fine-tuning, neural networks and CNNs, "
     "spaCy, NLTK"),
    ("Generative & Agentic AI", "LLMs, LangGraph, LangChain, agents and tool/function calling, multi-step workflows "
     "with conditional routing and bounded retries, conversational memory, retrieval-augmented generation (RAG), "
     "vector databases (pgvector, Chroma), hybrid search, reranking, prompt engineering, structured output, "
     "guardrails, Groq, Cohere"),
    ("Evaluation, Monitoring & Deployment", "code-graded agent evaluation, LLM-as-a-judge, RAGAS, Langfuse, MLflow, "
     "DVC, Prometheus, FastAPI (REST APIs), PostgreSQL, SQLAlchemy, Docker, Docker Compose, GitHub Actions (CI), "
     "pytest, Hugging Face Spaces"),
]

_shop, _research, _visioneer = copy.deepcopy(_BASE_PROJECTS)
_shop["tagline"] = "Tool-calling LLM agent over a 12,730-product catalogue"
_shop["bullets"] = [
    "Built the data pipeline: pandas loaders for five file formats with row-level Pydantic validation (invalid rows "
    "dropped with a per-row error report), then embeddings in PostgreSQL/pgvector for hybrid keyword + vector search "
    "with Cohere reranking.",
    "Analysed retrieval on 127 labelled queries with 95% confidence intervals, broken down by how queries were "
    "phrased: hybrid top-10 recall 72% vs 56% keyword and 41% vector; reranking lifted right-product-first from "
    "23% to 43% (40-query subset); an HNSW index cut median search latency from 35 ms to 3.1 ms.",
    "Built a tool-calling LangGraph agent that remembers each customer's lasting preferences, and a code-graded "
    "evaluation of it (12 tasks × 3 runs): prompt v2 passed 12 of 12 tasks vs 7 with 29% fewer paid calls; v3 "
    "moved price limits inside search, lifting on-target results from 70% to 100%.",
    "Deployed it as a FastAPI service with Docker Compose, guardrails (0 of 21 legitimate facts refused), Langfuse "
    "tracing, Prometheus/Grafana monitoring, 104 automated tests and GitHub Actions CI.",
]
PROJECTS = [_shop, _research, _visioneer]

COVER_LETTER = {
    "date": "24 October 2026",
    "to": ["Talent Acquisition, Vodafone Egypt", "Discover Graduate Program 2027 — Technology, Data Intelligence"],
    "greeting": "Dear Vodafone Talent Acquisition Team,",
    "paragraphs": [
        "I'm applying for the Discover Graduate Program 2027 in Technology, Data Intelligence. The track's focus, "
        "machine learning and data analytics with a primary focus on AI, generative AI and agentic AI, describes "
        "the work I've been doing, and I'd like to grow it inside a business at Vodafone's scale.",
        "On the agentic side, I built a Shopping Assistant: a tool-calling LangGraph agent that searches a "
        "12,730-product catalogue with hybrid retrieval over PostgreSQL and pgvector plus reranking, remembers each "
        "customer's lasting preferences, and runs as a FastAPI service with Docker, Langfuse tracing and Prometheus "
        "and Grafana monitoring. I also designed a research agent whose multi-step workflow rewrites queries, grades "
        "what it retrieves and reflects on its own answer before replying.",
        "On the data side, I measured every change before keeping it. I evaluated retrieval on 127 labelled queries "
        "with 95% confidence intervals and broke the results down by how queries were phrased: hybrid search found "
        "the right product in the top 10 for 72% of queries, against 56% for keyword and 41% for vector search. "
        "A code-graded evaluation of the agent, 12 tasks run 3 times each, showed a revised prompt passing all 12 "
        "tasks instead of 7. Before that, I fine-tuned Stable Diffusion with LoRA in work published in 2025, and as "
        "a research intern I built a quantum machine-learning pipeline that denoised and classified EEG signals.",
        "I completed my BSc in Computer Science in June 2024 and then my mandatory military service, and since "
        "February 2026 I've been a Computer Science teaching assistant, where I designed and led 50 lab sessions for "
        "more than 600 students. This would be my first role in industry. I'm a native Arabic speaker with "
        "professional English, I live in Giza, and I'd welcome the chance to show what I can contribute to Data "
        "Intelligence.",
    ],
    "closing": "Sincerely,",
}
