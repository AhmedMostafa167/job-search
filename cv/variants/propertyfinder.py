"""Property Finder — Associate AI Product Builder (reports to Head of Product). Dubai, on the ground: "Dubai-based or
genuinely ready to move". LinkedIn job 4476322990, posted 2026-10-24. MENA's leading property portal (since 2007).
Asks: something you built that people used (link + five lines: what it is, who used it, what broke), building with
AI coding agents as a habit, getting your own data, funnel maths and statistics, end-to-end ownership, going to
market. Nice: coding, design fluency, STEM degree. Process: send the thing, 45-min problem interview, hometask
(prototype + one-pager), bar raiser.
Honest framing: the Shopping Assistant was evaluated on labelled data, not used by real customers; the Research
Assistant is a live public demo. Native Arabic helps across Dubai, Cairo and Riyadh.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_PropertyFinder"

TITLE = "AI Product Builder — Working Prototypes, Data & Measured Results"

SUMMARY = (
    "Builder who ships working AI prototypes and measures them before arguing for them. Built a conversational "
    "shopping assistant over 12,730 products and tested every change on labelled data: hybrid search found the "
    "right product in the top 10 72% of the time vs 56% for keyword search, reranking put it first in 43% of "
    "queries instead of 23%, and a prompt rewrite took the agent from 7 to 12 of 12 tasks. Prototypes with AI "
    "coding agents as a habit; pulls and analyses data directly with SQL and pandas. Native Arabic speaker with "
    "professional English, ready to relocate to Dubai."
)

SKILLS = [
    ("Building with AI", "prototyping with AI coding agents (Claude), LLM agents and tool calling (LangGraph, "
     "LangChain), retrieval-augmented generation (RAG), prompt engineering and versioning, structured output, "
     "Groq, Cohere, Anthropic and OpenAI APIs, Gradio demos on Hugging Face Spaces"),
    ("Data & Measurement", "SQL, PostgreSQL, pandas, NumPy, labelled test sets, 95% confidence intervals, "
     "stage-by-stage measurement, comparing versions on the same tasks, Langfuse, MLflow"),
    ("Engineering", "Python, FastAPI, pgvector, Docker, Docker Compose, Git, GitHub Actions (CI), pytest, "
     "Prometheus, Grafana"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA, scikit-learn, XGBoost"),
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "Conversational product search: built, measured, fixed"
PROJECTS[0]["bullets"] = [
    "Built a shopping assistant that answers in plain language over a 12,730-product catalogue, remembers each "
    "customer's lasting preferences, and combines keyword and vector search (PostgreSQL + pgvector) with reranking.",
    "Found what broke by measuring it: vector search alone found the right product in the top 10 only 41% of the "
    "time (keyword 56%); combining them reached 72% on 127 labelled queries, and reranking lifted right-product-"
    "first from 23% to 43%.",
    "The first agent prompt passed 7 of 12 test tasks; the rewrite passed 12 of 12 with 29% fewer paid reranking "
    "calls. "
    "When about 30% of results still broke the customer's price or rating limits, moving those limits inside search "
    "made 100% of results match.",
    "Kept an improvement log of every change with before-and-after numbers; 104 automated tests, CI and dashboards.",
]
PROJECTS[1]["bullets"][0] = (
    "Designed a self-correcting research agent over arXiv and the web (query rewriting, relevance grading, cited "
    "answers, a reflection step with a bounded retry) and built it with an AI coding agent; live public demo on "
    "Hugging Face Spaces."
)
