"""KAISPE — AI Engineer (fresh graduates). Email areeba.anwar@kaispe.com, subject "AI Engineer". Seen 2026-10-16.
Microsoft Dynamics / Power Platform partner (est. 2017), offices: Arlington Heights IL + Karachi. Location not stated.
Asks: GenAI, LLMs, AI agents, agentic AI. Base CV with agentic-first framing.
"""
from cv_content import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_KAISPE"

TITLE = "AI Engineer — Generative AI & Agentic Systems (LLMs · Agents · RAG)"

SUMMARY = (
    "AI engineer building generative-AI applications end to end: agentic workflows and tool-using agents with "
    "long-term memory, RAG with hybrid search, and the evaluation, guardrails and monitoring that show whether each "
    "change works. On a 12,730-product shopping assistant, raised agent task success from 7 to 12 of 12 tasks and "
    "right-product-ranked-first from 23% to 43%. Published researcher (LoRA fine-tuning of Stable Diffusion; quantum "
    "machine learning) and Computer Science teaching assistant."
)

SKILLS = [
    ("Generative AI & Agents", "LLMs, agentic AI, LangGraph, LangChain, agents and tool calling, multi-step "
     "workflows with conditional routing, conversational memory, retrieval-augmented generation (RAG), hybrid "
     "search (PostgreSQL full-text + pgvector, Reciprocal Rank Fusion), cross-encoder reranking, prompt engineering, "
     "structured output (Pydantic), Chroma, Groq, Cohere"),
    *SKILLS[1:],
]
