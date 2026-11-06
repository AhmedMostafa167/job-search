"""General CV: LLM applications, RAG and agents (for AI Engineer / GenAI / Agentic AI posts with no specific variant)."""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _G

FILE_STEM = "Ahmed_Dorra_CV_General_LLM_Agents"
TITLE = "AI Engineer — LLM Agents, RAG & Evaluation (LangGraph · FastAPI · Python)"
SUMMARY = (
    "AI engineer who builds LLM applications end to end: hybrid-search RAG, tool-using agents with long-term memory, "
    "and the evaluation, guardrails and monitoring that show whether each change works. On a 12,730-product "
    "shopping assistant, raised right-product-ranked-first from 23% to 43% and agent task success from 7 to 12 of 12 "
    "tasks. Mentors AI and MLOps learners, teaches Computer Science to 700+ students, and is a published researcher. "
    "Native Arabic speaker; open to relocation and remote work."
)
PROJECTS = copy.deepcopy(_G)
