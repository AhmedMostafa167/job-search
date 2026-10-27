# Machine Learning Engineer, Multilingual Data — Featherless AI (remote)

- **Posting:** Himalayas https://himalayas.app/companies/featherless-ai/jobs/machine-learning-engineer-multilingual-data (posted 24 Sep 2026, listed until 23 Nov). No location restriction.
- **Apply:** open the link on your phone and tap **Apply**; it goes to their hiring page. Upload `Ahmed_Dorra_CV_Featherless.pdf`. Himalayas blocks automated checks, so I couldn't follow the link myself.
- **Verdict: apply as a stretch.**
  - They want 3+ years. But the core of the role is **non-English data quality**, and native Arabic plus careful evaluation is a real edge.
  - NLP fundamentals, embeddings, data pipelines with validation, and fine-tuning exposure all fit.
  - **Gaps (not claimed):** Spark or Ray, multilingual benchmarks (FLORES, XTREME), and LLM training at scale.
- **Company check: no red flags.** Featherless AI is a Series A LLM-inference platform (featherless.ai, registered May 2024). The post asks for no fee.

---

## Cover note (if there's a box)

Hello Featherless team,

I'm applying for the Machine Learning Engineer, Multilingual Data role. I'm a native Arabic speaker, and much of my work is about data quality and measurement: Python pipelines that validate every row (pandas loaders for 5 file formats with Pydantic), labelled evaluation sets with 95% confidence intervals, and stage-by-stage comparisons. On a 12,730-product search system, hybrid retrieval reached 72% top-10 recall against 41% for vector search alone. I also fine-tuned Stable Diffusion with LoRA (with a colleague; published). I know first-hand where Arabic breaks tokenisers and English-first models, and I'd like to help fix that in your data. Based in Egypt (GMT+2), remote.

Ahmed Dorra · github.com/AhmedMostafa167 · linkedin.com/in/ahmed-mostafa-dorra

---

## Interview prep

- **Arabic data issues:** dialects vs MSA, diacritics, Arabizi (Arabic in Latin letters), right-to-left text with embedded numbers and code, tokeniser fertility (more tokens per word), and normalisation (alef and yaa variants).
- **Data quality:** deduplication (exact and near-duplicate with MinHash), language identification, filtering toxic or low-quality text, and measuring a dataset's effect by training and evaluating a small model.
- **Benchmarks:** FLORES (translation), XTREME (cross-lingual), and Arabic suites (e.g., ArabicMMLU). Know what each measures.
- **Pipelines:** how you'd scale your pandas pipeline (chunking, multiprocessing, then Spark or Ray).
- **Walk through the Shopping Assistant:** the LangGraph agent, hybrid retrieval (PostgreSQL full-text + pgvector, Reciprocal Rank Fusion, reranking), memory as typed facts in PostgreSQL plus a Postgres checkpointer, and the evaluation (12 tasks × 3 runs; 7 → 12 of 12 with 29% fewer paid rerank calls).
- **Numbers to know:** 72% / 56% / 41% top-10 recall (hybrid / keyword / vector, 127 labelled queries), 23% → 43% right-product-first with reranking, HNSW 35 ms → 3.1 ms, 104 tests.
- **Remote work:** how you work asynchronously: written updates, clear PRs, overlap hours with their time zone (Egypt is GMT+2).

---

## Original post

> Machine Learning Engineer — Multilingual Data — Featherless AI — Worldwide — posted 2026-09-24 — https://himalayas.app/companies/featherless-ai/jobs/machine-learning-engineer-multilingual-data
>
> We’re looking for a Machine Learning Engineer to own and scale our multilingual data pipeline—from sourcing and curation to evaluation and continuous improvement. You’ll work closely with researchers and infra engineers to ensure our models perform robustly across languages, scripts, and cultural contexts.
>
> This role sits at the intersection of data, research, and production ML and is ideal for someone who cares deeply about data quality, linguistic diversity, and model generalization beyond English.
>
> What You’ll Do
>
> Design, build, and maintain large-scale multilingual datasets across high- and low-resource languages
>
> Develop data pipelines for collection, cleaning, normalization, deduplication, and labeling
>
> Implement quality filters using statistical, heuristic, and model-based methods
>
> Work with researchers to define language coverage, benchmarks, and evaluation metrics
>
> Analyze dataset bias, coverage gaps, and failure modes across regions and scripts
>
> Support training, fine-tuning, and distillation workflows with high-quality multilingual data
>
> Continuously iterate on datasets based on model performance and real-world usage
>
> What We’re Looking For
>
> 3+ years of experience as an ML Engineer, Applied Scientist, or similar role
>
> Strong experience working with multilingual or non-English datasets
>
> Solid understanding of NLP fundamentals (tokenization, embeddings, language modeling)
>
> Experience building scalable data pipelines (Python, Spark, Ray, or similar)
>
> Familiarity with Unicode, scripts, tokenization challenges, and language-specific quirks
>
> Comfort collaborating with researchers and translating research needs into production systems
>
> Nice to Have
>
> Experience with low-resource languages or multilingual benchmarks (e.g. FLORES, XTREME)
>
> Exposure to LLM training, fine-tuning, or distillation
>
> Linguistics background or experience working with native language experts
>
> Contributions to open-source datasets or ML tooling
>
> Experience with data quality evaluation at scale
>
> Why Join
>
> Real ownership over a core differentiator of the product
>
> Work on models used globally, not just in English-speaking markets
>
> Small, high-caliber team with deep ML and systems experience
>
> Competitive compensation + meaningful equity at Series A stage
>
> Originally posted on Himalayas
