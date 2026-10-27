# Machine Learning Engineer, Human-AI Interaction — XenonStack (Alexandria, Egypt)

- **Posting:** LinkedIn job 4472285181 (https://www.linkedin.com/jobs/view/4472285181), posted 26 Sep 2026, still live on 27 Oct. Full-time, Alexandria.
- **Apply:** open the link and tap **Apply**. Upload `Ahmed_Dorra_CV_XenonStack.pdf` and paste the note below if asked.
- **Verdict: apply.** It's in Egypt, so there's no visa issue.
  - The role is prompt engineering, context design and memory, RAG with vector databases, and LangChain/LangGraph. That's close to your work.
  - They ask for 2–4 years. Your projects cover the skills, so it's worth sending.
  - **Gaps (not claimed):** knowledge-graph integration, LlamaIndex, MCP/A2A, RLHF, and enterprise governance work.
  - **Check first:** Alexandria is a 3-hour commute from Giza, so ask whether the role is hybrid or remote, or plan to relocate.
- **Company check: no red flags.** XenonStack is an established data and AI company (Akira AI, ElixirData, NexaStack, MetaSecure). The listing is under "XenonStack Moments". It asks for no fee.

---

## Note to paste

Hello XenonStack team,

I'm applying for the Machine Learning Engineer, Human-AI Interaction role in Alexandria. Much of my work is exactly this layer: designing prompts and structured outputs, assembling context from hybrid-search RAG, giving LangGraph agents tools and memory, and proving each change with a code-graded test suite and Langfuse traces. A revised prompt took my Shopping Assistant agent from 7 to 12 of 12 test tasks with 29% fewer paid rerank calls. I'm based in Giza; could you tell me whether the role is on site in Alexandria, hybrid or remote?

GitHub: github.com/AhmedMostafa167
Portfolio: ahmedmostafa167.github.io
LinkedIn: linkedin.com/in/ahmed-mostafa-dorra

Best regards,
Ahmed Dorra
+20 100 614 8440 · newahmed1672022@gmail.com

---

## Interview prep

- **Walk through the Shopping Assistant:** the LangGraph graph (nodes, tool calls, conditional routing, bounded retries), where state lives (Postgres checkpointer vs typed facts in PostgreSQL), and why memory is typed facts rather than vectors.
- **Evaluation:** the 12 tasks × 3 runs code-graded suite; prompt v2 went from 7 to 12 of 12 with 29% fewer paid rerank calls; v3 moved price and rating limits inside search (57/81 → 48/48 matching).
- **Retrieval:** hybrid vs keyword vs vector (72% / 56% / 41% top-10 recall on 127 labelled queries), reranking 23% → 43%, HNSW 35 ms → 3.1 ms.
- **Failure handling:** what happens when a tool errors, the model returns invalid JSON (Pydantic validation and retry), or the user tries to plant a false "fact" (memory-write guardrails, 0 of 21 legitimate facts refused).
- **Context windows:** how you decide what goes into the prompt (retrieved top-k after reranking, typed user facts, recent turns), and what you'd do as conversations grow (summarise, trim, retrieve on demand).
- **Knowledge graphs (gap):** know the idea of GraphRAG (entities and relations as a graph, traversed alongside vector search) and when it helps (multi-hop questions).
- **Ask them:** which product (Akira AI?), the team in Alexandria, and the work setup.

---

## Original post

> Machine Learning Engineer, Human-AI Interaction — XenonStack Moments — Abes 7-8-10, Alexandria, Egypt — LinkedIn https://www.linkedin.com/jobs/view/4472285181 — Not Applicable, Full-time
>
> About Xenonstack
>
> XenonStack is a Data and AI Foundry for Agentic Systems, enabling enterprises to design, deploy, operate, and scale intelligent agents across digital and physical environments.
>
> We Build Enterprise-grade Platforms Across The Agentic Stack
>
> Akira AI — Reasoning and agent orchestration. Turn models into collaborative, policy-governed agents that learn and act together.
> ElixirData — Agentic analytics intelligence. Explainable, decision-centric analytics for measurable business outcomes.
> NexaStack — Agentic infrastructure automation. Secure, compliant AI deployment across cloud, edge, and on-prem.
> MetaSecure — Trust, compliance and defense. Continuous assurance with AI-BOMs, risk scoring, and agentic security.
>
> Our mission is to accelerate the world’s transition to AI + Human Intelligence by making agentic systems reliable, responsible, and enterprise-ready.
>
> THE OPPORTUNITY
>
> We are seeking an Machine Learning Engineer, Human-AI Interaction to design, implement, and optimize the way AI agents understand, respond, and act within enterprise workflows .
>
> This role sits at the intersection of linguistics, context engineering, and enterprise AI systems . You will blend prompt engineering, context orchestration, and memory architecture to ensure large language models (LLMs) and multi-agent systems are accurate, reliable, and compliant in production.
>
> If you are passionate about making AI smarter, context-aware, and enterprise-ready , this role is for you.
>
> Key Responsibilities
>
> Prompt Engineering – Design, test, and refine prompt strategies to drive optimal agent behavior across diverse use cases.
> Context Orchestration – Build pipelines integrating RAG, knowledge graphs, APIs, and layered memory (short-term, long-term, episodic).
> Optimization – Optimize token usage and context allocation for long-running, multi-turn, and multi-agent workflows.
> Reusable Blueprints – Develop reusable interaction templates and context blueprints for engineering and product teams.
> Compliance & Guardrails – Implement safety, compliance, tone, and brand guardrails in agent workflows.
> Continuous Improvement – Use execution traces, feedback, and automated evaluation to improve agent responses.
> Experimentation – Conduct A/B testing on prompt and context variations to measure accuracy, latency, and cost trade-offs.
> Knowledge Management – Maintain a central library of tested interaction patterns and context management strategies.
> Research Tracking – Stay updated on multi-agent orchestration frameworks and the state of AI interaction design.
>
> Skills & Qualifications
>
> Must-Have
>
> 2–4 years in AI/ML engineering, NLP, or enterprise software development.
> Strong understanding of LLM architectures, prompt engineering, and context window limits.
> Hands-on with RAG pipelines, vector databases, and knowledge graph integration.
> Proficiency in Python and frameworks like LangChain, LangGraph, LlamaIndex.
> Familiarity with enterprise AI governance, privacy, and compliance standards.
> Proven ability to translate business objectives into structured AI interactions.
>
> Good-to-Have
>
> Experience with multi-agent orchestration (MCP, A2A messaging, AgentBridge).
> Knowledge of reinforcement learning (RLHF, RLAIF, reward modeling).
> Exposure to edge AI deployment and quantized inference.
> Domain knowledge in BFSI, GRC, SOC, or FinOps.
>
> WHY SHOULD YOU JOIN US?
>
> Agentic AI Product Company
>
> Build enterprise-grade AI platforms powered by Machine Learning, Generative AI, and Agentic Systems. From Vision AI to Inference Infrastructure, you’ll shape products that redefine enterprise AI adoption.
>
> A Fast-Growing Category Leader
>
> XenonStack is one of the fastest-growing Data and AI Foundries , setting benchmarks in how businesses deploy and scale AI agents with platforms like Akira AI, NexaStack, and Vision AI .
>
> Career Mobility & Growth
>
> Move between roles and functions — from AI Engineering to Model Ops, AgentOps, or Systems Architecture — and craft a career that grows with your aspirations.
>
> Global Exposure
>
> Work with Fortune 500 enterprises, BFSI leaders, and global innovators , delivering real-world impact across industries and geographies.
>
> Create Real Impact
>
> Contribute from day one. Even mid-level engineers design mission-critical interaction patterns that go directly into production.
>
> Culture of Excellence
>
> Our values — Agency, Taste, Ownership, Mastery, Impatience, and Customer Obsession — empower you to push boundaries and innovate fearlessly.
>
> Responsible AI First
>
> Join a company that prioritizes trustworthy, explainable, and compliant AI . You’ll contribute to Responsible AI frameworks ensuring our agentic systems are not just powerful, but also ethical and reliable.
>
> XENONSTACK CULTURE – JOIN US & MAKE AN IMPACT!
>
> At XenonStack, we believe in shaping the future of intelligent systems . We foster a culture of cultivation built on bold, human-centric leadership principles, where deep work, simplicity, and adoption define everything we do.
>
> Our Cultural Values
>
> Agency – Be self-directed and proactive.
> Taste – Sweat the details and build with precision.
> Ownership – Take responsibility for outcomes.
> Mastery – Commit to continuous learning and growth.
> Impatience – Move fast and embrace progress.
> Customer Obsession – Always put the customer first.
>
> Our Product Philosophy
>
> Obsessed with Adoption – Making AI accessible and enterprise-ready.
> Obsessed with Simplicity – Turning complexity into seamless, intuitive AI experiences.
>
> Be a part of our mission to accelerate the world’s transition to AI + Human Intelligence and reimagine how enterprises interact with AI agents.
