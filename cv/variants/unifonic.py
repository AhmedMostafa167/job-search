"""Unifonic — Tech Internship Program, Cairo 2026 (fresh graduates; software, data, AI/ML, QA, DevOps), on-site.
unifonic.com/en/careers/tech-internship-program-cairo-2026, HubSpot form on the page. Seen 2026-10-18.
Saudi-founded (2006) AI-native customer-experience platform; Agentic Studio = goal-driven AI agents over WhatsApp,
SMS, voice. Cairo office: Cairo Festival City, New Cairo. Lead with the customer-facing conversational agent,
its memory, guardrails, feedback and evaluation; mention native Arabic (MENA/GCC). No speech/voice claims.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Unifonic"

TITLE = "AI Engineer — Conversational AI Agents (LLMs · RAG · Evaluation)"

SUMMARY = (
    "AI engineer building customer-facing conversational agents end to end: tool-using LangGraph agents that "
    "remember each customer across conversations, retrieval over a real catalogue, and the guardrails, evaluation, "
    "tracing and monitoring that show whether each change helps. On a 12,730-product shopping assistant, raised "
    "agent task success from 7 to 12 of 12 tasks and right-product-ranked-first from 23% to 43%. Native Arabic "
    "speaker; published researcher and Computer Science teaching assistant."
)

SKILLS = [
    ("Conversational AI & Agents", "LangGraph, LangChain, agents and tool calling, multi-turn conversation state "
     "(Postgres checkpointer), long-term customer memory, prompt engineering and versioning, structured output "
     "(Pydantic), guardrails, retrieval-augmented generation (RAG), hybrid search, reranking, Groq, Cohere, Chroma"),
    ("Evaluation & Observability", "code-graded agent evaluation, LLM-as-a-judge, RAGAS, Langfuse (tracing, "
     "prompt management, user-feedback scores), MLflow, DVC, Prometheus, Grafana"),
    ("Backend & DevOps", "Python, FastAPI (REST APIs), SQL, PostgreSQL, SQLAlchemy, Alembic, Docker, Docker Compose, "
     "GitHub Actions (CI), pytest, Nginx, Gradio, Hugging Face Spaces"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA, scikit-learn, XGBoost, pandas, NumPy, "
     "spaCy, NLTK"),
]

_shop, _research, _visioneer = copy.deepcopy(_BASE_PROJECTS)
_shop["tagline"] = "Customer-facing conversational agent with long-term memory"
_shop["bullets"] = [
    "Built a LangGraph agent, served through a FastAPI API, that holds multi-turn shopping conversations over a "
    "12,730-product catalogue (hybrid search + Cohere reranking) and remembers each customer's lasting preferences "
    "across conversations as typed facts in PostgreSQL, separating them from one-off requests.",
    "Designed a code-graded agent evaluation (12 tasks × 3 runs, logged to Langfuse and MLflow): prompt v2 passed "
    "12 of 12 tasks vs 7 with 29% fewer paid searches; v3 moved price and rating limits inside search, lifting "
    "on-target results from 70% to 100%.",
    "Added input and memory-write guardrails tested with hostile tasks (0 of 21 legitimate facts refused) and a "
    "check that every price in a reply comes from search results (25 of 25 applicable runs).",
    "Traced conversations in Langfuse with customer feedback recorded as a score on the trace; monitored with "
    "Prometheus/Grafana; 104 pytest tests and GitHub Actions CI; reranking lifted right-product-first from 23% to 43%.",
]
PROJECTS = [_shop, _research, _visioneer]

COVER_LETTER = {
    "date": "18 October 2026",
    "to": ["Hiring Team, Unifonic", "Tech Internship Program, Cairo 2026 (AI/ML track)"],
    "greeting": "Dear Unifonic Hiring Team,",
    "paragraphs": [
        "I'm applying for the Tech Internship Program in Cairo, on the AI/ML track. Agentic Studio, with goal-driven "
        "agents that handle customer conversations across WhatsApp, SMS and voice for enterprises in Arabic-speaking "
        "markets, is the kind of system I've spent the past year learning to build, and I'd like to learn to build it "
        "at real scale alongside your engineers.",
        "My most recent project, a Shopping Assistant, is a customer-facing conversational agent. Built with LangGraph "
        "and served through a FastAPI API on PostgreSQL, it holds multi-turn conversations over a 12,730-product "
        "catalogue, searches it with hybrid retrieval and reranking, and remembers each customer's lasting "
        "preferences across conversations while leaving one-off requests out. On a labelled test set, reranking "
        "raised the right product to first place from 23% to 43% of the time.",
        "What I care about most is knowing whether an agent actually works. I built a code-graded evaluation of 12 "
        "tasks, each run 3 times: my first prompt passed 7 of them, and the revised version passed all 12 with 29% "
        "fewer paid searches. I added guardrails that I tested with hostile inputs, a check that every price in a "
        "reply comes from real search results (it passed in all 25 applicable runs), Langfuse tracing with customer "
        "feedback scored on each conversation, and 104 automated tests in CI.",
        "I graduated in Computer Science in June 2024, completed my military service from January 2025 to January "
        "2026, and since February 2026 I've been back as a Computer Science teaching assistant, a role in which I "
        "designed and led 50 lab sessions for more than 600 students in 2024. I also fine-tuned Stable Diffusion with "
        "LoRA in a project published in 2025. I'm a native Arabic speaker with professional English, which matters "
        "for conversational AI across MENA and the GCC.",
        "I'm based in Giza and available full-time. I'd welcome the chance to talk about how I could contribute to "
        "Agentic Studio. Thank you for your time and consideration.",
    ],
    "closing": "Sincerely,",
}
