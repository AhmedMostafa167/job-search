# Backend Software Engineer — Enveritas (YC S18 non-profit; remote worldwide)

- **Posting:** Hacker News "Who is hiring?" (September 2026), https://news.ycombinator.com/item?id=49541107. The role page is https://enveritas.org/jobs/backend-software-eng/ (worldwide remote, USD 135–155k). Their site blocks automated checks, so **open the link to confirm it's still open**.
- **Apply:** on the Enveritas jobs page. Upload `Ahmed_Dorra_CV_Enveritas.pdf`.
- **Verdict: apply as a stretch.** Python, PostgreSQL and Docker fit, and the mission (sustainability data for smallholder farmers) is a good story.
  - **Gaps (not claimed):** PostGIS and geospatial work, AWS and Terraform. The level isn't stated; the pay suggests mid-level.
- **Company check: no red flags.** Enveritas is a well-known YC-backed 501(c)(3) non-profit working in 30+ countries.

---

## Cover note

Hello Enveritas team,

I'm applying for the Backend Software Engineer role. I build data-heavy Python services: FastAPI and Pydantic APIs on PostgreSQL (SQLAlchemy, Alembic migrations, indexing), ingestion pipelines that validate every row, Docker Compose deployments, 104 automated tests in CI, and Prometheus/Grafana monitoring. On a 12,730-product catalogue, an HNSW index cut median search latency from 35 ms to 3.1 ms. I'd love to apply this to field data that helps farmers and supply chains. I haven't used PostGIS or Terraform yet. Based in Egypt, remote.

Ahmed Dorra · github.com/AhmedMostafa167

---

## Interview prep

- **PostGIS basics (gap):** geometry vs geography types, spatial indexes (GiST), ST_Intersects and ST_Within, and checking a farm polygon against deforestation maps.
- **Data quality from the field:** validating survey data, handling missing and duplicate records, auditability.
- **AWS and Terraform basics:** RDS, ECS or Lambda, S3; why infrastructure as code.
- **Walk through the Shopping Assistant:** the LangGraph agent, hybrid retrieval (PostgreSQL full-text + pgvector, Reciprocal Rank Fusion, reranking), memory as typed facts in PostgreSQL plus a Postgres checkpointer, and the evaluation (12 tasks × 3 runs; 7 → 12 of 12 with 29% fewer paid rerank calls).
- **Numbers to know:** 72% / 56% / 41% top-10 recall (hybrid / keyword / vector, 127 labelled queries), 23% → 43% right-product-first with reranking, HNSW 35 ms → 3.1 ms, 104 tests.
- **Remote work:** how you work asynchronously: written updates, clear PRs, overlap hours with their time zone (Egypt is GMT+2).

---

## Original post

> Hacker News — HN Who's Hiring September 2026 — 2026-09-02 — https://news.ycombinator.com/item?id=49541107
>
> Enveritas (YC S18, non-profit) | Backend Software Engineer | Remote (Global) | https://enveritas.org/jobs/
> Enveritas is a 501(c)(3) nonprofit working on sustainability issues facing smallholder coffee farmers. We collect field data in 30+ countries and build systems for analyzing risks in coffee, cocoa, and tea supply chains (including EUDR-related deforestation checks).
> * Backend Software Engineer (Python, PostgreSQL/PostGIS, Docker, AWS, Terraform) - $135-$155k - https://enveritas.org/jobs/backend-software-eng/#10d7adef8us (worldwide remote)
