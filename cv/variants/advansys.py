"""Advansys Intelligent Solutions — AI Software Engineer, Nasr City, hybrid, full-time. LinkedIn Easy Apply.
Seen 2026-10-18 (posted ~1 month earlier, 100+ applicants). Advansys ESC (INTRO Group), Nasr City Free Zone.
Asks: 2+ yrs professional software dev, OOD/microservices, Python + Node/Java/C#, LLM APIs, RAG, LangChain/PyTorch,
SQL + pgvector/Chroma, Azure AI/AWS Bedrock, CI/CD; industrial use cases (predictive maintenance, anomaly detection).
Same core asks as Raya, so reuse its framing. No Node/Java/C#, Azure or AWS claimed.
"""
from variants.raya import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_Advansys"

TITLE = "AI Software Engineer — LLM Integration, RAG & Production Python"

SUMMARY = (
    "AI engineer integrating LLMs into production-style software in Python: RAG pipelines over PostgreSQL and "
    "pgvector with hybrid search and reranking, LangGraph agents served through FastAPI APIs, and the tests, CI, "
    "monitoring and documentation around them. On a 12,730-product shopping assistant, raised right-product-ranked-"
    "first from 23% to 43% and agent task success from 7 to 12 of 12 tasks, and cut median vector-search latency "
    "from 35 ms to 3.1 ms. Computer Science teaching assistant used to training others; published researcher."
)

COVER_LETTER = {
    "date": "18 October 2026",
    "to": ["Hiring Team, Advansys Intelligent Solutions", "AI Software Engineer, Nasr City"],
    "greeting": "Dear Advansys Hiring Team,",
    "paragraphs": [
        "I'm applying for the AI Software Engineer position in Nasr City. The role joins modern AI, from LLMs to "
        "predictive analytics, with scalable software engineering, and that combination is what I've focused on: "
        "building LLM features and then making them testable, measurable and maintainable.",
        "My main project is a Shopping Assistant over a 12,730-product catalogue. Its RAG pipeline combines "
        "PostgreSQL full-text search with pgvector, fuses the results and reranks them, and a LangGraph agent serves "
        "it through a FastAPI API. On 127 labelled queries, hybrid retrieval found the right product in the top 10 "
        "72% of the time, against 56% for keyword search and 41% for vector search alone; on a 40-query subset, "
        "reranking lifted the right product to first place from 23% to 43%; and an HNSW index cut median "
        "vector-search latency from 35 ms to 3.1 ms. The service runs in Docker Compose with 104 automated tests, "
        "GitHub Actions CI and Prometheus and Grafana monitoring, and I documented its architecture, API and "
        "evaluation results.",
        "Most of my engineering so far has been on my own projects rather than inside a company, but I've held them "
        "to production standards: every change was measured before it was kept. As a Computer Science teaching "
        "assistant I designed and led 50 lab sessions for more than 600 students, which is close to the part of the "
        "role that trains staff on AI-assisted workflows. Industrial use cases such as predictive maintenance would "
        "be new to me, though I have worked with noisy time-series signals: as a research intern I built a quantum "
        "machine-learning pipeline that denoised and classified EEG data.",
        "I hold a BSc in Computer Science (2024), completed my military service in January 2026, and live in Giza, "
        "so a hybrid role in Nasr City works well for me. I'd welcome the chance to discuss how I could contribute.",
    ],
    "closing": "Sincerely,",
}
