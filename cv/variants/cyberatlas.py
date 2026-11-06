"""CyberAtlas — Software Engineer. Remote worldwide, full-time. HN "Who is hiring?" September 2026. Internet
exposure-mapping startup (cyberatlas.ai, registered January 2026).
Asks: strong Python (Flask/FastAPI) and/or Go; large-scale data systems; OpenSearch/Elasticsearch; Redis/LMDB;
MongoDB/Postgres; Docker; production systems; work on backend services, data pipelines, search, fingerprinting,
vulnerability and malware detection. Apply by email to atlas@cyberatlas.ai with an anti-bot check (run a query on
their Finder tool and paste the first-page results), subject containing "HN Software Engineer".
Not claimed: Go, OpenSearch, Redis, LMDB, MongoDB, security. Built on the Audena backend variant.
"""
from variants.audena import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_CyberAtlas"

TITLE = "Software Engineer — Python (FastAPI), Data Pipelines & Search"

SUMMARY = (
    "Python engineer building backend services, data pipelines and search: FastAPI and Pydantic APIs on PostgreSQL, "
    "ingestion of 5 file formats with row-level validation, and hybrid search that fuses PostgreSQL full-text and "
    "pgvector results (Reciprocal Rank Fusion) with reranking. Measures performance: an HNSW index cut median search "
    "latency from 35 ms to 3.1 ms, and hybrid retrieval reached 72% top-10 recall vs 41% for vector alone on 127 "
    "labelled queries. Docker Compose deployment, 104 automated tests, GitHub Actions CI, Prometheus and Grafana. "
    "Based in Egypt, remote."
)
