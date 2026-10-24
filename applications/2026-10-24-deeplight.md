# Applied AI Engineer – Agentic Systems — Deeplight AI, Dubai (full-time, visa sponsored)

- **Posting:** LinkedIn, https://www.linkedin.com/jobs/view/4480956223 (posted 19 Oct 2026; found 24 Oct through a LinkedIn search). Deeplight also lists jobs on Workable: https://apply.workable.com/deeplight/
- **Apply:** on LinkedIn (Easy Apply, or the company form it opens). Upload `Ahmed_Dorra_CV_Deeplight.pdf`, and `Ahmed_Dorra_Cover_Letter_Deeplight.pdf` if there's a cover-letter field.
  - Screening answers: **years of experience** `[FILL IN]`, and be honest: projects, research internship and teaching, no company AI job yet. **Visa:** you need sponsorship, which they offer. **Notice period** `[FILL IN]` · **Expected salary (AED/month)** `[FILL IN]`.
- **Verdict: apply. This is the best match in this batch.**
  - The must-haves read like a description of your Shopping Assistant: agents with tool calling and state, pytest, structured outputs validated with Pydantic, evaluation on representative task sets with tracing, and trade-offs between quality, latency and cost. No years of experience are stated.
  - Gaps: MCP, AWS/Azure and banking clients. All three are listed as an "edge", not a requirement. None is claimed; the letter says so plainly.
  - They want people who can explain and "sell" their decisions to clients. Your teaching (50 labs, 600+ students) supports that.
- **Company check: no red flags.** deeplight.ai was registered in 2021. It's a UAE AI and data consultancy (DIFC, Dubai) serving banks, insurers and enterprises. Workable and GulfTalent list its other jobs (Principal AI/ML Engineer, GenAI Engineer). The posting offers individual visa sponsorship and health insurance. It asks for no fee and no ID. Their website didn't load from here, so open it once before the interview.

---

## Note to a Deeplight recruiter (LinkedIn message, after applying)

Hello, I've just applied for the Applied AI Engineer – Agentic Systems role. I build LangGraph agents with tool calling and memory, and I evaluate them with code-graded task sets: on my Shopping Assistant, a revised prompt took the agent from 7 to 12 of 12 tasks with 29% fewer paid rerank calls. I'm ready to relocate to Dubai and would be glad to walk you through the system. Thank you! — Ahmed Dorra

---

## Interview prep

- **"Walk us through a system you built"** (they say they will ask). Have a 5-minute version of the Shopping Assistant ready:
  1. Problem.
  2. Architecture: agent, search tool, hybrid retrieval, memory.
  3. Evaluation: 12 tasks × 3 runs, logged to Langfuse and MLflow.
  4. What broke: vector-only recall of 41%, prompt v1 passing 7 of 12, and about 30% of results breaking price or rating limits.
  5. Fixes.
  6. Limits: the reranking result is on a 40-query subset, and the tests use labelled data, not real users.
- **State management:** what lives in LangGraph state vs the Postgres checkpointer vs long-term facts (typed facts, `MAX_FACTS_PER_USER = 50`), and how memory writes are guarded (0 of 21 legitimate facts refused).
- **Failure handling:** tool errors, timeouts, retries with limits (the Research Assistant's bounded reflection retry), fallbacks, and when to hand off to a human.
- **Structured outputs:** Pydantic schemas, what to do when validation fails (retry with the error, or fall back).
- **Evaluation:** representative tasks, code graders vs LLM-as-a-judge, why you ran each task 3 times (non-determinism), regression testing between prompt versions, failure-mode analysis.
- **Trade-offs:** reranking cost vs quality (29% fewer paid rerank calls), HNSW latency vs recall (35 ms → 3.1 ms), model choice (Groq for speed).
- **MCP (gap):** know the basics. It's an open protocol: an MCP server exposes tools, resources and prompts, and an LLM client discovers and calls them. Say how you'd wrap your search tool as an MCP server.
- **Cloud (gap):** you've deployed with Docker and on Hugging Face Spaces; know what AWS Bedrock and Azure OpenAI offer.
- **Relocation:** ready to move to Dubai; the employer sponsors the visa.

---

## Original post (LinkedIn)

> **Applied AI Engineer - Agentic Systems** — Deeplight AI · Dubai, Dubai, United Arab Emirates
>
> DeepLight AI is a specialist AI and data consultancy dedicated to transforming the regional corporate landscape through bespoke, high-impact intelligent systems. Based in the UAE, we partner with major enterprise and financial services clients to bridge the gap between cutting-edge AI research and operational business reality.
>
> We don't build isolated prototypes or generic "off-the-shelf" wrappers. We engineer secure, scalable, and resilient AI foundations designed to integrate seamlessly into complex corporate environments.
>
> The Opportunity
>
> We are seeking a hands-on Applied AI Engineer - Agentic Systems to design, build, and deploy LLM-powered autonomous agents and multi-step agentic workflows for real-world enterprise use cases.
>
> In this role, you will bridge the gap between advanced AI capabilities and production software engineering. You will combine tool calling, state management, context engineering, and external API integrations to transform complex business processes into reliable, auditable, and maintainable AI applications.
>
> What You'll Do
>
> Architect Autonomous Workflows: Design and implement multi-step agent loops, state machines, and tool-calling mechanisms that execute complex enterprise tasks autonomously and reliably
> Master Context Engineering & RAG: Build advanced context management pipelines and Retrieval-Augmented Generation (RAG) modules to ground agent reasoning in dynamic enterprise knowledge sources
> Integrate & Connect Systems: Develop secure API integrations connecting LLMs and agents to enterprise databases, legacy line-of-business applications, and modern protocol standards (such as MCP)
> Engineering for Production & Fail-Safes: Write clean, production-ready Python code backed by automated testing, structured output validation (e.g., Pydantic), fallback logic, and human-in-the-loop (HITL) oversight controls
> Evaluate, Trace & Optimize: Instrument end-to-end tracing and evaluation suites (e.g., LangSmith, Phoenix) to benchmark performance, eliminate hallucination loops, diagnose latency spikes, and optimize token costs
> Translate & Advocate: Collaborate directly with client technical teams and business sponsors to translate ambiguous processes into clear technical designs, acceptance criteria, and system architectures
>
> As an AI consultancy, our greatest asset is the expertise of our people.
>
> While technical mastery is the foundation of what we do, the ability to bridge the gap between complex data science and actionable business value is what defines your success with Deeplight.
>
> We're looking for individuals who are not only world-class in their fields of specialism, but also compelling communicators and persuasive advocates for their own skills.
>
> You will be the face of our firm, tasked with building trust, articulating the "why" behind your technical decisions, and effectively "selling" your vision to high-level stakeholders.
>
> If you thrive on the challenge of presenting cutting-edge solutions as much as you do on building them, you will fit right in.
>
> Requirements
>
> What We're Looking For
>
> Demonstrable experience personally implementing AI agents, multi-agent frameworks, tool calling, and state management systems
> Advanced proficiency in Python with a focus on code maintainability, testing (pytest), code reviews, and Git version control
> Practical experience integrating commercial and open-weight LLM APIs, designing prompts, validating structured outputs, and gracefully handling model/tool failures
> Experience evaluating LLM applications using representative task sets, failure mode analysis, regression testing, and application tracing tools
> Ability to articulate and balance decisions across reasoning quality, system reliability, inference latency, and operational cost
>
> What Gives You an Edge
>
> Experience deploying and supporting LLM agents used by active business teams or external customers
> Familiarity with modern orchestration frameworks (e.g., LangGraph, AutoGen, CrewAI, LlamaIndex Workflows) or custom state-machine implementations
> Hands-on experience with the Model Context Protocol (MCP), Docker containerization, and cloud deployment (AWS/Azure)
> Prior experience delivering technical solutions directly within regulated enterprise environments (e.g., Banking, Financial Services, Insurance)
>
> Demonstrating Your Expertise
>
> We value practical, battle-tested engineering. During our process, candidates should be prepared to walk through a system they personally built—explaining implementation choices, evaluation approaches, system limitations, and how they navigated the journey from prototype to production.
>
> Benefits
>
> The benefits you'll enjoy as part of this role include:
>
> Competitive salary
> Comprehensive 'Gold Level' personal health insurance
> Individual Visa Sponsorship
> Professional development and certification support
> Subscription reimbursement relating to your role
> Opportunity to work on cutting-edge AI projects
> Monthly Employee Incentive program
> Career advancement opportunities in a rapidly growing AI company
>
> This position offers a unique opportunity to shape the future of AI implementation while working with a talented team of professionals at the forefront of technological innovation. The successful candidate will play a crucial role in driving our company's success in delivering transformative AI solutions to our clients.
>
> At DeepLight AI, we recognise that diversity drives innovation. We are committed to fostering an inclusive environment where individuals with different thinking styles can thrive and contribute their unique strengths to our specialised AI and data solutions.
>
> Our goal is to ensure our application and interview process is accessible, predictable, and fair for all candidates.
>
> If you require any specific adjustments to the application process, or if you require any reasonable adjustments should you be successful in being processed to the interview stage, please do let us know. This information will be kept strictly confidential and will not impact hiring decisions.
