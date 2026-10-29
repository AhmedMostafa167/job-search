"""_VOIS (Vodafone Intelligent Solutions), Egypt (Cairo / Smart Village, Giza). General tailoring for VOIS AI roles,
requested by Ahmed 2026-10-29 (referral or any VOIS AI posting). VOIS Egypt AI postings seen on
opportunities.vodafone.com / flexa.careers: Senior AI & Automation Engineer (1367221633, 1422915633), Senior Python
Backend Developer (1407931833), E2E Senior AI & Data Solution Architect (1420211733); mostly senior.
Recurring asks: Python services; AI-powered automation that combines traditional automation with GenAI/LLMs; RAG;
agentic workflows, orchestration, guardrails and evaluation; responsible AI (data privacy, transparency, secure
GenAI deployment, PEFT and RAG); Agile/SAFe; cloud. Separate from the Vodafone Egypt Discover Graduate Program CV
(vodafone.py). Not claimed: Agile/SAFe, telecom or network automation, cloud, enterprise delivery.
"""
from variants.general import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_VOIS"

TITLE = "AI Engineer — Generative AI, Agentic Automation & Python Services"

SUMMARY = (
    "AI engineer building Python services that combine dependable automation with LLMs: LangGraph agent workflows "
    "with tool calling, conditional routing and bounded retries, RAG with hybrid search and reranking, FastAPI APIs on "
    "PostgreSQL, Docker and CI. Builds responsible-AI controls in from the start: input and memory-write guardrails, a "
    "grounding check on every quoted price, Langfuse tracing for transparency, and evaluation before each change. On "
    "a 12,730-product assistant, a revised prompt raised task success from 7 to 12 of 12 with 29% fewer paid rerank "
    "calls; LoRA (PEFT) fine-tuning with PyTorch and Hugging Face, published. Native Arabic speaker; based in Giza."
)

SKILLS = [
    ("GenAI & Agentic Automation", "LangGraph and LangChain agents, tool calling, multi-step workflows with "
     "deterministic routing and bounded retries, retrieval-augmented generation (RAG), hybrid search (PostgreSQL "
     "full-text + pgvector), cross-encoder reranking, prompt engineering and versioning, structured output (Pydantic); "
     "Anthropic, OpenAI, Groq and Cohere APIs"),
    ("Responsible AI & Evaluation", "input and memory-write guardrails, grounding checks, Langfuse tracing and prompt "
     "management, code-graded evaluation, LLM-as-a-judge, RAGAS, labelled test sets with 95% confidence intervals, "
     "MLflow, DVC, Prometheus, Grafana"),
    ("Python Services", "Python, FastAPI (REST APIs), SQL, PostgreSQL, SQLAlchemy, Alembic, Git, Docker, Docker "
     "Compose, GitHub Actions (CI), pytest, Nginx, Gradio, Hugging Face Spaces"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA / PEFT fine-tuning, scikit-learn, "
     "XGBoost, pandas, NumPy, spaCy, NLTK"),
]
