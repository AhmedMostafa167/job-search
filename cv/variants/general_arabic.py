"""General CV: Arabic NLP / MENA-GCC AI roles (leads with the Arabic intent classifier)."""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _G

FILE_STEM = "Ahmed_Dorra_CV_General_Arabic_NLP"
TITLE = "AI Engineer — Arabic NLP, LLM Applications & Model Serving (AraBERT · RAG · FastAPI)"
SUMMARY = (
    "AI engineer and native Arabic speaker who builds Arabic and multilingual NLP systems: a fine-tuned AraBERT "
    "intent classifier (macro-F1 0.919, with dialect-level results on Saudi, Moroccan and Tunisian), served as ONNX "
    "behind a monitored FastAPI API, plus LLM agents and RAG with measured evaluation. Teaches Computer Science and "
    "mentors AI learners across the MENA region. Open to relocation to the Gulf and remote work."
)
PROJECTS = copy.deepcopy(_G)
