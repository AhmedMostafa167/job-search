"""General CV: ML / MLOps engineer (training, evaluation, serving, monitoring)."""
import copy

from variants.general import *  # noqa: F401,F403
from variants.general import PROJECTS as _G, SKILLS as _S

FILE_STEM = "Ahmed_Dorra_CV_General_ML_MLOps"
TITLE = "ML Engineer — Model Training, Serving & MLOps (PyTorch · FastAPI · MLflow · Docker)"
SUMMARY = (
    "ML engineer who takes models from training to a monitored service: fine-tuning with PyTorch and Hugging Face, "
    "evaluation with confidence intervals and promotion gates, experiment tracking with MLflow and DVC, FastAPI "
    "services in Docker, GitHub Actions CI with automated tests, and Prometheus/Grafana monitoring. Teaches a "
    "starter MLOps course to about 500 students and mentors learners in the MLOps MENA community. Native Arabic "
    "speaker; open to relocation and remote work."
)
SKILLS = [_S[1], _S[2], _S[3], _S[0]]
PROJECTS = copy.deepcopy(_G)
