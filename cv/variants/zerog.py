"""zeroG (Lufthansa Group's AI company, Frankfurt) — Junior AI Engineering Consultant (m/f/d). LinkedIn 4484831643 and
4484832538, seen 2026-11-02. Entry level, EUR 54-73k, English working language, relocation package for moves to
Germany; "we don't expect you to tick every box".
Asks: Python and software engineering fundamentals; first hands-on ML/GenAI work (LLMs, RAG, agents) from studies,
internships or personal projects; SQL and data pipelines; exposure to Azure, GCP or AWS; MLOps/LLMOps, evaluation,
monitoring; AI security and compliance basics (GDPR, EU AI Act); explaining technical topics clearly; growing into a
consulting role. Bonus: managed AI platforms or observability tooling, agentic architectures, aviation.
Not claimed: cloud platforms (only Hugging Face Spaces), Azure OpenAI or Vertex AI, GDPR or EU AI Act work.
"""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _GENERAL_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_zeroG"

TITLE = "Junior AI Engineer — GenAI, RAG & Agents, with Evaluation and Monitoring (Python)"

SUMMARY = (
    "AI engineer who builds GenAI solutions end to end in Python and explains them clearly. Built a LangGraph agent "
    "with hybrid RAG over 12,730 products: data ingested with pandas from five file formats and validated row by "
    "row with Pydantic, served through a FastAPI REST API on PostgreSQL in Docker, with GitHub Actions CI, 104 "
    "automated tests, Langfuse tracing, MLflow and Prometheus/Grafana monitoring. Measures every change: hybrid "
    "retrieval reached 72% top-10 recall vs 41% vector-only on 127 labelled queries, and a revised prompt raised "
    "agent task success from 7 to 12 of 12. Teaches Computer Science to 700+ students and a starter MLOps course to "
    "about 500; mentors learners in the MLOps MENA community. Open to relocating to Germany."
)

SKILLS = [
    ("GenAI, RAG & Agents", "LangGraph, LangChain, agents and tool calling, retrieval-augmented generation (RAG), "
     "hybrid search (PostgreSQL full-text + pgvector), reranking, prompt engineering and versioning, structured "
     "output (Pydantic), guardrails; LLM APIs (Anthropic, OpenAI, Groq, Cohere, Hugging Face)"),
    ("Data & Engineering", "Python, SQL, PostgreSQL, SQLAlchemy, Alembic, pandas, NumPy, data ingestion and "
     "validation pipelines (Pydantic), FastAPI (REST APIs), Docker, Docker Compose, Git, GitHub Actions (CI), pytest"),
    ("MLOps, Evaluation & Monitoring", "labelled test sets with 95% confidence intervals, code-graded agent "
     "evaluation, LLM-as-a-judge, RAGAS, Langfuse tracing, MLflow, DVC, Prometheus, Grafana"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA fine-tuning, scikit-learn, XGBoost, "
     "spaCy, NLTK"),
]

_shop, _research, _visioneer = copy.deepcopy(_GENERAL_PROJECTS)
_visioneer["bullets"] = [
    "With a colleague, fine-tuned Stable Diffusion v1.5 with LoRA (PyTorch, Hugging Face Diffusers) on ~12k "
    "captioned floor-plan images to generate furnished 2D layouts from text prompts; a teammate trained the "
    "companion schematic model, and both were served to an Android AR app. Published in Machine Graphics & "
    "Vision (2025).",
]
PROJECTS = [_shop, _research, _visioneer]
