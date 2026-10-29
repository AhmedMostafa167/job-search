# AI Engineer — MigrationIT (Cairo; 0–2 years)

- **Posting:** MigrationIT careers on Zoho Recruit, job 586058000030469269, posted **28 Oct 2026**: https://migrationit.zohorecruit.com/jobs/Careers/586058000030469269 (found through freehire).
- **Apply:** open the link → **Apply** → fill the form and upload `Ahmed_Dorra_CV_MigrationIT.pdf`. Paste the note below if there's a cover-letter box.
- **Verdict: apply. One of the best fits in this sweep.**
  - **0–2 years.** They want Python components that connect apps to LLMs, model API integration with structured outputs and validation, RAG (chunking, embeddings), multi-step workflows with tool calls, state and retries, evaluation test cases (relevance, factual consistency, response time), Git, testing and logs, FastAPI and Docker, and guardrails.
  - Every core ask is in the Shopping Assistant or the Research Assistant.
  - **Gaps (not claimed):** n8n, cloud platforms, and human-review queues.
- **Company check: no red flags.** MigrationIT is an IT services company (migrationit.com, registered 2011). The post is on its own Zoho Recruit page and lists social and medical insurance. No fee, no ID.

---

## Note to paste (message box or cover note)

Hello MigrationIT team,

I'm applying for the AI Engineer role in Cairo. Your list reads like my last year of work. I connect applications to LLMs in Python: model API integration with Pydantic-validated structured outputs, RAG pipelines (chunking, embeddings, hybrid vector search, reranking), and LangGraph workflows with tool calls, state and bounded retries, served through FastAPI on PostgreSQL in Docker. I write test cases before trusting a change. On a 12,730-product assistant, labelled queries measured relevance (72% top-10 recall), a grounding check confirmed quoted prices in 25 of 25 runs, and an index change cut median search time from 35 ms to 3.1 ms. The repository has 104 automated tests, guardrails and tracing.

I'm based in Giza and can start soon.

GitHub: github.com/AhmedMostafa167
Portfolio: ahmedmostafa167.github.io
LinkedIn: linkedin.com/in/ahmed-mostafa-dorra

Best regards,
Ahmed Dorra
+20 100 614 8440 · newahmed1672022@gmail.com

---

## Interview prep

- **LLM integration:** how you validate model output with Pydantic and what happens on a validation failure (retry with the error, or fall back to a safe answer).
- **RAG:** chunking choices, embeddings, why hybrid search (72% vs 56% keyword vs 41% vector), Reciprocal Rank Fusion, and reranking (23% → 43%).
- **Workflows:** the LangGraph graph, state, tool calls, and the Research Assistant's reflection step with a bounded retry.
- **Evaluation:** turning "relevance, factual consistency, response time" into tests: labelled queries, the grounding check, and latency (35 ms → 3.1 ms with HNSW).
- **Support:** how you'd debug a failed API call or a bad retrieval (Langfuse traces, logs, reproducing with a fixed test case).
- **Safety:** prompt injection, keeping secrets out of prompts, and your input and memory-write guardrails (0 of 21 legitimate facts refused).
- **AI coding assistants:** say you use them and always verify generated code with tests.
- **Ask them:** which clients or products the AI team builds for, and which model providers they use.

---

## Original post

> Source: https://migrationit.zohorecruit.com/jobs/Careers/586058000030469269
>
> AI Engineer — MigrationIT — Cairo, Egypt — posted 2026-10-28
>
> * AI application development: Build and maintain Python components that connect applications to approved AI models, internal services, and databases.
>
> * LLM integration: Assist with prompt development, model API integration, structured outputs, and validation of model responses.
>
> * Retrieval workflows: Support document preparation, chunking, embedding generation, and retrieval-augmented generation (RAG) pipelines.
>
> * Orchestration: Help connect model calls, retrieval steps, tools, and business logic into controlled workflows with appropriate error handling and human review.
>
> * Evaluation: Create test cases and assess output relevance, factual consistency, response time, and common failure scenarios.
>
> * Application support: Investigate failed API calls, retrieval problems, unexpected model responses, and workflow errors; document and escalate findings.
>
> * ​Responsible implementation: Use approved AI coding assistants, validate generated code, and follow security and data-handling requirements. Do not submit confidential information to unapproved AI services.
>
> Requirements
> ------------
>
> * 0–2 years of relevant experience; a degree in computer science, engineering, data science, or a related field, or equivalent practical experience.
>
> * Python and APIs: Basic proficiency in Python, HTTP/REST APIs, JSON, exception handling, and integrating external services.
>
> * Databases: Basic SQL and relational-database concepts, plus awareness of the purpose of vector search and embeddings.
>
> * Machine learning: Understanding of core ML concepts, including training versus inference, evaluation, and overfitting.
>
> * LLMs: Foundational knowledge of prompting, tokens, context windows, embeddings, RAG, hallucinations, and output validation.
>
> * Orchestration: Basic understanding of multi-step AI workflows, tool calls, state, retries, and fallbacks; exposure to one tool or framework such as LangChain, LangGraph, n8n, or an equivalent.
>
> * AI-assisted development: Ability to use a coding assistant responsibly, explain generated code, and verify its behavior through testing.
>
> * Engineering and support: Basic Git, debugging, testing, log analysis, and awareness of secure credential handling.
>
> * Preferred qualifications: Practical AI work: A chatbot, document Q&A, retrieval, or AI automation project built during study, an internship, or independent learning.
>
> * Application development: Exposure to FastAPI or Flask, Docker, a cloud platform, or an approved model-serving service.
>
> * AI safety and monitoring: Awareness of prompt injection, sensitive-data exposure, output guardrails, and monitoring model usage and errors.
>
> Benefits
> --------
>
> Social and Individual Medical Insurance
