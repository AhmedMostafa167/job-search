# AI Agent Engineer graduate roles (2027 start) — ByteDance (Dubai) and TikTok (Singapore)

- **Postings:**
  - **ByteDance:** Enterprise Services AI Agent Engineer Graduate (Corporate Service System – Global Travel), Dubai. LinkedIn job 4475398701, posted 26 Oct 2026.
  - **TikTok:** AI Agent Algorithm Engineer Graduate (Global E-Commerce, Conversational AI), Singapore. LinkedIn job 4447695182, posted 21 Oct 2026.
- **Apply:** from each LinkedIn page, which sends you to jobs.bytedance.com (free account). Upload `Ahmed_Dorra_CV_AI_Agents.pdf` to both.
  - **Rules:** you can apply to at most 2 ByteDance/TikTok jobs worldwide, considered in the order you apply. These two are the best fits, so use your 2 slots on them, **Dubai first**.
  - They ask you to state your **graduation date and availability** in the resume. The CV summary says "BSc, June 2024"; put your availability in the form.
  - An online coding assessment follows. Practise LeetCode easy and medium problems.
- **Verdict: apply. Long shots, but a high reward.**
  - **ByteDance (Dubai):** agent runtime, tools/MCP, agent patterns (reasoning, memory, multi-agent), LangChain/LangGraph, prompt and context engineering, and evaluation. They also want Go, Java or Python and distributed systems or microservices; you have Python only.
  - **TikTok (Singapore):** for people "completing or recently completed" a degree, with "genuine hands-on experience with LLMs or agents (side projects count)". Their preferred list includes "your own agent loop, a memory/context system, a RAG or tool-use agent", which is what you've built. They also want Python plus C++, Go, Rust or Java.
  - **Risk:** you graduated in June 2024, which may fall outside their "recent graduate" window.
- **Company check: no red flags.** These are official ByteDance and TikTok campus roles. Apply only on jobs.bytedance.com.

---

## Short answer for "Why this role?" (if asked)

I've built the parts you describe, at side-project scale: a LangGraph agent loop with tool calling, conditional routing and bounded retries; conversation state in a Postgres checkpointer plus long-term memory as typed facts; context assembled from hybrid-search RAG with reranking; and a code-graded evaluation that measures each change (a revised prompt raised task success from 7 to 12 of 12 with 29% fewer paid rerank calls). I want to do this at ByteDance/TikTok scale, across many languages; I'm a native Arabic speaker with professional English.

---

## Interview prep

- **Walk through the Shopping Assistant:** the LangGraph graph (nodes, tool calls, conditional routing, bounded retries), where state lives (Postgres checkpointer vs typed facts in PostgreSQL), and why memory is typed facts rather than vectors.
- **Evaluation:** the 12 tasks × 3 runs code-graded suite; prompt v2 went from 7 to 12 of 12 with 29% fewer paid rerank calls; v3 moved price and rating limits inside search (57/81 → 48/48 matching).
- **Retrieval:** hybrid vs keyword vs vector (72% / 56% / 41% top-10 recall on 127 labelled queries), reranking 23% → 43%, HNSW 35 ms → 3.1 ms.
- **Failure handling:** what happens when a tool errors, the model returns invalid JSON (Pydantic validation and retry), or the user tries to plant a false "fact" (memory-write guardrails, 0 of 21 legitimate facts refused).
- **Online assessment:** arrays, hash maps, two pointers, BFS/DFS, heaps and simple dynamic programming. Do 2 problems a day until the test.
- **Agent runtime topics (TikTok):** context compaction and summarisation, observation masking, just-in-time retrieval, tool search over many tools, LLM-as-a-judge calibrated against human labels.
- **Post-training (gap):** what SFT, DPO and RLHF are, at a high level.
- **Systems (ByteDance):** what a microservice is, idempotency, retries, and how you'd make the agent runtime scale.

---

## Original post

### ByteDance — Dubai

> Enterprise Services AI Agent Engineer Graduate (Corporate Service System - Global Travel) - 2027 Start — ByteDance — Dubai, Dubai, United Arab Emirates — LinkedIn https://www.linkedin.com/jobs/view/4475398701 — Not Applicable, Full-time
>
> Responsibilities
>
> About the Team
>
> We are building an intelligent enterprise-services platform to power ByteDance's global growth and operations. Guided by an AI-First philosophy, the team delivers AI solutions built on industry best practices.
>
> As a campus-hire AI Application Engineer, you will contribute to the end-to-end delivery of AI-powered business systems. Working alongside product, design, and cross-regional engineering teams, you will grow rapidly into an engineer capable of independently building AI products.
>
> We are looking for talented individuals to join our team. As a graduate, you will get opportunities to pursue bold ideas, tackle complex challenges, and unlock limitless growth.
>
> Successful candidates must be able to commit to an onboarding date by the end of the year. Please state your availability and graduation date clearly in your resume.
>
> Candidates can apply to a maximum of two positions and will be considered for jobs in the order you apply. The application limit is applicable to our Company and its affiliates' jobs globally. Applications will be reviewed on a rolling basis - we encourage you to apply early.
>
> Online Assessment
>
> Candidates who pass resume screening will be invited to participate in Our Company's technical online assessment.
>
> Responsibilities
>
> Build backend services and the Agent runtime, ensuring code quality, readability, and maintainability; continuously improve system performance and stability through profiling and tuning.
> Integrate internal enterprise systems into Agents via Tools / MCP / CLI / A2A.
> Take an role in code reviews, and learn and follow the team's coding standards and architectural conventions.
> Write clear, AI-friendly technical documentation and contribute to the team knowledge base.
> Explore embedding AI capabilities into backend services, and contribute to AI-driven feature development, evaluation, and validation.
>
> Qualifications
>
> Minimum Qualifications:
>
> Bachelor's degree or above in Computer Science, AI, or a related field.
> Solid foundation in data structures, algorithms, and computer systems, with strong coding habits.
> Proficiency in one or more of Golang / Java / Python.
> Hands-on experience with distributed systems and microservice architecture.
> Hands-on experience with, and understanding of, AI Agent architectural patterns (reasoning, memory management, multi-Agent collaboration, etc.).
> Strong communication and collaboration skills; genuine interest in exploring the Agent engineering ecosystem.
>
> Preferred Qualifications: AI related Experience
>
> AI product Builder: as a core contributor to build an AI product / Agent / application aimed at real world users. able to articulate the product positioning, technology choices, user scale, and iteration process.
> Hands-on experience with different mainstream Agent frameworks (e.g., LangChain / LangGraph, Claude Agent SDK, etc.), Prompt Engineering, Harness Engineering, Context Management and Evaluation.
>
> By submitting an application for this role, you accept and agree to our global applicant privacy policy, which may be accessed here: https://jobs.bytedance.com/en/legal/privacy
>
> Job Information
>
> About Us
>
> Founded in 2012, ByteDance's mission is to inspire creativity and enrich life. With a suite of more than a dozen products, including TikTok, Lemon8, CapCut and Pico as well as platforms specific to the China market, including Toutiao, Douyin, and Xigua, ByteDance has made it easier and more fun for people to connect with, consume, and create content.
>
> Why Join ByteDance
>
> Inspiring creativity is at the core of ByteDance's mission. Our innovative products are built to help people authentically express themselves, discover and connect – and our global, diverse teams make that possible. Together, we create value for our communities, inspire creativity and enrich life - a mission we work towards every day.
>
> As ByteDancers, we strive to do great things with great people. We lead with curiosity, humility, and a desire to make impact in a rapidly growing tech company. By constantly iterating and fostering an "Always Day 1" mindset, we achieve meaningful breakthroughs for ourselves, our Company, and our users. When we create and grow together, the possibilities are limitless. Join us.
>
> Diversity & Inclusion
>
> ByteDance is committed to creating an inclusive space where employees are valued for their skills, experiences, and unique perspectives. Our platform connects people from across the globe and so does our workplace. At ByteDance, our mission is to inspire creativity and enrich life. To achieve that goal, we are committed to celebrating our diverse voices and to creating an environment that reflects the many communities we reach. We are passionate about this and hope you are too.

### TikTok — Singapore

> AI Agent Algorithm Engineer Graduate (Global E-Commerce, Conversational AI) - 2027 Start — TikTok — Singapore, Singapore — LinkedIn https://www.linkedin.com/jobs/view/4447695182 — Not Applicable, Full-time
>
> Responsibilities
>
> About the Team
>
> We build the next-generation unified Agent system for TikTok's global e-commerce customer service — running in 30+ languages across one of the largest e-commerce surfaces on the internet. Our north star is a self-evolving Agent, where post-training, harness, memory / context engineering, tools, and evaluation form one closed loop, and every served conversation becomes the next iteration's training / eval / retrieval / skill-induction signal. We build the agent runtime itself — Codex / Claude-Code-class — not prompts on top of a vendor API. As a new grad, you'll own a real end-to-end piece from day one and ship it to production.
>
> We are looking for talented individuals to join our team. As a graduate, you will get opportunities to pursue bold ideas, tackle complex challenges, and unlock limitless growth.
>
> Successful candidates must be able to commit to an onboarding date by the end of the year. Please state your availability and graduation date clearly in your resume.
>
> Candidates can apply to a maximum of two positions and will be considered for jobs in the order you apply. The application limit is applicable to our Company and its affiliates' jobs globally. Applications will be reviewed on a rolling basis - we encourage you to apply early.
>
> Job Responsibilities
>
> Build and evolve the agent runtime (harness / agent loop) powering our customer-service agents — orchestrate skills, tools, and context; implement loop control & intervention, progressive disclosure, and behavior-level guardrails.
> Engineer context & memory for long multi-turn agents — agentic memory (structured note-taking), context compaction / summarization, context editing / observation masking, and just-in-time (retrieve-then-load) retrieval.
> Post-train and fine-tune LLMs (SFT / DPO / RL) and build the data flywheel that turns served conversations into training / eval / retrieval signals.
> Design and integrate tools, Skills, and MCP connectors (tools-as-APIs), plus skill / tool search for large tool inventories.
> Build evaluation — LLM-as-judge with human-agreement calibration; regression / safety / cost / latency-aware harnesses; close the offline↔online gap.
> Build the self-evolving loop — replay + user-simulator + Auto-RCA / Auto-GSB / Auto-Policy — so the system continuously improves itself.
> Own one high-leverage end-to-end surface and ship it to production across 30+ languages, measured on real business metrics (CSAT, resolution / containment rate).
>
> Qualifications
>
> Minimum Qualifications
>
> Individuals who are completing or have recently completed a Bachelor's degree or Master's degree in CS / AI / Math or a quantitative field.
> Strong Python plus one of C++ / Go / Rust / Java
> Solid ML / DL / NLP fundamentals, with genuine hands-on experience with LLMs or agents (coursework, research, internship, competition, open-source, or a serious side project)
> Able to read a paper or an engineering blog and turn it into working code
>
> Preferred Qualifications
>
> Have built the runtime, not just called an API — even at research / hobby / competition scale: your own agent loop / harness, a memory / context-management system, a RAG or tool-use agent, or a fine-tuned / post-trained model
> Hands-on experience in any one of: post-training (SFT / DPO / RLHF / RLAIF / RLVR, reward modeling); agent systems (harness, context engineering, MCP / Skills, sub-agents, tool search); evaluation (LLM-as-judge, τ-bench / SWE-bench / GAIA / BFCL); inference & serving (vLLM / TensorRT-LLM, MoE, KV / prompt caching); or multilingual NLP — depth in one is enough, breadth welcome
>
> Job Information
>
> About TikTok
>
> TikTok is the leading destination for short-form mobile video. At TikTok, our mission is to inspire creativity and bring joy. TikTok's global headquarters are in Los Angeles and Singapore, and we also have offices in New York City, London, Dublin, Paris, Berlin, Dubai, Jakarta, Seoul, and Tokyo.
>
> Why Join Us
>
> Inspiring creativity is at the core of TikTok's mission. Our innovative product is built to help people authentically express themselves, discover and connect – and our global, diverse teams make that possible. Together, we create value for our communities, inspire creativity and bring joy - a mission we work towards every day.
>
> We strive to do great things with great people. We lead with curiosity, humility, and a desire to make impact in a rapidly growing tech company. Every challenge is an opportunity to learn and innovate as one team. We're resilient and embrace challenges as they come. By constantly iterating and fostering an "Always Day 1" mindset, we achieve meaningful breakthroughs for ourselves, our company, and our users. When we create and grow together, the possibilities are limitless. Join us.
>
> Diversity & Inclusion
>
> TikTok is committed to creating an inclusive space where employees are valued for their skills, experiences, and unique perspectives. Our platform connects people from across the globe and so does our workplace. At TikTok, our mission is to inspire creativity and bring joy. To achieve that goal, we are committed to celebrating our diverse voices and to creating an environment that reflects the many communities we reach. We are passionate about this and hope you are too.
