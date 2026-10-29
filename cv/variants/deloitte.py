"""Deloitte Egypt — Deloitte Innovation Hub (DIH), AI & Data team, Technology & Transformation, Cairo. General
tailoring for Deloitte (referral or any DIH AI role), requested by Ahmed 2026-10-29. Open DIH Cairo AI postings on
middleeastjobs.deloitte.com then: Senior AI/ML Engineer (257268, 3-7 yrs), AI/ML Tech Leads (257269, 257270),
Decision Intelligence Engineer (243928, 0-3 yrs, supply chain); the entry-level AI & Data Engineer career-fair
postings (246858, 252988) were closed.
Their asks: full data-science lifecycle from PoC to tested production; data collection, cleaning, feature
engineering; training, testing, evaluating and fine-tuning models with the right metrics; technical documentation;
client pain points, communicating solutions, proposals; PyTorch or TensorFlow; deployment; Matplotlib/Seaborn,
Tableau or Power BI. Consulting framing: business problem → measured solution → clear explanation.
Not claimed: client or consulting engagements, TensorFlow, Tableau, Power BI, Matplotlib/Seaborn, cloud.
"""
from variants.general import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_Deloitte"

TITLE = "AI & Data Engineer — Machine Learning, Generative AI & Data Solutions"

SUMMARY = (
    "AI engineer who takes data and AI solutions through the whole lifecycle, from proof of concept to a tested, "
    "deployed service: data collection and cleaning with validation, model fine-tuning with PyTorch and Hugging Face, "
    "LLM applications with RAG and agents, and evaluation with the right metrics on labelled data before anything "
    "ships. On a 12,730-product assistant, hybrid retrieval reached 72% top-10 recall vs 41% for vector search alone, "
    "and reranking lifted the right answer to first place from 23% to 43%. Documents and explains results clearly: as "
    "a teaching assistant, led 50 lab sessions for 600+ students. Two peer-reviewed publications; native Arabic, "
    "professional English; based in Giza."
)

SKILLS = [
    ("Machine Learning & Data Science", "PyTorch, Hugging Face Transformers, Diffusers, LoRA fine-tuning, "
     "scikit-learn, XGBoost, pandas, NumPy, data cleaning and row-level validation (Pydantic), feature preparation, "
     "spaCy, NLTK"),
    ("Generative AI", "LLM applications, retrieval-augmented generation (RAG), hybrid search (PostgreSQL full-text + "
     "pgvector), cross-encoder reranking, LangGraph and LangChain agents, tool calling, prompt engineering, "
     "structured output, guardrails; Anthropic, OpenAI, Groq and Cohere APIs"),
    ("Evaluation & MLOps", "labelled test sets with 95% confidence intervals, stage-by-stage comparisons, "
     "code-graded evaluation, LLM-as-a-judge, RAGAS, MLflow, DVC, Langfuse, Prometheus, Grafana"),
    ("Engineering & Deployment", "Python, SQL, PostgreSQL, FastAPI (REST APIs), SQLAlchemy, Alembic, Git, Docker, "
     "Docker Compose, GitHub Actions (CI), pytest, Gradio, Hugging Face Spaces"),
]
