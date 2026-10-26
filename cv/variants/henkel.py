"""Henkel — AI Engineer (corporate functions, digital), New Cairo, hybrid. Cornerstone requisition 86074, posted
2026-01-07, still open 2026-10-26. A second "AI Engineer" requisition (89184, GenAI models, 3-4 yrs, TensorFlow,
diffusion, C#/.NET, Power BI) is a worse fit and is skipped.
Asks (86074): 2-3 yrs; agentic LLM apps (tool calling, routing, multi-step orchestration) and RAG over enterprise
documents; define evaluation criteria (accuracy, groundedness, cost, latency) before building; NL-to-SQL / BI
integration; Teams/chat/voice interfaces; LangGraph/LangChain; async FastAPI, Pydantic, uv; Terraform; CI/CD; Azure;
responsible AI, governance, monitoring. Nice: Teams bots, MCP, SAP BTP.
Same core as Deeplight, so reuse it. No Azure, Terraform, uv, Teams bots, MCP, NL-to-SQL or SAP claimed.
"""
from variants.deeplight import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_Henkel"

TITLE = "AI Engineer — Agentic LLM Applications & RAG (LangGraph · FastAPI · Evaluation)"

SUMMARY = (
    "AI engineer building agentic LLM applications in Python: LangGraph agents with tool calling and conditional "
    "routing, RAG with hybrid search and reranking, FastAPI services with Pydantic-validated structured outputs, and "
    "CI, tracing and monitoring around them. Defines how a feature will be judged before building it, then measures "
    "accuracy, groundedness, cost and latency: on a 12,730-product assistant, agent task success rose from 7 to 12 "
    "of 12 with 29% fewer paid rerank calls, a grounding check confirmed quoted prices in 25 of 25 runs, and an HNSW "
    "index cut median search latency from 35 ms to 3.1 ms. Computer Science teaching assistant, used to working with "
    "non-technical audiences."
)

COVER_LETTER = None
