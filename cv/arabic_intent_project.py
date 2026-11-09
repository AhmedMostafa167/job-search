"""The Arabic banking intent project (github.com/AhmedMostafa167/arabic_banking_intent), added to every CV at build time.

Numbers come from that repo's README (checked 4 Nov 2026). The README's laptop remark is left out on purpose.
Full entry for ML/MLOps/Arabic/data roles; short entry for LLM-agent roles, where the agent projects keep the lead.
A variant can override this with ARABIC_INTENT_FULL (bool) and ARABIC_INTENT_POSITION (0 = first project).
VISIONEER is dropped from the Projects section (the paper stays under Publications).
"""
import copy
import re

LINKS = [("GitHub", "https://github.com/AhmedMostafa167/arabic_banking_intent"),
         ("Model", "https://huggingface.co/Ahmed167/arabert-arbanking77-intents")]
STACK = ("Python · PyTorch · Hugging Face Transformers · ONNX Runtime · FastAPI · MLflow · DVC · Docker · "
         "Prometheus · Grafana · Locust · GitHub Actions")

FULL = {
    "name": "Arabic Banking Intent Classifier",
    "tagline": "AraBERT fine-tuning with a production-style MLOps pipeline",
    "links": LINKS, "stack": STACK,
    "bullets": [
        "Fine-tuned AraBERT to classify Arabic banking messages into 77 intents (ArBanking77, SinaLab): validation "
        "macro-F1 0.919 vs 0.887 for a TF-IDF baseline, and 0.843 / 0.779 / 0.599 on Saudi, Moroccan and Tunisian "
        "dialects never seen in training (baseline 0.719 / 0.612 / 0.499).",
        "Found that the official validation split leaks paraphrases (scores inflated by about 3 points) and built a "
        "grouped split; a paired-bootstrap promotion gate in the MLflow model registry decided which model to serve.",
        "Served it as ONNX fp16 from a FastAPI container without PyTorch (image 2.26 GB to 0.95 GB, median latency "
        "670 to 530 ms on CPU), load-tested with Locust, with Prometheus/Grafana dashboards and a drift alert that "
        "fired on unseen-dialect traffic. Published with a model card on the Hugging Face Hub.",
    ],
}
SHORT = copy.deepcopy(FULL)
SHORT["bullets"] = [
    "Fine-tuned AraBERT on 77 Arabic banking intents (macro-F1 0.919 vs 0.887 for TF-IDF; 0.843 vs 0.719 on an unseen "
    "dialect), fixed a leaky validation split, gated promotion in the MLflow registry, and served it as ONNX fp16 "
    "behind FastAPI in Docker (image 2.26 GB to 0.95 GB) with Prometheus/Grafana monitoring.",
]
FOCUS_FULL = re.compile(r"MLOps|Machine Learning|ML Engineer|AI / ML|Data Scien|NLP|Arabic|Model|Instructor", re.I)
ML_SKILL = re.compile(r"MLOps|Machine Learning|Evaluation|ML\b", re.I)
SKILL_ADD = "Arabic NLP (AraBERT), ONNX Runtime, MLflow model registry"


def apply(module):
    projects = [p for p in module.PROJECTS if p["name"] != "VISIONEER"]
    full = getattr(module, "ARABIC_INTENT_FULL", None)
    if full is None:
        full = bool(FOCUS_FULL.search(getattr(module, "TITLE", "")))
    entry = copy.deepcopy(FULL if full else SHORT)
    default_pos = 1 if full else 2
    projects.insert(min(getattr(module, "ARABIC_INTENT_POSITION", default_pos), len(projects)), entry)
    module.PROJECTS = projects
    skills = list(module.SKILLS)
    for i, (k, v) in enumerate(skills):
        if ML_SKILL.search(k) and SKILL_ADD not in v:
            skills[i] = (k, v + "; " + SKILL_ADD)
            break
    module.SKILLS = skills
