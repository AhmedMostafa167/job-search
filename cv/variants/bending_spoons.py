"""Bending Spoons — Graduate AI Software Engineer (LinkedIn 4482911009 / 4482688951; Milan, London, Madrid, Warsaw;
relocation package). Asks: build AI-powered product features from idea to production; use AI tools across design,
implementation, testing and docs; end-to-end ownership across stacks; simplify relentlessly; reasoning ability,
drive, team spirit, English. The CV row uses the general CV; this variant exists for the cover letter.
Not claimed: Rust, gRPC, Kubernetes, microservices at scale.
"""
from variants.general import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_BendingSpoons"

COVER_LETTER = {
    "date": "8 November 2026",
    "to": ["Bending Spoons Talent Team", "Graduate AI Software Engineer — Milan, London, Madrid or Warsaw"],
    "greeting": "Dear Bending Spoons Team,",
    "paragraphs": [
        "I'm applying for the Graduate AI Software Engineer role. You describe the job as taking AI features from "
        "possibility to production and judging them by whether they hold up for real users. That is how I've "
        "built my own projects, and I'd like to do it on products used by millions.",
        "My main project is a Shopping Assistant: a tool-calling LangGraph agent that searches a 12,730-product "
        "catalogue with hybrid retrieval (PostgreSQL full-text plus pgvector, then reranking), remembers each "
        "customer's lasting preferences as typed facts in PostgreSQL, and runs as a FastAPI service with Docker, "
        "104 automated tests in CI, and Prometheus and Grafana monitoring. I owned it end to end, from the "
        "ingestion pipeline to the demo storefront, and I used AI coding tools throughout while keeping every "
        "change behind tests and measurements.",
        "I try to reason from evidence rather than intuition. I measured retrieval on 127 labelled queries with "
        "95% confidence intervals: hybrid search found the right product in the top 10 for 72% of queries, "
        "against 41% for vector search alone, so I kept the more complex design only because it earned its "
        "place. A code-graded agent evaluation, 12 tasks run 3 times each, showed a revised prompt passing 12 "
        "of 12 tasks instead of 7 with 29% fewer paid API calls. Simplifying where it counted mattered too: one "
        "HNSW index cut median search latency from 35 ms to 3.1 ms, and moving price and rating limits inside "
        "the search, instead of filtering afterwards, raised correct results from 70% to 100%.",
        "I also fine-tuned AraBERT to classify 77 Arabic banking intents (macro-F1 0.919) and served it as an "
        "ONNX model behind a monitored API, and I co-authored published LoRA fine-tuning work. I completed my "
        "BSc in Computer Science in 2024 and my military service, and I now teach Operating Systems to more than "
        "700 students and mentor learners in the MLOps MENA community. Teaching has made me good at explaining "
        "trade-offs and at helping other people's ideas win, which I think fits your small, talent-dense teams.",
        "I'm Egyptian, fluent in English and ready to relocate to any of your offices. Thank you for "
        "considering my application; I'd welcome the chance to take your tests and show what I can do.",
    ],
    "closing": "Sincerely,",
}
