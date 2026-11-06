"""Finalyze — Machine Learning Intern (Arabic Natural Language Processing). Cairo-based financial-data startup
(AUC Venture Lab graduate) extracting Arabic financial statements from the Egyptian Exchange. Wuzzuf, posted
2026-10-25, seen 2026-10-26. 12 weeks from November 2026, 15-20 h/week, fully remote, UNPAID.
Work: measure how accurately the LLMs behind their extraction read Arabic financial statements (Eastern Arabic
numerals), compare models' accuracy and cost per statement, build an evaluation set from verified pages, and a
sentiment score per listed company (ingestion, labelled dataset, baseline model). Write a one-page plan first;
every result rerunnable from a notebook; CTO reviews every change.
Asks: recent graduate OK; reads Arabic fluently; trained a text classifier; measured model output against labelled
data (precision/recall); Python and notebooks.
Built on the AIC variant (research and evaluation rigour, Arabic). Text-classifier experience is coursework only
(DeepLearning.AI NLP Specialization), so it is not claimed as project work. No OCR claimed.
"""
from variants.aic import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_Finalyze"

TITLE = "Machine Learning — LLM Evaluation & Arabic NLP"

SUMMARY = (
    "Computer Science graduate who measures language models carefully: labelled evaluation sets, 95% confidence "
    "intervals, stage-by-stage comparisons and a written log of every result, so each change is judged on numbers "
    "and can be rerun. On a 12,730-product search system, measured hybrid retrieval at 72% top-10 recall vs 56% "
    "keyword and 41% vector, and tracked accuracy against cost (a revised prompt passed 12 of 12 test tasks instead "
    "of 7 with 29% fewer paid rerank calls). Native Arabic speaker; published researcher; Python, PyTorch and "
    "Hugging Face."
)
