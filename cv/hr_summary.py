"""HR-first summary, applied to every CV at build time (Ahmed's request, Nov 2026).

The first reader is usually HR with no technical background, so the summary leads with how Ahmed works with people
(teaching 700+ students, mentoring the MLOps MENA community) and keeps the technical proof to one closing clause.
Wording matches the CVs Ahmed approved in Drive (Resume/"CVs 2026-11-24 (new summary, links, email)").

Shape: <opening> <SOFT> <TEAM>, backed by <backing>.[ <tail>]
Defaults are picked from the variant's TITLE; MODULE_OVERRIDES pins exact wording for the general CVs and a few
variants. (Overrides live here, not in the variant files, because variants `import *` from each other.)
"""
import re

SOFT = ("Teaching 700+ students and mentoring the MLOps MENA community has meant breaking hard topics into clear "
        "steps, adapting the explanation for engineers, managers and non-technical colleagues, and giving feedback "
        "that moves people forward.")
TEAM = "On a team, that shows up as smoother handoffs, faster onboarding and decisions stakeholders can follow"

# (pattern on TITLE or module name, opening verb phrase, backing)
PROFILES = [
    (r"Arabic", "who builds Arabic NLP systems and explains them to any team.",
     "a fine-tuned AraBERT intent classifier (macro-F1 0.919, with Saudi, Moroccan and Tunisian dialect results) "
     "served as ONNX behind a monitored FastAPI API"),
    (r"Data Scien|Data Analy|Analyst", "who turns model results into clear decisions for technical and non-technical "
     "teams.",
     "labelled test sets with 95% confidence intervals, honest baselines and published research (an AraBERT "
     "classifier at 0.919 macro-F1 vs a 0.887 TF-IDF baseline)"),
    (r"Data Engineer", "who builds reliable data pipelines and explains them clearly to any team.",
     "hands-on experience with pandas ingestion from five file formats, row-level validation, PostgreSQL, Docker "
     "and CI with 104 automated tests"),
    (r"Test|QA", "who tests software carefully and explains issues clearly to any team.",
     "hands-on experience with 104 automated tests, CI pipelines and evaluations re-run after every change"),
    (r"Instructor|Trainer|Mentor|Teach|Tutor", "who turns complex AI topics into clear, practical lessons.",
     "hands-on experience building, deploying and evaluating LLM and ML systems, and two published research papers"),
    (r"MLOps|Machine Learning|ML Engineer|AI / ML|ML Software|Model", "who builds and runs ML systems and makes them "
     "clear to everyone on the team.",
     "hands-on experience fine-tuning, serving and monitoring models (an AraBERT classifier served as ONNX behind a "
     "monitored FastAPI API with a promotion gate and drift alert)"),
    (r"Agent|LLM|RAG|GenAI|Generative|Prompt|Conversational", "who builds LLM agents and RAG systems, and makes them "
     "clear to everyone on the team.",
     "hands-on experience with hybrid-search RAG, tool-using agents and measured evaluation (right product ranked "
     "first from 23% to 43%; agent task success from 7 to 12 of 12)"),
    (r"Backend|Software|Developer|Python|Full", "who builds reliable software and explains it clearly to any team.",
     "hands-on experience building FastAPI services on PostgreSQL with Docker, CI and 104 automated tests, and "
     "adding AI features to them"),
    (r"Research", "who researches and builds AI systems and explains them clearly to any team.",
     "two published research papers and hands-on experience building and evaluating LLM and ML systems"),
]
DEFAULT = ("who turns complex systems into something every team can understand and use.",
           "hands-on experience building and deploying production LLM and ML systems, and a habit of testing ideas "
           "with evidence")


MODULE_OVERRIDES = {  # module: (opening or None, backing or None, tail)
    "cv_content": ("AI Engineer " + DEFAULT[0], DEFAULT[1], ""),
    "variants.general": ("AI Engineer " + DEFAULT[0], DEFAULT[1], ""),
    "variants.general_arabic": ("Native Arabic-speaking AI Engineer who builds Arabic NLP systems and explains them "
                                "to any team.", None, "Open to relocation to the Gulf."),
    "variants.general_graduate": ("Junior AI Engineer who ships tested projects and explains them clearly to any "
                                  "team.",
                                  "shipped projects: a LangGraph shopping assistant with hybrid RAG and evaluation "
                                  "(agent task success from 7 to 12 of 12), a fine-tuned Arabic AraBERT classifier "
                                  "served as ONNX, and published research on LoRA fine-tuning and quantum machine "
                                  "learning", "Open to relocation with visa sponsorship."),
    "variants.finalyze": ("Machine Learning intern candidate who builds Arabic NLP systems and explains them to any "
                          "team.", None, ""),
    "variants.cib": ("AI Engineer who builds AI services for real customers and explains them clearly to any team.",
                     "a fine-tuned Arabic banking-intent classifier (77 intents, macro-F1 0.919) served behind a "
                     "monitored API with a drift alert, and production-style RAG services with tests, CI and "
                     "monitoring", ""),
}


def _role(title):
    role = re.split(r"\s+[—–-]\s+|,|\(", title or "AI Engineer")[0].strip()
    return role or "AI Engineer"


def apply(module):
    name = getattr(module, "__name__", "")
    title = getattr(module, "TITLE", "")
    key = title + " " + getattr(module, "__name__", "")
    opening_tail, backing = DEFAULT
    for pat, o, b in PROFILES:
        if re.search(pat, title, re.I) or (pat == r"Arabic" and re.search(pat, key, re.I)):
            opening_tail, backing = o, b
            break
    opening, tail = f"{_role(title)} {opening_tail}", ""
    if name in MODULE_OVERRIDES:
        o, b, t = MODULE_OVERRIDES[name]
        opening, backing, tail = o or opening, b or backing, t
    module.SUMMARY = f"{opening} {SOFT} {TEAM}, backed by {backing}." + (f" {tail}" if tail else "")
