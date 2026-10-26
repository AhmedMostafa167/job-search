"""CIB (Commercial International Bank) — AI Engineer / AI Senior Engineer (job 260002IN), AI Engineering team,
Giza head office. Posted 2026-10-25 on cibeg.taleo.net, seen 2026-10-26, alongside an AI Engineering Manager,
AI Solution Architect, AI Product Owner, AI Program Manager and Principal AI Engineer (a new team under Kamran
Bader, Chief Data, Analytics & AI Officer since mid-2026).
Asks (AI Engineer level): 1-3 yrs; GenAI integration pipelines, API wrappers, inference services; LLMOps (model
versioning, CI/CD, automated testing, monitoring, drift detection); APIs exposing model outputs; unit and integration
tests; production monitoring; reusable components; documentation and runbooks; secure coding; Python with
PyTorch/scikit-learn; Docker/Kubernetes; RAG; prompt engineering; data pipelines.
Lead with the Shopping Assistant as a production-style LLM service. No Kubernetes, drift detection or banking claimed.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS
from cv_content import SKILLS as _BASE_SKILLS

FILE_STEM = "Ahmed_Dorra_CV_CIB"

TITLE = "AI Engineer — GenAI Engineering & LLMOps (RAG · APIs · CI/CD · Monitoring)"

SUMMARY = (
    "AI engineer who builds GenAI features as production-style services in Python: RAG pipelines and LangGraph "
    "agents behind FastAPI APIs, packaged with Docker, tested (104 automated tests) and shipped through GitHub "
    "Actions CI, with Langfuse tracing and prompt versioning, MLflow and DVC for experiments and data, and "
    "Prometheus/Grafana monitoring. On a 12,730-product assistant, measured every change before keeping it: hybrid "
    "retrieval reached 72% top-10 recall vs 41% for vector search alone, and an HNSW index cut median search latency "
    "from 35 ms to 3.1 ms. Based in Giza; Computer Science teaching assistant used to documenting and explaining "
    "systems."
)

SKILLS = [
    ("LLMOps & Engineering", "Docker, Docker Compose, GitHub Actions (CI), pytest (unit and integration tests), "
     "Langfuse (tracing, prompt versioning, experiments), MLflow, DVC, Prometheus, Grafana, Git, Nginx"),
    ("APIs & Data", "Python, FastAPI (REST APIs), Pydantic validation, SQL, PostgreSQL, SQLAlchemy, Alembic, pandas "
     "ingestion pipelines with row-level validation"),
    ("GenAI & RAG", "retrieval-augmented generation (RAG), hybrid search (PostgreSQL full-text + pgvector, Reciprocal "
     "Rank Fusion), cross-encoder reranking, LangGraph, LangChain, agents and tool calling, prompt engineering, "
     "structured output, guardrails; Groq, Cohere, Anthropic and OpenAI APIs"),
    _BASE_SKILLS[3],
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "Production-style LLM service: RAG, agent, API, CI and monitoring"
PROJECTS[0]["bullets"] = [
    "Built a LangGraph agent and RAG pipeline over 12,730 products, served through a FastAPI REST API on PostgreSQL "
    "and pgvector, with ingestion from five file formats (pandas) and row-level Pydantic validation.",
    "Engineered it for operation, not just a demo: Docker Compose deployment, 104 automated tests in GitHub Actions "
    "CI, Langfuse tracing and prompt versioning, and Prometheus/Grafana dashboards.",
    "Measured each change on labelled data before keeping it: 127 queries with 95% confidence intervals (hybrid "
    "top-10 recall 72% vs 56% keyword and 41% vector); a 12-task × 3-run agent test (prompt v2 passed 12 of 12 vs "
    "7 with 29% fewer paid rerank calls); an HNSW index cut median vector search from 35 ms to 3.1 ms.",
    "Added input and memory-write guardrails (0 of 21 legitimate facts refused) and a check that every quoted price "
    "matches the catalogue (passed in 25 of 25 applicable runs).",
]

COVER_LETTER = {
    "date": "26 October 2026",
    "to": ["AI Engineering Team, Commercial International Bank (CIB)", "AI Engineer (260002IN), Giza Head Office"],
    "greeting": "Dear Hiring Team,",
    "paragraphs": [
        "I'm applying for the AI Engineer role (260002IN) in CIB's new AI Engineering team. The role is about taking "
        "approved GenAI designs into production with proper engineering around them: APIs, CI/CD, testing, "
        "monitoring and documentation. That is the part of AI work I've focused on most.",
        "My main project is a Shopping Assistant that I built as a production-style service. A LangGraph agent and "
        "a RAG pipeline (PostgreSQL full-text search plus pgvector, fused and reranked) run behind a FastAPI API. "
        "Data comes in through pandas loaders with row-level Pydantic validation. The service runs in Docker "
        "Compose with 104 automated tests in GitHub Actions CI, Langfuse tracing and prompt versioning, and "
        "Prometheus and Grafana monitoring.",
        "I also measure before I ship. On 127 labelled queries with 95% confidence intervals, hybrid retrieval "
        "found the right product in the top 10 72% of the time, against 41% for vector search alone. A code-graded "
        "agent test of 12 tasks run 3 times each showed a revised prompt passing 12 of 12 instead of 7, with 29% "
        "fewer paid rerank calls. An HNSW index cut median search latency from 35 ms to 3.1 ms. I added guardrails "
        "and a check that every price the agent quotes matches the catalogue, which matters even more in banking.",
        "My experience so far is in my own projects and in teaching rather than in a bank, and I haven't yet worked "
        "with Kubernetes or drift detection in production. I'd expect to learn both quickly in a team with clear "
        "engineering standards. I live in Giza, close to the head office, and as a Computer Science teaching "
        "assistant I'm used to writing clear documentation and explaining technical work.",
    ],
    "closing": "Sincerely,",
}
