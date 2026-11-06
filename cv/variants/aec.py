"""Junior AI Engineer — AEC (architecture, engineering & construction) technology company, Cairo preferred, remote,
Sun-Thu 9-5. Workable job 1777EB9BF8 (company name hidden as "Company"), posted 2026-07-08; Workable rate-limited the
open check on 2026-10-29. Asks: 2+ yrs AI/ML; AEC or construction-tech experience preferred; Python with PyTorch,
TensorFlow or scikit-learn; computer vision, LLMs and generative AI; BIM / Autodesk Revit a strong plus.
VISIONEER (text-to-floor-plan generation) leads because it is architecture-domain generative AI. Not claimed: BIM,
Revit, TensorFlow, construction-industry work.
"""
from variants.henkel_genai import *  # noqa: F401,F403
from variants.henkel_genai import PROJECTS as _HG_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_AEC_AI"

TITLE = "AI Engineer — Generative AI & Computer Vision for Architecture (Diffusion · LLMs · PyTorch)"

SUMMARY = (
    "AI engineer who applies generative AI to architecture: with a colleague, fine-tuned Stable Diffusion with LoRA "
    "on ~12k captioned floor plans to generate furnished 2D layouts from text, served to an Android AR app "
    "(published in Machine Graphics & Vision, 2025). Also builds LLM applications in Python: LangGraph agents with "
    "RAG and tool calling behind FastAPI REST APIs, with measured evaluation (on a 12,730-product assistant, "
    "reranking lifted right-product-first from 23% to 43%). Works in PyTorch, Hugging Face Diffusers and "
    "Transformers, and scikit-learn. Computer Science graduate based in Giza, open to remote work."
)

_shop, _visioneer, _research = _HG_PROJECTS
_visioneer = dict(_visioneer, tagline="Generative AI for architecture: text-to-floor-plan generation with AR (2024)")
PROJECTS = [_visioneer, _shop, _research]
