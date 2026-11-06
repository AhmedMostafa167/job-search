# Software Engineer — CyberAtlas (remote worldwide)

- **Posting:** Hacker News "Who is hiring?" (September 2026), https://news.ycombinator.com/item?id=49523704. Remote worldwide, full-time.
- **Apply by email** to **atlas@cyberatlas.ai**. A **Gmail draft is ready**; before sending:
  1. Go to https://cyberatlas.ai/finder, run a query yourself (e.g. a domain you know), and paste **the query and the first-page results** into the draft where marked. It's their anti-bot check, so you must do it yourself.
  2. Attach `Ahmed_Dorra_CV_CyberAtlas.pdf`.
  3. Keep the subject: it contains "HN Software Engineer", as they ask.
- **Verdict: apply.** Strong Python (FastAPI), data pipelines, search, Postgres and Docker all fit.
  - **Gaps (not claimed):** Go, OpenSearch or Elasticsearch, Redis, MongoDB, and security work. The post is about 2 months old, so it may have closed; an email costs nothing.
- **Company check: young but no red flags.** CyberAtlas maps internet-exposed infrastructure for security teams (cyberatlas.ai, registered January 2026). The post asks for no fee.

---

## Email (already in Gmail drafts)

**To:** atlas@cyberatlas.ai
**Subject:** HN Software Engineer – Ahmed Dorra

Hello CyberAtlas team,

I'm applying for the Software Engineer role from your Hacker News post. I build Python backend services, data pipelines and search: FastAPI and Pydantic APIs on PostgreSQL, ingestion of 5 file formats with row-level validation, and hybrid search that fuses PostgreSQL full-text and pgvector results with reranking. On a 12,730-product catalogue, an HNSW index cut median search latency from 35 ms to 3.1 ms, and hybrid retrieval reached 72% top-10 recall against 41% for vector search alone. Everything ships in Docker with 104 automated tests and CI. I haven't used Go or OpenSearch in production yet, and I'd pick them up quickly.

Anti-bot check:
1. Query I ran on Finder: [PASTE YOUR QUERY]
2. First-page results: [PASTE THE RESULTS]

CV attached. GitHub: github.com/AhmedMostafa167

Best regards,
Ahmed Dorra
+20 100 614 8440

---

## Interview prep

- **Search at scale:** inverted indexes, BM25, sharding and replicas in OpenSearch, and when to use a vector index.
- **Data pipelines:** batching, retries and idempotency, queues, and deduplicating billions of records (hashing, Bloom filters).
- **Caching:** what Redis is for, and cache invalidation.
- **Security basics:** what "exposed infrastructure" means (open ports, TLS certificates, banners), and fingerprinting.
- **Walk through the Shopping Assistant:** the LangGraph agent, hybrid retrieval (PostgreSQL full-text + pgvector, Reciprocal Rank Fusion, reranking), memory as typed facts in PostgreSQL plus a Postgres checkpointer, and the evaluation (12 tasks × 3 runs; 7 → 12 of 12 with 29% fewer paid rerank calls).
- **Numbers to know:** 72% / 56% / 41% top-10 recall (hybrid / keyword / vector, 127 labelled queries), 23% → 43% right-product-first with reranking, HNSW 35 ms → 3.1 ms, 104 tests.
- **Remote work:** how you work asynchronously: written updates, clear PRs, overlap hours with their time zone (Egypt is GMT+2).

---

## Original post

> Hacker News — HN Who's Hiring September 2026 — 2026-09-01 — https://news.ycombinator.com/item?id=49523704
>
> CyberAtlas | https://cyberatlas.ai | Software Engineer | REMOTE Worldwide | Full-time
> CyberAtlas maps the internet to help security teams, enterprises, and governments discover and understand their exposed digital infrastructure.
> We’re hiring a Software Engineer to build internet-scale systems processing billions of domains and websites.
> You’ll work on backend services, data pipelines, search, fingerprinting, vulnerability detection, malware detection, and performance optimization.
> Looking for strong Python (Flask/FastAPI) and/or Go experience, large-scale data systems, OpenSearch/Elasticsearch, Redis/LMDB, MongoDB/Postgres, Docker, and production systems.
> How to apply:
> Email atlas@cyberatlas.ai with your CV and, as a simple anti-bot check, include:
> 1. The query you ran on Finder ( https://cyberatlas.ai/finder )
> 2. The first-page results returned by that query
> 3. Please include “HN Software Engineer” in the subject.
