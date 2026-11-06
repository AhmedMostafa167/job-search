"""Plata — Applied AI Engineer (AI Tools, CRM and other teams). Remote within GMT-2 to GMT+5, or relocation to a hub
(Cyprus, Serbia, Spain, Georgia, Kazakhstan). Greenhouse job 4822359008 on the platacard board, posted 2026-10-22,
seen 2026-10-24. Mexican digital bank (Plata Card).
Asks: experience in an ML role; agent frameworks or tool-using LLM systems; designing evaluations for LLM systems
(representative task sets, automated graders, production signals, human review); launching AI features from
scratch; A/B tests; data loops from real usage; English B1+. Bonus: quantitative degree, ML/NLP publications.
Lead with evaluation design and the two publications. No A/B tests on real users or production traffic claimed.
"""
import copy

from cv_content import *  # noqa: F401,F403
from cv_content import PROJECTS as _BASE_PROJECTS
from cv_content import SKILLS as _BASE_SKILLS

FILE_STEM = "Ahmed_Dorra_CV_Plata"

TITLE = "Applied AI Engineer — LLM Products, Agents & Evaluation Design"

SUMMARY = (
    "AI engineer who builds LLM products and designs the evaluations that decide what ships: labelled task sets "
    "with 95% confidence intervals, code-graded agent tests repeated across runs, guardrail checks and tracing. On "
    "a 12,730-product shopping assistant, measured hybrid retrieval at 72% top-10 recall vs 56% keyword and 41% "
    "vector, lifted right-product-first from 23% to 43% with reranking, and raised agent task success from 7 to 12 "
    "of 12 tasks. Two peer-reviewed publications (LoRA fine-tuning of Stable Diffusion; quantum machine learning) "
    "and a BSc in Computer Science."
)

SKILLS = [
    ("Evaluation & Experimentation", "evaluation design for LLM systems: labelled task sets, automated code "
     "graders, LLM-as-a-judge, RAGAS, 95% confidence intervals, stage-by-stage ablations, comparing prompt and "
     "pipeline versions on the same tasks, guardrail checks; Langfuse (tracing, prompt management, experiments), "
     "MLflow, DVC"),
    ("LLM Products & Agents", "LangGraph, LangChain, agents and tool calling, conversational memory, RAG with "
     "hybrid search (PostgreSQL full-text + pgvector, Reciprocal Rank Fusion), cross-encoder reranking, prompt "
     "engineering, structured output (Pydantic), Groq, Cohere, Chroma"),
    _BASE_SKILLS[3],
    _BASE_SKILLS[2],
]

PROJECTS = copy.deepcopy(_BASE_PROJECTS)
PROJECTS[0]["tagline"] = "Conversational product search, built and evaluated from scratch"
PROJECTS[0]["bullets"] = [
    "Built a LangGraph shopping agent from scratch over a 12,730-product catalogue: hybrid retrieval (PostgreSQL "
    "full-text + pgvector HNSW, Reciprocal Rank Fusion, Cohere reranking) and long-term memory of each customer's "
    "preferences.",
    "Defined what “good” meant for each stage and measured it on 127 labelled queries with 95% confidence "
    "intervals: hybrid top-10 recall 72% vs 56% keyword and 41% vector; reranking lifted right-product-first from "
    "23% to 43% (40-query subset); an HNSW index cut median vector search from 35 ms to 3.1 ms.",
    "Designed a code-graded agent evaluation (12 tasks × 3 runs, logged to Langfuse and MLflow): prompt v2 passed "
    "12 of 12 tasks vs 7 with 29% fewer paid rerank calls; moving price and rating limits inside search lifted "
    "matching results from 70% to 100% (57/81 → 48/48).",
    "Kept an improvement log of every measured change (before-and-after numbers and the decision taken); input and "
    "memory-write guardrails (0 of 21 legitimate facts refused), 104 automated tests and GitHub Actions CI.",
]

COVER_LETTER = {
    "date": "24 October 2026",
    "to": ["Hiring Team, Plata", "Applied AI Engineer (remote, GMT+2)"],
    "greeting": "Dear Plata Hiring Team,",
    "paragraphs": [
        "I'm applying for the Applied AI Engineer role. Of everything in the posting, the part I care about most is "
        "designing the evaluation: deciding what “good” means, how to measure it, and how to tell whether a change "
        "is real. That is where I've put most of my effort.",
        "My main project is a conversational shopping assistant over 12,730 products, built from scratch with a "
        "LangGraph agent, hybrid retrieval and long-term customer memory. I evaluated each stage separately. On 127 "
        "labelled queries, with 95% confidence intervals, hybrid search found the right product in the top 10 72% "
        "of the time, against 56% for keyword search and 41% for vector search. On a 40-query subset, reranking "
        "moved the right product to first place 43% of the time instead of 23%. For the agent, I wrote a "
        "code-graded test of 12 tasks run 3 times each: a revised prompt passed 12 of 12 against 7, with 29% fewer "
        "paid rerank calls. I logged every change, with its numbers and the decision it led to.",
        "I haven't yet worked in an ML role inside a company, or run A/B tests on live traffic. My evaluations used "
        "labelled data I built myself, which is the starting point for the data loops you describe. My research "
        "background, two peer-reviewed papers on LoRA fine-tuning and quantum machine learning, is where I learned "
        "to report results with their samples and limits.",
        "I'm based in Egypt (GMT+2), within your remote time-zone range, and I'm also open to relocating to one of "
        "your hubs. I'd welcome the chance to talk.",
    ],
    "closing": "Sincerely,",
}
