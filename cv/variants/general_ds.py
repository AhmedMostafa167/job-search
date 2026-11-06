"""General CV: data scientist / junior ML (analysis, modelling, evaluation, communication)."""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _G

FILE_STEM = "Ahmed_Dorra_CV_General_Data_Scientist"
TITLE = "Data Scientist — Machine Learning, NLP & Evaluation (Python · SQL · PyTorch · scikit-learn)"
SUMMARY = (
    "Data scientist who builds and measures models: labelled test sets with 95% confidence intervals, honest "
    "baselines, and clear write-ups of what worked. Fine-tuned an Arabic AraBERT classifier (macro-F1 0.919 vs a "
    "0.887 TF-IDF baseline), compared retrieval methods on 127 labelled queries, and published LoRA fine-tuning "
    "and quantum machine-learning research. Python, SQL, pandas, scikit-learn, XGBoost and PyTorch. Teaches "
    "Computer Science and a starter MLOps course to hundreds of students. Native Arabic speaker."
)
SKILLS = [
    ("Data & Modelling", "Python, SQL, pandas, NumPy, scikit-learn, XGBoost, PyTorch, Hugging Face Transformers, "
     "spaCy, NLTK, feature engineering, model evaluation, statistics (confidence intervals, paired bootstrap)"),
    ("NLP & LLMs", "AraBERT fine-tuning, LoRA, retrieval-augmented generation (RAG), hybrid search, reranking, "
     "prompt engineering, LLM-as-a-judge, RAGAS"),
    ("Tracking & Deployment", "MLflow, DVC, FastAPI, Docker, GitHub Actions (CI), pytest, Prometheus, Grafana, Git"),
]
PROJECTS = copy.deepcopy(_G)
