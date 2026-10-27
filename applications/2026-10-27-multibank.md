# AI Engineer — Generative AI and Automation — MultiBank Group / MEX Digital (Dubai)

- **Posting:** Ashby https://jobs.ashbyhq.com/mexdigital/4c1abf17-cb71-470b-ae71-3a934c4e0cc7, published 2 Jun 2026 and **still open** on 27 Oct. The same role is on LinkedIn (job 4422417315) under MultiBank Group. On site in Dubai, full-time.
- **Apply (about 1 minute):** https://jobs.ashbyhq.com/mexdigital/4c1abf17-cb71-470b-ae71-3a934c4e0cc7/application
  - Enter your name and email, upload `Ahmed_Dorra_CV_MultiBank.pdf`, and add your phone number and location (Giza, Egypt).
  - Notice period and salary are optional; leave them blank or [FILL IN].
  - The form has a reCAPTCHA, so I didn't submit it for you.
- **Verdict: apply.** They want a **portfolio of deployed agents or RAG apps**. Your Research Assistant is live on Hugging Face Spaces, and the Shopping Assistant is public. They also ask for LangGraph or LangChain, Claude and OpenAI APIs, vector search, FastAPI, Docker, CI, evaluation harnesses and guardrails. They ask for 2+ years, so it's a stretch on years but strong on skills.
  - **Gaps (not claimed):** n8n, Make, Zapier, CrewAI, AutoGen, MCP, cloud and JavaScript/TypeScript.
- **Company check: no red flags.** MultiBank Group is a large, regulated FX and fintech group headquartered in Dubai. The MEX Digital board on Ashby carries the identical post, so the two appear to be the same group. It asks for no fee.

---

## Message (LinkedIn, to a MultiBank recruiter, after applying)

Hello, I applied for the AI Engineer – Generative AI and Automation role in Dubai. I build LLM agents in Python with a public portfolio: a LangGraph shopping agent with tool calling, memory and hybrid-search RAG (a revised prompt took it from 7 to 12 of 12 test tasks with 29% fewer paid rerank calls), and a research assistant live on Hugging Face Spaces that switches between Anthropic, OpenAI, Groq and Hugging Face models. I'm ready to relocate to Dubai. — Ahmed Dorra, github.com/AhmedMostafa167

---

## Interview prep

- **Walk through the Shopping Assistant:** the LangGraph graph (nodes, tool calls, conditional routing, bounded retries), where state lives (Postgres checkpointer vs typed facts in PostgreSQL), and why memory is typed facts rather than vectors.
- **Evaluation:** the 12 tasks × 3 runs code-graded suite; prompt v2 went from 7 to 12 of 12 with 29% fewer paid rerank calls; v3 moved price and rating limits inside search (57/81 → 48/48 matching).
- **Retrieval:** hybrid vs keyword vs vector (72% / 56% / 41% top-10 recall on 127 labelled queries), reranking 23% → 43%, HNSW 35 ms → 3.1 ms.
- **Failure handling:** what happens when a tool errors, the model returns invalid JSON (Pydantic validation and retry), or the user tries to plant a false "fact" (memory-write guardrails, 0 of 21 legitimate facts refused).
- **Automation (gap):** know what n8n, Make and Zapier do (no-code workflow tools) and when you'd write a Python agent instead (complex logic, testing, version control).
- **Fintech context:** guardrails for a trading-support assistant: no financial advice, human-in-the-loop for actions, logging for compliance.
- **MCP (gap):** a standard way to expose tools to models; you could wrap the search tool as an MCP server.
- **Ask them:** which business teams the agents serve, the salary range and visa.

---

## Original post

### Ashby posting (MEX Digital)

> AI Engineer – Generative AI and Automation — mexdigital — Dubai Office (OnSite) — published 2026-06-02 — https://jobs.ashbyhq.com/mexdigital/4c1abf17-cb71-470b-ae71-3a934c4e0cc7
>
> Welcome to MultiBank Group, a global financial pioneer established in 2005 in California and now proudly headquartered in Dubai, UAE. We specialize in delivering cutting-edge trading technology, unparalleled liquidity, and exceptional customer service. Our extensive range of financial products includes Forex, Metals, Shares, Indices, Commodities, and Cryptocurrency CFDs.
>
> Join our thriving community of over 2 million clients across 100 countries, contributing to a daily trading volume exceeding US$ 35 billion. As a heavily regulated institution with oversight from 18+ financial regulators across 5 continents, and recipient of over 80 financial awards, MultiBank Group is devoted to innovation, excellence, and empowering our clients to achieve their financial goals.
>
> Role Overview
>
> We are seeking an AI Engineer to design, build, and deploy intelligent AI agents and automated workflows that address real business problems. This is a hands-on, high-impact role within the Artificial Intelligence and Advanced Analytics team. The successful candidate will own end-to-end delivery of AI agents from scoping and architecture through integration, testing, and production deployment, enabling the organization to automate complex processes and unlock value from generative AI.
>
> Key Responsibilities
>
>  - Design, build, and deploy AI agents using frontier LLMs including Claude (Anthropic API), OpenAI, Gemini, and other frontier models
>
>  - Architect multi-agent systems and agentic workflows using frameworks including LangChain, LangGraph, CrewAI, AutoGen, and Semantic Kernel
>
>  - Build and manage automated business workflows using n8n, Make (Integromat), Zapier, and custom API integrations
>
>  - Implement RAG pipelines with vector databases including Pinecone, Weaviate, Qdrant, and pgvector to give agents access to organizational knowledge bases
>
>  - Design tool-use and function-calling integrations, connecting agents to internal systems, APIs, databases, and third-party services
>
>  - Fine-tune and prompt-engineer LLMs to optimize agent behavior, reliability, and task accuracy
>
>  - Collaborate with business stakeholders to identify automation opportunities and translate requirements into agent-based solutions
>
>  - Monitor, evaluate, and continuously improve deployed agents across quality, latency, cost, and safety metrics
>
>  - Establish and maintain best practices for agent safety, guardrails, human-in-the-loop controls, and responsible AI deployment
>
>  - Develop MCP (Model Context Protocol) server integrations to extend agent capabilities
>
> Requirements
>
>  - Bachelor's or Master's degree in Computer Science, Artificial Intelligence, Software Engineering, or a related field; equivalent practical experience will be considered
>
>  - 2 or more years of hands-on experience building production AI systems or intelligent automation solutions
>
>  - Demonstrated experience building agents or workflows with LangChain, LangGraph, CrewAI, n8n, or comparable frameworks
>
>  - Proven ability to integrate LLM APIs including Anthropic Claude and OpenAI into real-world applications
>
>  - Experience with vector databases and semantic search implementations is strongly preferred
>
>  - Portfolio or demonstrable projects showing deployed agents, automation workflows, or RAG-based applications
>
>  - Proficiency in Python as the primary language; JavaScript or TypeScript is beneficial
>
>  - Familiarity with cloud platforms, Docker, FastAPI, and CI/CD practices for AI pipelines
>
> Technical Skills
>
> LLM APIs: Anthropic Claude (claude-opus-4, claude-sonnet-4), OpenAI GPT-4o, Google Gemini, Mistral
>
> Agent Frameworks: LangChain, LangGraph, CrewAI, AutoGen, Semantic Kernel, Haystack
>
> Workflow Automation: n8n, Make (Integromat), Zapier, Apache Airflow
>
> Vector Databases and RAG: Pinecone, Weaviate, Qdrant, pgvector, Chroma, LlamaIndex
>
> Programming: Python (primary), JavaScript/TypeScript, REST API design
>
> Cloud and MLOps: AWS, Azure, GCP, Docker, FastAPI, CI/CD for AI pipelines
>
> Observability and Evaluation: LangSmith, Helicone, Weights and Biases, custom evaluation harnesses
>
> AI Agent Focus Areas
>
>  - Autonomous and semi-autonomous agents for customer service, operations, marketing, and data analysis
>
>  - Multi-agent orchestration including planner, executor, critic, and memory agent patterns
>
>  - Knowledge retrieval systems including enterprise RAG, document Q&A, and semantic search
>
>  - Process automation integrating CRM, ERP, and communication tools end-to-end
>
>  - Agent safety, guardrails, and human-in-the-loop oversight mechanisms
>
>  - MCP server development for extending agent capabilities
>
> Soft Skills
>
>  - Strong problem-solving ability and analytical thinking
>
>  - Ability to translate complex business needs into practical technical solutions
>
>  - Effective collaboration and communication in a team-oriented environment
>
>  - Intellectual curiosity and commitment to staying current with AI research and trends
>
> Why Join Us?
>
>  - Work with one of the world’s leading financial derivatives institutions.
>
>  - Competitive salary plus performance-based incentives.
>
>  - Access to a dynamic, international, and fast-growing environment.
>
>  - Strong opportunities for career progression within a global financial group.
>
>  - Be part of a business committed to innovation, excellence, and long-term growth.
>
> Become part of our international community at MultiBank Group, dedicated to excellence, innovation, and shaping the future of finance.
>
> MultiBank Group is an equal opportunity employer. We welcome applications from candidates of all backgrounds and do not discriminate on the basis of nationality, gender, age, religion, or disability.

### LinkedIn posting (MultiBank Group)

> AI Engineer – Generative AI and Automation — MultiBank Group — Dubai, Dubai, United Arab Emirates — LinkedIn https://www.linkedin.com/jobs/view/4422417315 — Not Applicable, Full-time
>
> Welcome to MultiBank Group , a global financial pioneer established in 2005 in California and now proudly headquartered in Dubai, UAE. We specialize in delivering cutting-edge trading technology, unparalleled liquidity, and exceptional customer service. Our extensive range of financial products includes Forex, Metals, Shares, Indices, Commodities, and Cryptocurrency CFDs.
>
> Join our thriving community of over 2 million clients across 100 countries, contributing to a daily trading volume exceeding US$ 35 billion. As a heavily regulated institution with oversight from 18+ financial regulators across 5 continents, and recipient of over 80 financial awards, MultiBank Group is devoted to innovation, excellence, and empowering our clients to achieve their financial goals.
>
> Role Overview
>
> We are seeking an AI Engineer to design, build, and deploy intelligent AI agents and automated workflows that address real business problems. This is a hands-on, high-impact role within the Artificial Intelligence and Advanced Analytics team. The successful candidate will own end-to-end delivery of AI agents from scoping and architecture through integration, testing, and production deployment, enabling the organization to automate complex processes and unlock value from generative AI.
>
> Key Responsibilities
>
> Design, build, and deploy AI agents using frontier LLMs including Claude (Anthropic API), OpenAI, Gemini, and other frontier models
> Architect multi-agent systems and agentic workflows using frameworks including LangChain, LangGraph, CrewAI, AutoGen, and Semantic Kernel
> Build and manage automated business workflows using n8n, Make (Integromat), Zapier, and custom API integrations
> Implement RAG pipelines with vector databases including Pinecone, Weaviate, Qdrant, and pgvector to give agents access to organizational knowledge bases
> Design tool-use and function-calling integrations, connecting agents to internal systems, APIs, databases, and third-party services
> Fine-tune and prompt-engineer LLMs to optimize agent behavior, reliability, and task accuracy
> Collaborate with business stakeholders to identify automation opportunities and translate requirements into agent-based solutions
> Monitor, evaluate, and continuously improve deployed agents across quality, latency, cost, and safety metrics
> Establish and maintain best practices for agent safety, guardrails, human-in-the-loop controls, and responsible AI deployment
> Develop MCP (Model Context Protocol) server integrations to extend agent capabilities
>
> Requirements
>
> Bachelor's or Master's degree in Computer Science, Artificial Intelligence, Software Engineering, or a related field; equivalent practical experience will be considered
> 2 or more years of hands-on experience building production AI systems or intelligent automation solutions
> Demonstrated experience building agents or workflows with LangChain, LangGraph, CrewAI, n8n, or comparable frameworks
> Proven ability to integrate LLM APIs including Anthropic Claude and OpenAI into real-world applications
> Experience with vector databases and semantic search implementations is strongly preferred
> Portfolio or demonstrable projects showing deployed agents, automation workflows, or RAG-based applications
> Proficiency in Python as the primary language; JavaScript or TypeScript is beneficial
> Familiarity with cloud platforms, Docker, FastAPI, and CI/CD practices for AI pipelines
>
> Technical Skills
>
> LLM APIs : Anthropic Claude (claude-opus-4, claude-sonnet-4), OpenAI GPT-4o, Google Gemini, Mistral
>
> Agent Frameworks : LangChain, LangGraph, CrewAI, AutoGen, Semantic Kernel, Haystack
>
> Workflow Automation: n8n, Make (Integromat), Zapier, Apache Airflow
>
> Vector Databases and RAG: Pinecone, Weaviate, Qdrant, pgvector, Chroma, LlamaIndex
>
> Programming: Python (primary), JavaScript/TypeScript, REST API design
>
> Cloud and MLOps: AWS, Azure, GCP, Docker, FastAPI, CI/CD for AI pipelines
>
> Observability and Evaluation: LangSmith, Helicone, Weights and Biases, custom evaluation harnesses
>
> AI Agent Focus Areas
>
> Autonomous and semi-autonomous agents for customer service, operations, marketing, and data analysis
> Multi-agent orchestration including planner, executor, critic, and memory agent patterns
> Knowledge retrieval systems including enterprise RAG, document Q&A, and semantic search
> Process automation integrating CRM, ERP, and communication tools end-to-end
> Agent safety, guardrails, and human-in-the-loop oversight mechanisms
> MCP server development for extending agent capabilities
>
> Soft Skills
>
> Strong problem-solving ability and analytical thinking
> Ability to translate complex business needs into practical technical solutions
> Effective collaboration and communication in a team-oriented environment
> Intellectual curiosity and commitment to staying current with AI research and trends
>
> Why Join Us?
>
> Work with one of the world’s leading financial derivatives institutions.
> Competitive salary plus performance-based incentives.
> Access to a dynamic, international, and fast-growing environment.
> Strong opportunities for career progression within a global financial group.
> Be part of a business committed to innovation, excellence, and long-term growth.
>
> Become part of our international community at MultiBank Group, dedicated to excellence, innovation, and shaping the future of finance.
>
> MultiBank Group is an equal opportunity employer. We welcome applications from candidates of all backgrounds and do not discriminate on the basis of nationality, gender, age, religion, or disability.
