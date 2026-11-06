# Junior AI Engineer, Production Agentic AI Systems — Careernet (Ajman, UAE)

- **Posting:** GulfTalent job 598724 (https://www.gulftalent.com/uae/jobs/ai-engineer-598724), posted 17 Jun 2026; seen through freehire. GulfTalent blocks automated checks, so **open the link first** to see whether it's still live.
- **Apply:** on GulfTalent (free account). Upload `Ahmed_Dorra_CV_Careernet.pdf`.
- **Verdict: apply.** It's "Junior", 1–4 years, on a live production AI agent for customer support and operations. They ask for agentic AI, RAG, tool calling, memory systems, LangGraph or similar, Git, Docker and CI/CD.
  - **Gaps (not claimed):** JavaScript or TypeScript, AWS (EC2, RDS, CloudWatch), OpenClaw, CrewAI, DSPy and LlamaIndex.
- **Company check: no red flags.** Careernet is a large Indian recruitment firm hiring for a client in Ajman. The client isn't named, so ask who it is. The post asks for no fee.

---

## Note (if GulfTalent has a cover-letter box)

Hello, I'm applying for the Junior AI Engineer – Production Agentic AI Systems role in Ajman. I build LLM agents end to end in Python: LangGraph agents that call tools and APIs, conversation state and long-term memory in PostgreSQL, RAG with hybrid search, FastAPI services in Docker with GitHub Actions CI, and the tests and evaluation that keep agents reliable. A revised prompt took my Shopping Assistant agent from 7 to 12 of 12 test tasks. I'm based in Egypt and ready to relocate to the UAE. — Ahmed Dorra, github.com/AhmedMostafa167

---

## Interview prep

- **Walk through the Shopping Assistant:** the LangGraph graph (nodes, tool calls, conditional routing, bounded retries), where state lives (Postgres checkpointer vs typed facts in PostgreSQL), and why memory is typed facts rather than vectors.
- **Evaluation:** the 12 tasks × 3 runs code-graded suite; prompt v2 went from 7 to 12 of 12 with 29% fewer paid rerank calls; v3 moved price and rating limits inside search (57/81 → 48/48 matching).
- **Retrieval:** hybrid vs keyword vs vector (72% / 56% / 41% top-10 recall on 127 labelled queries), reranking 23% → 43%, HNSW 35 ms → 3.1 ms.
- **Failure handling:** what happens when a tool errors, the model returns invalid JSON (Pydantic validation and retry), or the user tries to plant a false "fact" (memory-write guardrails, 0 of 21 legitimate facts refused).
- **AWS basics (gap):** EC2 (virtual machines), RDS (managed PostgreSQL), CloudWatch (logs and metrics), and how your Docker Compose setup would map onto them.
- **Customer-support agents:** escalation to a human, refusing out-of-scope requests, and measuring resolution rate.
- **Ask them:** the client company, salary range in AED, visa, and the on-site setup in Ajman.

---

## Original post

> AI Engineer — Careernet — Ajman, UAE — posted 2026-06-17 — https://www.gulftalent.com/uae/jobs/ai-engineer-598724
>
> Position: Junior AI Engineer – Production Agentic AI Systems Location: Ajman Required years of experience: 1 - 4 years We are looking for a passionate Junior AI Engineer to join a fast-growing team and work on a live, production-grade AI agent powering customer support and business operations. This is an excellent opportunity for engineers who want hands-on exposure to Agentic AI, AWS infrastructure, LLM integrations, automation workflows, and enterprise-scale AI systems. Key Responsibilities: 1. Support and enhance production AI agents built on OpenClaw and LLM technologies. 2. Debug and improve agent behavior, routing, reliability, and response quality. 3. Maintain and optimize customer support and internal operations workflows. 4. Work with PostgreSQL databases, APIs, and AI-powered automation tools. 5. Assist with AWS infrastructure, Docker deployments, monitoring, and CI/CD pipelines. 6. Improve observability, evaluations, telemetry, and performance tracking of AI systems. 7. Collaborate with senior engineers to implement safe, scalable, and secure AI solutions.
>
> Qualifications & Skills: 1. Strong foundation in Python and/or JavaScript/TypeScript. 2. Good understanding of Git, Docker, and software development best practices. 3. Familiarity with AWS services such as EC2, RDS, CloudWatch, or similar cloud platforms. 4. Knowledge of Agentic AI concepts, RAG, tool calling, memory systems, or LLM applications. 5. Experience working with databases, APIs, and backend systems. 6. Understanding of security principles, access control, and production system reliability. 7. Strong problem-solving skills with the ability to learn and adapt quickly. Nice-to-have: 1. Experience with OpenClaw, LangGraph, CrewAI, DSPy, LlamaIndex, or similar AI frameworks. 2. Exposure to vector databases, embeddings, fine-tuning, or model serving. 3. Familiarity with AI coding tools such as Cursor, Claude Code, or Codex-style agents. 4. Knowledge of CI/CD pipelines, observability tools, and cloud security practices.
