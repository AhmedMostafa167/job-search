"""Capgemini Egypt (Cairo AI Hub) — AI & Automation Engineer (ref 587989, updated 2026-10-29) and AI Automation Test
Engineer (ref 488387, updated 2026-10-28). Both from cg-jobstream-api (country_code eg-en); apply via
careers.capgemini.com. One CV covers both.
AI & Automation asks: 1+ yr; conversational AI and virtual agents (Copilot Studio, Power Platform, Power Automate);
integrations with ServiceNow/ITSM, REST APIs, JSON, auth, webhooks; deploy on Azure; CI/CD, Git, ALM across
DEV/QA/UAT/Prod; functional and integration testing; L3 support; documentation.
Test asks: 2-6 yrs test automation (Selenium/Playwright/Cypress, Java/Python, Postman); API, regression and CI testing;
AI/GenAI exposure a plus.
Not claimed: Copilot Studio, Power Platform/Automate, Azure, ServiceNow, PowerShell, JavaScript, Selenium, Postman.
"""
from variants.vois import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_Capgemini"

TITLE = "AI Engineer — Conversational AI, API Integrations, CI/CD & Automated Testing"

SUMMARY = (
    "AI engineer who builds conversational AI agents and takes them from development to tested, monitored "
    "deployment: a LangGraph chatbot agent with tool calling and RAG, integrated through a FastAPI REST API with "
    "JSON schemas validated by Pydantic, packaged with Docker and shipped through GitHub Actions CI. Tests "
    "everything: 104 automated pytest tests, a code-graded agent evaluation (12 tasks × 3 runs) re-run after "
    "each change. On a 12,730-product assistant, a revised prompt raised task success from 7 to 12 "
    "of 12 with 29% fewer paid rerank calls. Writes clear documentation; Computer Science teaching assistant; "
    "native Arabic speaker with professional English."
)

SKILLS = [
    ("Conversational AI & Agents", "LangGraph and LangChain agents, chatbots with tool calling and conversational "
     "memory, retrieval-augmented generation (RAG), hybrid search (PostgreSQL full-text + pgvector), reranking, "
     "prompt engineering and versioning, structured output (Pydantic), guardrails; Anthropic, OpenAI, Groq, Cohere"),
    ("Integration & Deployment", "Python, FastAPI (REST APIs, JSON), SQL, PostgreSQL, SQLAlchemy, Alembic, Git, "
     "GitHub Actions (CI), Docker, Docker Compose, Nginx, Hugging Face Spaces"),
    ("Testing & Quality", "pytest (unit and integration tests), code-graded evaluation, measured comparisons on "
     "labelled test sets with 95% confidence intervals, LLM-as-a-judge, RAGAS, Langfuse tracing, Prometheus, "
     "Grafana, MLflow"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA fine-tuning, scikit-learn, XGBoost, "
     "pandas, NumPy, spaCy, NLTK"),
]
