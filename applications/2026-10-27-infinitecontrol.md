# AI Engineer (Senior/Mid Level) — Infinite Control (Cairo)

- **Posting:** Wuzzuf https://wuzzuf.net/jobs/p/pcajnbfwstm2-ai-engineer-seniormid-level-infinite-control-cairo-egypt, posted 8 Oct 2026; seen through freehire. Wuzzuf blocks automated checks, so **open the link first**. On site in Cairo.
- **Apply:** on Wuzzuf (**Apply For Job**). Upload `Ahmed_Dorra_CV_InfiniteControl.pdf`.
- **Verdict: apply as a stretch.** The title says Senior/Mid, but the requirements read like your project list:
  - advanced RAG (chunking, metadata filtering, vector search, retrieval optimisation);
  - agents with tools, state and memory;
  - evaluation of retrieval quality, tool-call accuracy and regressions;
  - guardrails against prompt injection and excessive agency, with "LLMs are untrusted components";
  - FastAPI, PostgreSQL, LangGraph, Hugging Face, LoRA and PyTorch.
  - **Gaps (not claimed):** document intelligence and OCR, ERP/CRM integration, async background processing, LlamaIndex, vLLM, Ollama, QLoRA and quantisation.
- **Company check: thin but no red flags.** I found only the Wuzzuf post. infinitecontrol.net was registered in October 2021, but it isn't confirmed to be the same company. Ask for the company website if they call. The post asks for no fee.

---

## Note (if Wuzzuf asks)

Hello, I'm applying for the AI Engineer role. I build RAG systems and LLM agents in Python: hybrid PostgreSQL full-text + pgvector search with reranking and filters applied inside retrieval, LangGraph agents with tool calling and memory behind FastAPI, and evaluation and guardrails that treat model output and user text as untrusted. On my Shopping Assistant, hybrid retrieval reached 72% top-10 recall against 41% for vector alone, and filtering inside search lifted on-target results from 70% to 100%. Based in Giza. — Ahmed Dorra, github.com/AhmedMostafa167

---

## Interview prep

- **Walk through the Shopping Assistant:** the LangGraph graph (nodes, tool calls, conditional routing, bounded retries), where state lives (Postgres checkpointer vs typed facts in PostgreSQL), and why memory is typed facts rather than vectors.
- **Evaluation:** the 12 tasks × 3 runs code-graded suite; prompt v2 went from 7 to 12 of 12 with 29% fewer paid rerank calls; v3 moved price and rating limits inside search (57/81 → 48/48 matching).
- **Retrieval:** hybrid vs keyword vs vector (72% / 56% / 41% top-10 recall on 127 labelled queries), reranking 23% → 43%, HNSW 35 ms → 3.1 ms.
- **Failure handling:** what happens when a tool errors, the model returns invalid JSON (Pydantic validation and retry), or the user tries to plant a false "fact" (memory-write guardrails, 0 of 21 legitimate facts refused).
- **Deterministic workflow vs autonomous agent:** they ask this directly. Your Research Assistant is a fixed graph with bounded retries; the Shopping Assistant lets the model choose tools. Explain when you'd pick each (reliability, audit, cost).
- **"LLMs are never the authorisation layer":** permissions are checked in code before a tool runs, never by asking the model.
- **Document intelligence (gap):** know the pipeline (PDF parsing, layout, OCR for scans, chunking by section, metadata).

---

## Original post

> AI Engineer (Senior/Mid Level) — Infinite Control — Cairo, Egypt — posted 2026-10-08 — https://wuzzuf.net/jobs/p/pcajnbfwstm2-ai-engineer-seniormid-level-infinite-control-cairo-egypt
>
> *Company Description*
>
> Infinite Control is a technology-focused company specializing in advanced automation and intelligent systems. The organization is committed to leveraging artificial intelligence to solve complex real-world problems and improve operational efficiency for its clients. Team members collaborate across disciplines to design, build, and deploy AI-driven solutions that deliver measurable impact
>
> *Job Description*
>
> We are looking for an AI Engineer to transform complex business problems into reliable, secure, and production-ready AI solutions. You will design and develop enterprise AI applications, including RAG systems, AI agents, document intelligence pipelines, and AI-powered business automation, integrated with ERP, CRM, APIs, and other enterprise systems.
>
> *Key Responsibilities*
>
> *
>
> Design and build enterprise-grade LLM applications, RAG systems, AI agents, and document understanding solutions.
>
> *
>
> Develop agentic workflows that use tools and APIs, manage state and memory, and support human-in-the-loop escalation.
>
> *
>
> Integrate AI solutions with ERP, CRM, databases, and enterprise APIs.
>
> *
>
> Transform AI prototypes and proof-of-concepts into scalable, reliable, secure, and production-ready applications.
>
> *
>
> Establish evaluation and testing processes to measure retrieval quality, tool-call accuracy, task completion, hallucinations, and regressions.
>
> *
>
> Implement safeguards against AI security risks such as prompt injection, excessive agency, tool abuse, and data leakage
>
> Requirements
> ------------
>
> *
>
> Bachelor’s or Master’s degree in Computer Science, Engineering, or a related field, or equivalent practical experience.
>
> *
>
> Strong experience with LLM application development, including prompt/context engineering, structured outputs, and function/tool calling.
>
> *
>
> Hands-on experience with Advanced RAG, including chunking, metadata filtering, vector search, and retrieval optimization.
>
> *
>
> Experience designing AI agents and agentic workflows, including planning, tool use, state, and memory.
>
> *
>
> Ability to determine when to use deterministic workflows vs. autonomous agents based on business and reliability requirements.
>
> *
>
> Strong understanding of AI evaluation and security, including the principle that LLMs are untrusted components and must never act as the authorization layer.
>
> *
>
> Strong Python development skills with experience in Git and API integration.
>
> *
>
> Experience with FastAPI or similar backend frameworks.
>
> *
>
> Strong knowledge of PostgreSQL.
>
> *
>
> Experience with async programming and background processing.
>
> *
>
> Understanding of production software engineering, reliability, testing, scalability, and maintainability.
>
> *Nice to Have*
>
> *
>
> *Frameworks:* LangGraph, LlamaIndex, Hugging Face, vLLM, Ollama.
>
> *
>
> *Data & Knowledge:* pgvector, vector databases, Knowledge Graphs.
>
> *
>
> *Advanced ML:* LoRA/QLoRA fine-tuning, quantization, PyTorch.
>
> *
>
> Experience deploying and operating *LLM/AI systems in production*.
