"""General CV: graduate / junior programmes and internships (skills first, short and plain)."""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _G

FILE_STEM = "Ahmed_Dorra_CV_General_Junior_Graduate"
TITLE = "Junior AI Engineer — Python, Machine Learning, LLM Applications"
SUMMARY = (
    "Junior AI engineer with Computer Science training and shipped projects: a LangGraph shopping assistant with "
    "hybrid RAG and evaluation (agent task success 7 to 12 of 12), a fine-tuned Arabic AraBERT classifier served as "
    "ONNX, and published research on LoRA fine-tuning and quantum machine learning. Teaches Computer Science to 700+ "
    "students and mentors learners in the MLOps MENA community. Native Arabic speaker; open to relocation, "
    "visa sponsorship and remote work."
)
PROJECTS = copy.deepcopy(_G)
