"""General CV: instructor / mentor / teaching-heavy AI roles."""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _G

FILE_STEM = "Ahmed_Dorra_CV_General_AI_Instructor"
TITLE = "AI Instructor & Mentor — Machine Learning, MLOps and LLM Applications"
SUMMARY = (
    "Computer Science teaching assistant and AI mentor: teaches Advanced Operating Systems to 700+ students and a "
    "starter MLOps course to about 500, designed and led 50 Compiler Theory labs for 600+ students, and mentors "
    "learners in the MLOps MENA community. Builds the systems he teaches: LLM agents with RAG, a fine-tuned Arabic "
    "classifier, and monitored FastAPI services. Native Arabic speaker with professional English."
)
PROJECTS = copy.deepcopy(_G)
