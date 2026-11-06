"""Enveritas (YC S18, non-profit) — Backend Software Engineer. Remote worldwide, USD 135-155k. HN "Who is hiring?"
September 2026; posting at enveritas.org/jobs (Cloudflare blocks automated checks). Sustainability data for
smallholder coffee, cocoa and tea farmers (EUDR deforestation checks).
Asks: Python, PostgreSQL/PostGIS, Docker, AWS, Terraform. Not claimed: PostGIS, AWS, Terraform, geospatial.
Built on the Audena backend variant.
"""
from variants.audena import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_Enveritas"

TITLE = "Backend Software Engineer — Python, PostgreSQL & Docker"

SUMMARY = (
    "Backend engineer building data-heavy Python services: FastAPI and Pydantic APIs on PostgreSQL (SQLAlchemy, "
    "Alembic migrations, indexing), ingestion pipelines that validate every row (pandas loaders for 5 file formats), "
    "Docker Compose deployments, 104 automated tests in GitHub Actions CI, and Prometheus/Grafana monitoring. Measures "
    "what changes: an HNSW index cut median search latency from 35 ms to 3.1 ms on a 12,730-product catalogue. Keen "
    "to apply this to field data for farmers and supply chains. Based in Egypt, remote."
)
