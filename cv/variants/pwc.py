"""PwC Middle East — ETIC (Egypt Technology & Innovation Centre), "ETIC, AI Engineer - Associate" (Workday
752966WD), Cairo, Advisory / Technology. Posted 2026-08-18, still open on 2026-10-26 (canApply true). The posting
body is PwC's generic Associate text (feedback, collaboration, data handling, communication, networking); the
optional skills list is consulting-flavoured (business analysis, data analytics, research, CX strategy).
Second role at the same centre, same CV: "ETIC, Python Developer - Associate" (734201WD, posted 2026-07-07):
1+ yrs backend, Python and Django, APIs, Docker, cloud, LLM API integration. No Django, Azure or AWS claimed.
Built on the general variant; adds communication and documentation, which the Associate framework stresses.
"""
from variants.general import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_PwC"

TITLE = "AI Engineer — LLM Applications, Evaluation & Python Backends"

SUMMARY = (
    "AI engineer who builds AI products end to end in Python and explains them clearly: LLM applications (RAG, "
    "LangGraph agents and their evaluation), FastAPI services with tests, CI and monitoring, and model fine-tuning "
    "with PyTorch and Hugging Face. On a 12,730-product shopping assistant, raised right-product-ranked-first from "
    "23% to 43% and agent task success from 7 to 12 of 12 tasks, and kept a written log of every measured change. "
    "Computer Science teaching assistant (50 lab sessions for 600+ students), published researcher, and native "
    "Arabic speaker with professional English."
)

COVER_LETTER = {
    "date": "26 October 2026",
    "to": ["Hiring Team, PwC Egypt Technology & Innovation Centre (ETIC)", "AI Engineer – Associate, Cairo"],
    "greeting": "Dear ETIC Hiring Team,",
    "paragraphs": [
        "I'm applying for the AI Engineer – Associate role at ETIC. I'd like to build AI solutions that solve real "
        "client problems, and to work in a team that cares about explaining and measuring that work as much as "
        "building it.",
        "My main project is a Shopping Assistant over 12,730 products: a LangGraph agent with hybrid retrieval "
        "(PostgreSQL full-text search plus pgvector, fused and reranked) and long-term customer memory, served "
        "through a FastAPI API with 104 automated tests, GitHub Actions CI, and Langfuse, Prometheus and Grafana "
        "monitoring. I measured every change on labelled data. Hybrid search found the right product in the top 10 "
        "72% of the time, against 41% for vector search alone. Reranking moved it to first place 43% of the time "
        "instead of 23%. A revised prompt took the agent from 7 to 12 of 12 test tasks. I kept a written log of "
        "each result and the decision it led to, the kind of evidence a client can follow.",
        "Communication is the other half of the Associate role, and it's where my teaching helps. As a Computer "
        "Science teaching assistant I designed and led 50 lab sessions for more than 600 students, and I've "
        "published two peer-reviewed papers, on LoRA fine-tuning and quantum machine learning.",
        "I hold a BSc in Computer Science (2024), completed my military service, and live in Giza. I'd welcome the "
        "chance to discuss how I could contribute to ETIC's AI work.",
    ],
    "closing": "Sincerely,",
}
