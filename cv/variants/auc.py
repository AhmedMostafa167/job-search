"""AUC (American University in Cairo) — Master of Science in Computer Science (thesis), Fall 2027 entry, with
fellowship applications (University Fellowship, Mohammed Bin Abdulkarim Allehedan Fellowship, Laboratory Instruction
Graduate Fellowship). Seen on LinkedIn 2026-10-28 (post about the Spring 2027 cycle, 7 Oct - 2 Nov 2026).
Academic CV: research, publications, teaching and evaluation rigour first; the industry framing is toned down.
The Allehedan fellowship asks for "relevant scientific research background", so the two papers lead.
"""
from cv_content import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_AUC"

TITLE = "Computer Science Graduate — Machine Learning, NLP & LLM Systems Research"

SUMMARY = (
    "Computer Science graduate (BSc, 2024) applying for graduate study in machine learning and natural language "
    "processing. Author of two peer-reviewed papers: LoRA fine-tuning of Stable Diffusion for floor-plan generation "
    "(Machine Graphics & Vision, 2025) and quantum denoising for brain-computer interfaces (Neurogenomics 2024). "
    "Builds and evaluates LLM systems with research rigour: labelled test sets with 95% confidence intervals, "
    "stage-by-stage ablations and a written log of every result. Computer Science teaching assistant who designed "
    "and led 50 lab sessions for 600+ students; native Arabic speaker interested in Arabic language technology."
)

from variants.aic import SKILLS  # noqa: E402,F401  (research-first skills order: DL & NLP, evaluation, data)
