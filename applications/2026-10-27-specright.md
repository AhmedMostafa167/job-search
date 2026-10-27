# Agentic Software Engineer (Full Stack) — Specright (remote, Egypt)

- **Posting:** Ashby https://jobs.ashbyhq.com/specright/34f918e4-3f45-4d74-a39b-ed63fb180d1a, published 1 Oct 2026, **open** on 27 Oct. Remote, location "Egypt", full-time.
- **Apply (about 1 minute):** https://jobs.ashbyhq.com/specright/34f918e4-3f45-4d74-a39b-ed63fb180d1a/application
  - Enter your name and email, upload `Ahmed_Dorra_CV_Specright.pdf`, add your LinkedIn URL, and submit.
  - The form has a reCAPTCHA, so I didn't submit it for you.
- **Verdict: apply as a stretch.**
  - Remote from Egypt is exactly what you need. They want agent builders who use agent evals and tracing, which you do.
  - They also want "proven full-stack engineering, shipped to production" and 1–2 agentic features owned in production. You have projects, not paid production work, and no front-end.
  - TypeScript is only a nice-to-have, and Python counts.
- **Company check: no red flags.** Specright is an established US packaging-specification SaaS company, 100% remote, with other Egypt-based roles open (Salesforce Engineer). It hires through Ashby.

---

## Message (if you find the recruiter on LinkedIn)

Hello, I applied for the Agentic Software Engineer role (remote, Egypt). I build LLM agents in Python and judge them with agent-specific evaluation: a code-graded task suite repeated across runs, Langfuse traces of every model and tool call, and regression checks before changes ship. A revised prompt took my Shopping Assistant agent from 7 to 12 of 12 tasks with 29% fewer paid rerank calls. I'd be glad to walk you through it. — Ahmed Dorra, github.com/AhmedMostafa167

---

## Interview prep

- **Walk through the Shopping Assistant:** the LangGraph graph (nodes, tool calls, conditional routing, bounded retries), where state lives (Postgres checkpointer vs typed facts in PostgreSQL), and why memory is typed facts rather than vectors.
- **Evaluation:** the 12 tasks × 3 runs code-graded suite; prompt v2 went from 7 to 12 of 12 with 29% fewer paid rerank calls; v3 moved price and rating limits inside search (57/81 → 48/48 matching).
- **Retrieval:** hybrid vs keyword vs vector (72% / 56% / 41% top-10 recall on 127 labelled queries), reranking 23% → 43%, HNSW 35 ms → 3.1 ms.
- **Failure handling:** what happens when a tool errors, the model returns invalid JSON (Pydantic validation and retry), or the user tries to plant a false "fact" (memory-write guardrails, 0 of 21 legitimate facts refused).
- **Agentic coding practices:** how you use Claude Code or Copilot day to day: break a task into small steps, review every diff, add tests first, and steer when the agent drifts.
- **Tool API design:** structured output schemas, idempotent tools (safe to retry), clear error messages the model can recover from, and rate limiting.
- **Full-stack gap:** be honest. You're backend and AI-focused; describe the Gradio and FastAPI front ends you've shipped, and say you'd pick up their TypeScript stack.
- **Ask them:** the agent products in flight, the Egypt team, and the contract type.

---

## Original post

> Agentic Software Engineer (Full Stack) — specright — Egypt (Remote) — published 2026-10-01 — https://jobs.ashbyhq.com/specright/34f918e4-3f45-4d74-a39b-ed63fb180d1a
>
> Specright is the first purpose-built, patented platform for Specification Management. Whether it's packaging, raw materials, formulas, products, or machines, Specright helps companies digitize, map, and take action across their supply chain to reduce costs, increase profitability, and drive sustainability. Specright serves customers across industries, including packaging, food and beverage, consumer packaged goods, pharmaceutical, retail, industrials, and more.
>
> We're looking for an Agentic Software Engineer (Full-Stack) to help us ship reliable, user-facing AI agent products to production — fast. You'll work at the intersection of modern AI tooling and strong software engineering discipline, building agentic experiences that our customers and internal teams rely on every day.This is not a research role. You will own production systems end-to-end: designing agent architectures, writing and reviewing code (often with agentic coding assistants), setting up rigorous evals, and operating what you build. If you care about making AI agents that actually work — not just demo well — this roleis for you.
>
> What You'll Do
>
>  - Build and Ship Agentic Applications Design, develop, and deliver agentic products end-to-end — including chat-based interfaces, AI workflow tools, and internal copilots — that serve real users in production.
>
>  - Leverage Agentic Coding Workflows Use modern agentic coding tools daily (e.g., Claude Code, Codex, Cursor, and similar assistants) to accelerate delivery while maintaining high code quality and engineering standards.
>
>  - Design Agent Systems Architect agent internals: tool calling, multi-step orchestration, memory and state management, retrieval pipelines, permissions models, and failure recovery strategies.
>
>  - Own Evals and Quality Build and maintain agent evaluation infrastructure — regression suites, scenario-based tests, golden traces, and both offline and online metrics — so you always know whether your agent got better or worse.
>
>  - Implement Observability Instrument agents with production-grade observability: distributed tracing, prompt and version tracking, tool-call telemetry, and cost/latency monitoring.
>
>  - Own Production Readiness Take responsibility for the full lifecycle: rollout plans, QA, guardrails, incident response, and continuous improvement of deployed agents.
>
> What You Bring (Must-Haves)
>
>  - Proven full-stack engineering ability. You've shipped production software end-to-end — not justprototypes or demos.
>
>  - Hands-on experience building LLM-powered agents that work in production. You've owned at least 1–2 agentic features or products through deployment and operation.
>
>  - Deep familiarity with agentic coding best practices. You understand task decomposition, agent delegation, prompt hygiene, iterative loops, and how to review and steer agentic outputs effectively.
>
>  - Practical experience with agent evals and tracing. You've gone beyond model benchmarking to build evaluation systems specifically for agent behavior — including trace-based debugging and regression detection.
>
>  - Solid engineering fundamentals. Testing, debugging, security basics, performance optimization, and reliability are second nature to you.
>
> Nice-to-Haves
>
>  - Proficiency in TypeScript/Node.js and/or Python, with experience in modern web stacks and startup-pace delivery.
>
>  - Familiarity with agent tooling ecosystems: prompt/version stores, eval harnesses, tracing and telemetry platforms (OpenTelemetry, LangSmith, Datadog, Honeycomb, or similar).
>
>  - Experience with RAG architectures: vector databases, indexing strategies, chunking approaches, and retrieval evaluation.
>
>  - Experience designing tool APIs for agents: structured output schemas, idempotency, rate limiting, and error handling patterns that make agents more reliable.
>
> We are an energetic company with an entrepreneurial, informal, versatile, intelligent, and fast-paced culture. We are a 100% remote company and promote an open and relatively flat organization with an emphasis on collaboration, sharing ideas, and information. It's more important to innovate than to worry about making mistakes.
>
> Specright is an equal opportunity employer. We celebrate diversity and are committed to creating an inclusive environment for all employees.
