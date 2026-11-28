# 28 Nov 2026 batch: Ali Turky's lists

15 new jobs added as Ready to send (#1–#15; TP added as #9 after the repost check, so the rows after it moved down one). One section per job below.

## Already in the tracker or closed (not re-added)

| From the list | Status |
|---|---|
| Vertex Technologies, Junior Data Engineer | Already Ready to send (#131) |
| Capgemini YPP Associate AI Engineer | **Position filled**: row moved to Withdrawn |
| Provectus Junior AI/ML Engineer | **No longer accepting applications**: row moved to Withdrawn |
| Arabic.AI (Tarjama&) AI Engineer | Applied twice (16 Oct, 8 Nov) |
| PwC ETIC AI Engineer Associate / Data Science Associate | Applied 29 Oct (same requisitions) |
| SDG Group AI/LLM Engineer (LangGraph) | Applied 27 Nov |
| Orascom Digital Transformation Associate (El Gouna AI Lab) | Applied 27 Nov |
| Numrah ML Engineer | Applied 27 Nov |
| Lamdax Fresh Graduate AI Engineer | Applied 4 Nov |
| Smarterminds AI Engineer Intern | Applied 17 Oct |
| Finalyze ML Intern (Arabic NLP) | Already Ready to send (#117) |
| TP AI & Automation Analyst | **New repost** (1-3 yrs; old 3-4 yr post closed): added as #9, see `2026-11-28-tp-ai-automation-analyst.md` |
| Forasna Deep Learning & Full-Stack (6th of October) | Closed ("this job is closed", 3 months old) |

## Agentic AI Engineer (junior, 2 openings) — Forsa Property

- **Location:** New Cairo (hybrid)
- **Posting:** https://forsaprop.com/en/careers/agentic-ai-engineer/
- **Source:** Ali Turky list (company careers page)
- **CV:** `Ahmed_Dorra_CV_Forsa_Property.pdf` (variant `cv/variants/forsa_property.py`)
- **Tracker id:** `2026-11-28-forsa-property-agentic-ai-engineer` (priority #1)

### Verdict
**Apply.** Junior, hybrid in New Cairo, and the asks (Python, LLMs, vector DBs and embeddings, agent frameworks, RAG) are exactly the shopping assistant. Only gap: AutoGen (you use LangGraph/LangChain).

### Company check
Egyptian property portal (forsaprop.com, domain registered May 2025), lists real compounds and developers, Arabic/English site. Young but real; no fees asked.

### How to apply
Open the link → **Apply Now** → upload `Ahmed_Dorra_CV_Forsa_Property.pdf`. Paste the note below if there's a message box.

### Note to paste
```
Hello, I'm applying for the Agentic AI Engineer position at Forsa Property. Your post asks for LLM agents, RAG pipelines and vector databases for real estate. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, available to start immediately, and can commute to New Cairo. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Walk through the shopping assistant's agent loop: tools, memory, hybrid search; why LangGraph.
- How would you build a property-search agent? (constraints like budget/area inside the SQL search, not after it: the 70%→100% fix)
- Vector DB choice: pgvector + HNSW (35 ms → 3.1 ms) vs Chroma (Research Assistant).
- AutoGen vs LangGraph: say you haven't used AutoGen; explain the multi-step graph you built.

### Original post

> At a Glance
> Department
> Technology
> Location
> Mohammed Nagib Axis, New Cairo
> Work Type
> Full-time
> Workplace
> Hybrid
> Seniority
> Junior
> Openings
> 2
> Job Description
> Join our team to build cutting-edge AI agents and autonomous systems. Work with LLMs, RAG pipelines, and multi-agent architectures to create intelligent solutions for the real estate industry.
> Full Requirements
> Strong Python programming skills
> Experience with LLMs (GPT, Claude, etc.)
> Knowledge of vector databases and embeddings
> Familiarity with agent frameworks (LangChain, AutoGen, etc.)
> Problem-solving mindset and ability to learn quickly


---

## AI Engineer (agent orchestration) — The HR Game (for a banking client)

- **Location:** Cairo
- **Posting:** https://eg.linkedin.com/jobs/view/4494141920
- **Source:** Ali Turky list (LinkedIn)
- **CV:** `Ahmed_Dorra_CV_The_HR_Game.pdf` (variant `cv/variants/hr_game.py`)
- **Tracker id:** `2026-11-28-the-hr-game-ai-engineer` (priority #2)

### Verdict
**Apply.** Agent orchestration, tool calling, agent evaluation, retries and failure recovery: all in your LangGraph agent with its code-graded evaluation. LinkedIn tags it Mid-Senior but no years are stated. Banking is a nice-to-have.

### Company check
Egyptian HR/recruitment firm (thehrgame.com, since 2023) hiring for a banking client; 200+ applicants on LinkedIn, so apply soon.

### How to apply
Open the LinkedIn link → **Apply** (Easy Apply or their form) → upload `Ahmed_Dorra_CV_The_HR_Game.pdf`. If there's a note field, paste the note.

### Note to paste
```
Hello, I'm applying for the AI Engineer position at The HR Game. Your post centres on agent orchestration, tool calling and evaluating agent reliability; that's the core of my recent work. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, available to start immediately, and can commute to anywhere in Cairo. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Human approval checkpoints: how you'd add an interrupt/approve step in LangGraph before a risky tool call.
- Retries and failure recovery: bounded retries, the Research Assistant's self-correcting loop, guardrails.
- Agent evaluation: 12 tasks × 3 runs, code-graded; v2 12/12 vs 7 with 29% fewer paid calls.
- Access control / data privacy: per-user memory scoping, MAX_FACTS_PER_USER, refusing ungrounded prices (25/25).

### Original post

> Design and implement AI agents that coordinate tools, workflows, and Large Language Models (LLMs) to automate and execute controlled business tasks.
> The role involves designing agent orchestration and tool-calling workflows, integrating APIs and enterprise systems, managing agent execution, and implementing security controls and human approval checkpoints.
> The AI Agent Engineer will also evaluate agent performance, monitor execution, troubleshoot failures, and ensure reliable, secure, and efficient AI-driven solutions.
> Requirements
> Bachelor's degree in Computer Science, Engineering, Data Science, Mathematics, Statistics, Information Systems, or a related field
> Hands-on experience with Python programming
> Strong understanding of Large Language Models (LLMs) and LLM APIs
> Experience with AI Agent development and orchestration
> Knowledge of tool calling, workflow design, and API integrations
> Experience in evaluating AI agent performance, reliability, and task completion
> Understanding of state management, error handling, retries, and failure recovery
> Knowledge of access control, data privacy, and secure system design
> Strong analytical, problem-solving, and communication skills
> Ability to collaborate with technical and business teams
> Nice to Have:
> Experience with cloud platforms, MLOps, and enterprise integrations
> Previous experience in banking or financial services environments


---

## NLP Engineer — Multilingual (French / Arabic / Swahili) — Kilwa Technologies

- **Location:** Remote (full-time)
- **Posting:** https://www.kilwa.io/careers/nlp-engineer-multilingual
- **Source:** Ali Turky list (company careers page)
- **CV:** `Ahmed_Dorra_CV_Kilwa.pdf` (variant `cv/variants/kilwa.py`)
- **Tracker id:** `2026-11-28-kilwa-nlp-engineer-multilingual` (priority #3)

### Verdict
**Apply.** Remote full-time NLP role that needs fluency in Arabic *or* French *or* Swahili, so your native Arabic plus the AraBERT classifier (dialect results, grouped split against leakage) is a direct fit. They want a short note on what you'd own and links to shipped work.

### Company check
Chicago-based, remote-first; site lists 9 roles, published research briefs, partners, US SBA SDVOSB certification. kilwa.io registry date not public (.io RDAP). No fees asked.

### How to apply
Email **info@kilwa.io** · Subject: `NLP Engineer — Multilingual (Arabic): Ahmed Dorra` · attach `Ahmed_Dorra_CV_Kilwa.pdf` · body below.

### Email
```
Hello Kilwa team,

I'm applying for the NLP Engineer — Multilingual role. I'm a native Arabic speaker and I build Arabic NLP systems directly in the source language. My latest project fine-tunes AraBERT on 77 Arabic banking intents (macro-F1 0.919 vs 0.887 for TF-IDF) and reports dialect-level results on Saudi, Moroccan and Tunisian text the model never saw. I found that the official validation split leaked paraphrases into training, rebuilt it as a grouped split, and gated promotion in the MLflow registry on a paired bootstrap; the model runs as ONNX behind a monitored FastAPI API.

What I'd want to own: Arabic sentiment and policy-signal extraction, starting with a labelled evaluation set per region and register (Gulf vs North African media), so every model change is measured against translate-first baselines.

Work I've shipped:
- Arabic Banking Intent Classifier: github.com/AhmedMostafa167/arabic_banking_intent
- Shopping Assistant (LLM agent + hybrid RAG, measured on 127 labelled queries): github.com/AhmedMostafa167/Shopping-Assistant
- Portfolio: ahmedmostafa167.github.io

I'm in Egypt, available to start immediately, and happy to work US hours. CV attached.

Best regards,
Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com · linkedin.com/in/ahmed-mostafa-dorra
```

### Interview prep
- Why translation pipelines lose nuance: negation, hedging, dialect words, named entities; your answer: evaluate natively per register.
- Low-resource tricks: multilingual encoders (AraBERT/XLM-R), grouped splits, small labelled sets with confidence intervals.
- Be honest: no French/Swahili; Arabic is your lane.
- Sentiment vs intent: same fine-tuning recipe; what changes is labels and evaluation.

### Original post

> NLP Engineer — Multilingual (French / Arabic / Swahili)
> Own the capability almost nobody else in this market has: reading the languages African investment decisions are actually made in.
> LOCATION
> Remote
> TYPE
> Full-time
> TEAM
> Engineering
> What you'll do
> Build and improve sentiment and policy-signal extraction natively in French, Arabic and Swahili.
> Keep nuance intact by processing source languages directly rather than translating to English first.
> Expand regional source coverage and adapt models to region-specific media registers.
> Feed Sentiment Pulse output into the ISI and METI models as a first-class input.
> What you bring
> Multilingual NLP experience, ideally in lower-resource language settings.
> Working fluency in at least one of French, Arabic or Swahili.
> An understanding of where translation pipelines quietly destroy policy nuance.
> How to apply
> Email us with your CV and a short note on what you'd want to own here. Links to work you've shipped are worth more than a cover letter.
> Apply for this role


---

## Junior AI & LLM Engineer — Eurosoft LLC

- **Location:** Remote (hybrid in Tashkent optional)
- **Posting:** https://www.eurosoft.uz/careers/junior-ai-llm-engineer
- **Source:** Ali Turky list (company careers page)
- **CV:** `Ahmed_Dorra_CV_Eurosoft.pdf` (variant `cv/variants/eurosoft.py`)
- **Tracker id:** `2026-11-28-eurosoft-junior-ai-llm-engineer` (priority #4)

### Verdict
**Apply.** Junior, remote, "up to 2 years or strong projects", and the stack is RAG, embeddings, vector search, answer-quality evaluation. Open until 24 Jan 2027. Gap: OCR (don't claim it). Russian/Uzbek is only a plus.

### Company check
Tashkent software company since 2019 (eurosoft.uz registered Dec 2018), IT Park resident, 120+ projects, named clients. No fees.

### How to apply
Use **only the form** on the page (they blacklist email/LinkedIn applications) → upload `Ahmed_Dorra_CV_Eurosoft.pdf`; paste the note in any message field.

### Note to paste
```
Hello, I'm applying for the Junior AI & LLM Engineer position at Eurosoft LLC. Your post asks for RAG, embeddings, vector search and evaluating answer quality; that's what my projects measure. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, Egypt, available to start immediately, and happy to work remotely in any time zone. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Answer-quality evaluation: 127 labelled queries with 95% CIs; RAGAS/LLM-as-judge in the Research Assistant; prices_grounded check.
- Hosted vs open models: Groq/Cohere/OpenAI/Anthropic provider switch in the Research Assistant.
- PDF handling: say you've parsed text documents but not OCR.

### Original post

> Junior AI & LLM Engineer
> Build RAG pipelines, AI assistants and agents on top of open and hosted LLMs.
> Remote
> Engineering · Junior
> Full-time · Junior
> Remote-first · hybrid in Tashkent possible
> Apply for this role
> WHAT WE LOOK FOR
> Up to 2 years of experience, or strong personal or university projects
> Python and the LLM ecosystem (OpenAI or Anthropic APIs, open models)
> RAG: embeddings, vector search and prompt design
> Evaluating answer quality and handling documents (PDF, OCR)
> Eager to learn through code review and mentoring
> Good written English; Russian or Uzbek is a plus
> WHAT WE OFFER
> Remote-first: work from anywhere, or hybrid with our office in Tashkent
> Real products: private LLM and RAG platforms, AI assistants and enterprise systems for clients in Uzbekistan, South Korea and the UAE
> Mentoring and code review from senior engineers
> Market-level salary in USD, based on your experience
> KEY FACTS
> Work mode
> Remote. We are a remote-first company; hybrid with our Tashkent office is also possible.
> Location
> Remote-first · hybrid in Tashkent possible
> Level and type
> Full-time · Junior
> Team
> Engineering · Junior
> Open until
> 24 January 2027
> Posted
> 26 October 2026
> Apply for this role


---

## AI/ML Engineer — Arabic NLP + LLMs + Applied AI (contract) — Cube Master

- **Location:** Remote (Saudi company)
- **Posting:** https://cm.sa/en/careers/aiml-engineer/
- **Source:** Ali Turky list (company careers page)
- **CV:** `Ahmed_Dorra_CV_Cube_Master.pdf` (variant `cv/variants/cube_master.py`)
- **Tracker id:** `2026-11-28-cube-master-ai-ml-engineer-arabic-nlp` (priority #5)

### Verdict
**Apply.** Arabic LLM assistants and tutors, Hugging Face, LangChain, agent design and LoRA fine-tuning fit you well, and you're a native speaker. Gaps: speech (ASR/TTS), quantization/distillation; say you haven't done them. Contract/long-term collaboration.

### Company check
Saudi software house in Al Mubarraz (CR 2251491915 on the site), apps/web/AI services, Arabic/English site. No fees.

### How to apply
Fill the form on the page: Experience → **Fresh-graduate** (or 1-3 years if you count projects), Nationality Egyptian, Location Giza, Degree Bachelor, Major Computer Science, heard via **other job websites**, attach `Ahmed_Dorra_CV_Cube_Master.pdf` (under 2 MB). Paste the skills text below into "most important skills".

**"Most important skills" field:**
```
Arabic NLP and LLM applications in Python: fine-tuned AraBERT on 77 Arabic banking intents (macro-F1 0.919, dialect results on Saudi, Moroccan and Tunisian), served as ONNX behind a monitored FastAPI API; LangGraph/LangChain agents with tool calling and long-term memory; hybrid RAG with reranking; LoRA fine-tuning (Hugging Face); evaluation with labelled test sets; Docker, PostgreSQL, MLflow. Native Arabic speaker; I teach 700+ students.
```

### Note to paste
```
Hello, I'm applying for the AI/ML Engineer — Arabic NLP + LLMs + Applied AI position at Cube Master. Your post asks for Arabic NLP, LLM agents and fine-tuned open models, and I'm a native Arabic speaker. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, Egypt, available to start immediately, and happy to work remotely in any time zone. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Arabic tutor design: retrieval over curriculum, dialect handling, evaluation set of student questions.
- LoRA: you used it in VISIONEER (with a colleague) — explain rank/alpha, why it's cheap.
- Speech: be honest; you'd call Whisper for STT and a TTS API, but you haven't shipped it.
- Serving efficiency: ONNX fp16 (2.26 GB → 0.95 GB image, 670 → 530 ms median).

### Original post

> We’re Hiring: AI/ML Engineer | Arabic NLP + LLMs + Applied AI
> 📍 Remote | 🕓 Contract / Long-Term Collaboration
> We’re building a portfolio of cutting-edge AI-driven products that combine Arabic language understanding, large language models (LLMs), and interactive voice and education technologies. From personalized tutoring systems to intelligent automation, our projects are ambitious, impactful, and production-focused.
> We're looking for a highly skilled AI/ML engineer who can design, build, and optimize end-to-end AI systems — not just prototypes, but real-world applications used by people every day.
> Requirements
> AI-powered Arabic-speaking assistants and tutors (LLM-based)
> Voice-enabled interactive apps using ASR/TTS and real-time reasoning
> Educational and domain-specific agents with strong personalization
> Scalable AI services optimized for responsiveness and efficiency
> Skills
> Strong experience in machine learning and NLP, with emphasis on LLMs
> Proven ability to work with Arabic language models or multilingual NLP
> Proficiency in Python, Hugging Face Transformers, LangChain, or similar frameworks
> Experience integrating speech-to-text (Whisper, Vosk, etc.) and text-to-speech (TTS)
> Deep understanding of prompt engineering, context management, and agent design
> Ability to evaluate, fine-tune, or deploy open-source models like Jais, Mistral, AraT5, DeepSeek, Phi-3, and others
> Experience with model optimization (quantization, LoRA, distillation) for deployment
> Comfortable in agile, collaborative environments with a problem-solving mindset


---

## Junior AI Technology Engineer — Investia Venture Capital

- **Location:** New Cairo (on-site)
- **Posting:** https://wuzzuf.net/jobs/p/gv1msetmo0bw-junior-ai-technology-engineer-investia-venture-capital-cairo-egypt
- **Source:** Ali Turky list (Wuzzuf)
- **CV:** `Ahmed_Dorra_CV_Investia.pdf` (variant `cv/variants/investia.py`)
- **Tracker id:** `2026-11-28-investia-junior-ai-technology-engineer` (priority #6)

### Verdict
**Apply.** Junior AI role in Cairo; 1-3 years preferred but fresh grads may be considered. Wuzzuf blocks automated reads, so this CV is built from Ali's summary: paste the post text to me if you want it tightened.

### Company check
Not verified (Wuzzuf blocked; no site found). Normal caution: no fees or ID before an offer.

### How to apply
Open the Wuzzuf link → **Apply** → upload `Ahmed_Dorra_CV_Investia.pdf`; answer the screening questions (answer bank) and paste the note if asked.

### Note to paste
```
Hello, I'm applying for the Junior AI Technology Engineer position at Investia Venture Capital. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, available to start immediately, and can commute to New Cairo. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Read the full Wuzzuf post before the interview: VC firms often want AI for deal screening/document analysis.
- Pitch: RAG over company documents + evaluation, using the shopping assistant numbers.

### Original post

> (Not readable automatically: summary from Ali Turky's list.)


---

## Data Scientist (Fresh Graduate) — Dice Group

- **Location:** Helwan, Cairo (on-site)
- **Posting:** https://wuzzuf.net/jobs/p/tqzmxkgamxgb
- **Source:** Ali Turky list (Wuzzuf)
- **CV:** `Ahmed_Dorra_CV_Dice_Group.pdf` (variant `cv/variants/dice_group.py`)
- **Tracker id:** `2026-11-28-dice-group-data-scientist-fresh-graduate` (priority #7)

### Verdict
**Apply.** Fresh-graduate data scientist, 0 years, in Cairo. Built from Ali's summary (Wuzzuf blocks automated reads); send me the text if you want it tighter.

### Company check
Not verified (Wuzzuf blocked). Normal caution: no fees or ID before an offer.

### How to apply
Open the Wuzzuf link → **Apply** → upload `Ahmed_Dorra_CV_Dice_Group.pdf`.

### Note to paste
```
Hello, I'm applying for the Data Scientist position at Dice Group. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, available to start immediately, and can commute to Helwan. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Classic DS questions: imbalanced metrics (F1), cross-validation, leakage (your grouped split story), feature engineering.
- The churn-model course you teach (preprocessing, linear model, MLflow) is good evidence.

### Original post

> (Not readable automatically: summary from Ali Turky's list.)


---

## ML Engineer Intern — FortyGuard

- **Location:** Remote
- **Posting:** https://forms.gle/Vx9UFNk6hNKukiqR6
- **Source:** Ali Turky list (Google Form)
- **CV:** `Ahmed_Dorra_CV_FortyGuard.pdf` (variant `cv/variants/fortyguard.py`)
- **Tracker id:** `2026-11-28-fortyguard-ml-engineer-intern` (priority #8)

### Verdict
**Apply (backup: internship).** Real climate-tech startup (urban temperature data and API). The form needs a Google sign-in, so I couldn't read the questions; built an ML/MLOps CV.

### Company check
FortyGuard Inc.: offices in Washington DC, San Jose and Hub71 Abu Dhabi; fortyguard.com since 2019; public API/MCP products. Legit.

### How to apply
Open the form (sign in with Google) → fill it → upload `Ahmed_Dorra_CV_FortyGuard.pdf`. Send me any open questions.

### Note to paste
```
Hello, I'm applying for the ML Engineer Intern position at FortyGuard. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, Egypt, available to start immediately, and happy to work remotely in any time zone. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Their product: hyperlocal temperature prediction; think time-series/geospatial regression, data quality, serving an API.
- Your serving story: FastAPI + ONNX + Prometheus/Grafana + drift alert.

### Original post

> (Not readable automatically: summary from Ali Turky's list.)


---

## Junior AI Engineer (part-time ~20 h/week) — IQ Vector AI

- **Location:** Remote (everywhere)
- **Posting:** https://wellfound.com/jobs/5044732-junior-ai-engineer
- **Source:** Ali Turky list (Wellfound)
- **CV:** `Ahmed_Dorra_CV_IQ_Vector_AI.pdf` (variant `cv/variants/iq_vector.py`)
- **Tracker id:** `2026-11-28-iq-vector-ai-junior-ai-engineer` (priority #9)

### Verdict
**Apply (backup).** Remote, early-career, Python/SQL/LLM pipelines and multi-agent work; part-time (~20 h/week, GBP 18k listed), so it can run alongside the TA job.

### Company check
London startup, 1-10 people, founder named on Wellfound; iqvector.ai registered Jan 2026 (young). The form adds you to a 24-month talent pool. No fees; don't send ID documents.

### How to apply
Fill the form: https://baserow.io/form/5dGFgfNPjhbG9qpSw8A3yGNK72vJQkGmkr__j_qmyn8 — Country **Egypt**; links `https://github.com/AhmedMostafa167, https://ahmedmostafa167.github.io, https://www.linkedin.com/in/ahmed-mostafa-dorra`; Education `Culture and Science City, Giza — BSc Computer Science (Graduated 2024)`; Availability **Both**. A CodeSignal test follows by email. Keep `Ahmed_Dorra_CV_IQ_Vector_AI.pdf` for when they ask.

### Note to paste
```
Hello, I'm applying for the Junior AI Engineer position at IQ Vector AI. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, Egypt, available to start immediately, and happy to work remotely in any time zone. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- CodeSignal: practise Python + SQL problems (arrays, hash maps, joins/group-by).
- Validating AI-generated code: tests first (104 tests), CI, review.

### Original post

> About the Role
> IQ Vector AI is hiring early-career talents and junior engineers (BSc, MSc, and PhD students or recent graduates in Machine Learning, Data Science, Computer Science, or Mathematics) for our core team and global B2B technology partners.
> You will work directly with the CEO and company founders with zero corporate hierarchy, solving concrete, high-impact business and engineering challenges every day. We operate an AI-native engineering environment: you will orchestrate swarms of AI agents to build, automate, and analyze faster, while rigorously verifying and validating all AI-generated code and technical outputs.
> Responsibilities
> • Work side-by-side with the CEO and founding team on daily B2B product, operational, growth, and technical Go-To-Market challenges.
> • Build and administer automated AI pipelines, databases, webhooks, and data intelligence graphs using Python, SQL, and LLMs.
> • Orchestrate multi-agent workflows and rigorously test and validate AI-generated code for production reliability.
> • Engineer algorithmic sourcing engines, analytics pipelines, and rapid enterprise AI prototypes.
> Requirements
> • Strong academic or practical foundation in Machine Learning, Data Science, Computer Science, or Mathematics (advanced students and recent graduates welcome).
> • Hands-on proficiency with Python, SQL, and daily use of modern AI and multi-agent coding tools.
> • Availability for remote part-time collaboration (~20 hours/week, min. 4 hours/day, 6+ months), flexible around university schedules.
> • Strong working proficiency in English.
> What We Offer
> • Direct mentorship and daily collaboration with the CEO and serial technology founders, with real responsibility from day one.
> • Pure commercial B2B AI & Data projects with competitive international compensation and flexible remote hours.
> Application Process: Please complete our candidate form at https://baserow.io/form/5dGFgfNPjhbG9qpSw8A3yGNK72vJQkGmkr__j_qmyn8
> Apply Now


---

## Intern – AI Engineer (stipend) — Shivante Solutions

- **Location:** Remote (Chennai company)
- **Posting:** https://careers.shivante.com/jobs/intern-ai-engineer
- **Source:** Ali Turky list (company careers page)
- **CV:** `Ahmed_Dorra_CV_Shivante.pdf` (variant `cv/variants/shivante.py`)
- **Tracker id:** `2026-11-28-shivante-ai-engineer-intern` (priority #10)

### Verdict
**Apply (backup: internship, stipend).** The work is RAG + tool calling + response evaluation, a strong match. Indian statutory knowledge and OCR are preferred only.

### Company check
Indian private limited company in Chennai with address and phone; shivante.com registered Oct 2025 (young). No fees.

### How to apply
Open the link → **Apply for this position** (about 5 minutes, no account) → upload `Ahmed_Dorra_CV_Shivante.pdf` and paste the note.

### Note to paste
```
Hello, I'm applying for the Intern – AI Engineer position at Shivante Solutions. Your post asks for RAG, tool calling with well-scoped tool schemas and response evaluation; I've built and measured all three. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, Egypt, available to start immediately, and happy to work remotely in any time zone. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Tool schema design: the v3 change that moved price/rating limits into search parameters (70% → 100%).
- Chunking long legal text: section-aware chunks, metadata for act/version, hybrid search for exact clause numbers.

### Original post

> About the role
> We are building an AI-powered knowledge assistant designed for finance and compliance professionals. As an AI Engineering Intern, you will play a central role in shaping how this assistant understands, retrieves, and responds to queries grounded in Indian statutory and regulatory frameworks.
> This is a hands-on role. You will work directly with real-world regulatory data, LLM pipelines, tool-calling systems, and an internal platform that keeps the knowledge base current and accurate. You will have meaningful ownership from day one and work closely with the founding team.
> Responsibilities
> Collect, clean, and structure statutory and regulatory documents (acts, rules, circulars, notifications, amendments) relevant to Indian finance and compliance domains
> Build and maintain a retrieval-augmented generation (RAG) pipeline to power the AI assistant
> Implement tool calling capabilities so the chatbot can perform actions beyond retrieval — such as looking up live data, triggering calculations, or querying external APIs based on user intent
> Define, test, and version tool schemas; ensure the model selects and invokes the right tool reliably across varied query types
> Develop and improve chunking, embedding, and indexing strategies for large legal and regulatory texts
> Design and contribute to an internal content management interface that allows non-technical users to add, update, or deprecate regulatory content without engineering involvement
> Work with the product team to define how the chatbot handles ambiguous queries, multi-act references, and version-specific answers
> Evaluate chatbot responses for factual accuracy and coverage gaps; iterate on prompts and retrieval logic accordingly
> Document data sources, update workflows, and pipeline decisions
> Requirements
> Pursuing or recently completed a degree in Computer Science, Engineering, or a related field
> Hands-on experience (academic or personal projects) with Python and at least one LLM framework (LangChain, LlamaIndex, Haystack, or similar)
> Working knowledge of LLM tool calling / function calling (OpenAI-style tool schemas or equivalent)
> Ability to design clear tool definitions with well-scoped descriptions and parameter schemas
> Basic understanding of vector databases (Chroma, Pinecone, Weaviate, or Qdrant) and embedding models
> Familiarity with REST APIs and working with JSON/structured data
> Strong attention to detail when handling legal or regulatory source material
> Good written communication in English
> Preferred qualifications
> Prior exposure to Indian statutory frameworks (GST, income tax, company law, or professional standards)
> Experience building multi-tool agents or agentic workflows where the model chains tool calls across steps
> Experience with OCR tools or PDF parsing libraries
> Understanding of prompt engineering and response evaluation techniques
> Familiarity with admin or CMS panel development (any stack)
> Benefits
> Meaningful ownership of a core product feature from day one
> Hands-on exposure to LLM application development in a production environment
> Direct mentorship from the founding team
> Stipend commensurate with contribution
> Letter of recommendation and internship certificate upon successful completion
> Flexible remote or hybrid working arrangement


---

## Full stack Developer - Graduate Program (754567WD) — PwC ETIC

- **Location:** Cairo - ETIC
- **Posting:** https://pwc.wd3.myworkdayjobs.com/en-US/Global_Experienced_Careers/job/ETIC--Full-stack-Developer----Graduate-Program_754567WD
- **Source:** Ali Turky list (Workday)
- **CV:** `Ahmed_Dorra_CV_PwC_ETIC_Graduate.pdf` (variant `cv/variants/pwc_fullstack_graduate.py`)
- **Tracker id:** `2026-11-28-pwc-etic-fullstack-developer-graduate` (priority #11)

### Verdict
**Backup (long shot).** Graduate programme, open (canApply true), but the core is JavaScript/React, which you can't claim. Your Python REST APIs, Docker, CI, TDD and ORM work cover the rest. Apply only after the stronger ones.

### Company check
PwC Middle East's Cairo tech centre; you already applied to its AI and Data Science Associate roles (29 Oct).

### How to apply
Open the Workday link → **Apply** (same Workday account as before) → upload `Ahmed_Dorra_CV_PwC_ETIC_Graduate.pdf`.

### Note to paste
```
Hello, I'm applying for the Full stack Developer - Graduate Program position at PwC ETIC. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, available to start immediately, and can commute to ETIC. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Expect a JS/React question: say you work in Python back ends and are ready to learn React in the programme.

### Original post

> Job Description & Summary
> Full Stack Developer Graduate scope overview:
> Participate in the designing and building of complex solutions for a web application (end-to-end)
> Oriented toward server-side web application logic in JavaScript and/or variants of it, microservices architecture, design, build and implementation
> Implementation of container-based REST APIs using container frameworks like OpenShift, or Docker
> Facilitating the team’s daily activities following different SCRUM events.
> Support and mentor the team in understanding agile methodology principals across all team members.
> Incorporate data protection and cybersecurity measures
> Ensure that database and front-end requests are at their optimal performance
> Automated testing, Test driven development (TDD)
> Create and maintain technical documentation
> Role Requirements:
> Knowledge of JavaScript, libraries, frameworks, and tech stacks
> Good knowledge with front-end development using React technology and (HTML, CSS,, Redux, etc)
> Good knowledge in DevOps continuous integration and continuous delivery tooling eg Gradle, GIT, GitHUB, GITLab, etc. and ability to perform developer-owned Devops tasks
> Strong drive for Clean Code, Automation tools, Design improvements and Code quality (via Unit testing)
> Ability to use Asynchronous Programming to improve productivity
> Solid background in managing databases and Object-Relational Mapping (ORM) tool
> Role Requirements:
> Knowledge of JavaScript, libraries, frameworks, and tech stacks
> Good knowledge with front-end development using React technology and (HTML, CSS,, Redux, etc)
> Good knowledge in DevOps continuous integration and continuous delivery tooling eg Gradle, GIT, GitHUB, GITLab, etc. and ability to perform developer-owned Devops tasks
> Strong drive for Clean Code, Automation tools, Design improvements and Code quality (via Unit testing)
> Ability to use Asynchronous Programming to improve productivity
> Solid background in managing databases and Object-Relational Mapping (ORM) tool
> Experience in:
> Nodejs Frameworks, JavaScript, Typescript
> Experience in Python is a plus or any other back-end technology
> Google Cloud Platform is a plus
> Caching technologies (e.g Redis)
> Custom integration with IdAM Auth0 SAML, etc.
> DynamoDB, OpenShift, Docker
> RDBMS databases knowledge, specifically on Cloud SQL using MySql
> Gitlab, Github or any similar tool, Branching and Merging Strategies
> Azure DevOps knowledge, Jenkins, APIgee, JSON, JSF, XHTML, Tools like Kibana, new relic or similar logging and monitoring tools
> BDD, TDD. Unit Testing Frameworks (JUnit),Performance testing, API tests, Contract and Component level Testing
> Linux, Frontend/UI Dev experience, Automation Testing, Devops tools
> Education (if blank, degree and/or field of study not specified)
> Degrees/Field of Study required:
> Degrees/Field of Study preferred:
> Certifications (if blank, certifications not specified)
> Required Skills
> Optional Skills
> Desired Languages (If blank, desired langu


---

## AI Engineer Intern (3 months) — KoreaShopABC Egypt

- **Location:** Zahraa El Maadi, Cairo (on-site)
- **Posting:** https://wuzzuf.net/jobs/p/bra5lzjoeskb-ai-engineer-intern-koreashopabc-cairo-egypt
- **Source:** Ali Turky list (Wuzzuf)
- **CV:** `Ahmed_Dorra_CV_KoreaShopABC.pdf` (variant `cv/variants/koreashopabc.py`)
- **Tracker id:** `2026-11-28-koreashopabc-ai-engineer-intern` (priority #12)

### Verdict
**Backup (internship, low pay/unpaid).** Entry-level AI agents and automation; aimed at students, Laravel listed. Only worth it if nothing better lands.

### Company check
koreashopabc.com since 2022; also posts a full-stack AI role on Wuzzuf. No fees.

### How to apply
Open the Wuzzuf link → **Apply** → upload `Ahmed_Dorra_CV_KoreaShopABC.pdf`.

### Note to paste
```
Hello, I'm applying for the AI Engineer Intern position at KoreaShopABC Egypt. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, available to start immediately, and can commute to Maadi. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Show agents + automation demos (shopping assistant video).

### Original post

> Job Description:
> Hiring ASAP: AI Engineer Interns | KoreaShopABC Egypt
> Location: Zahraa El Maadi, Cairo (On-Site)
> Duration: 3 Months
> Compensation: Paid / Educational Internship
> 
> Job Description
> 
> Join our AI JOBS platform , featuring real business AI projects. Learn, build and deliver practical AI solutions with guidance and supervision.
> 
> Responsibilities:
> 
> Build AI tools, agents and automation.
> 
> Automate social media, marketing and sales.
> 
> Develop AI-powered websites and applications.
> 
> Test and deliver working AI solutions.
> 
> 3-Month Learning Program
> Month 1: AI training, tools and guided projects.
> 
> Month 2: Develop real AI applications and automation.
> 
> Month 3: Complete independent projects and build your portfolio.
> 
> Benefits
> 
> Hands-on experience with real AI business projects
> 
> Practical AI training and mentorship.
> 
> Build a professional portfolio of completed projects.
> 
> Internship completion certificate.
> 
> Flexible schedule for university students.
> 
> Exposure to international Korean companies.
> 
> Opportunity for paid employment based on performance.
> 
> Requirements
> Job Requirements
> Ideal Candidates:
> Computer Science / AI students or fresh graduates.
> 
> Basic Python, Laravel, APIs or AI knowledge.
> 
> Fast learners with strong problem-solving skills.
> 
> Self-motivated, responsible and passionate about AI.


---

## Junior Arabic NLP Engineer (contributor) — Apex AI Arabia

- **Location:** Remote
- **Posting:** https://apexaiarabia.com/opportunities/HR-OPN-2026-0321
- **Source:** Ali Turky list (company site)
- **CV:** `Ahmed_Dorra_CV_Apex_AI_Arabia.pdf` (variant `cv/variants/apex_ai_arabia.py`)
- **Tracker id:** `2026-11-28-apex-ai-arabia-junior-arabic-nlp-engineer` (priority #13)

### Verdict
**Backup, with caution.** Arabic text processing and evaluations fit you, but it's a contributor role with **no fixed salary**, and the domain is only 5 months old. Don't pay anything or send ID; get written terms first.

### Company check
Jeddah/Riyadh 'enterprise AI' site with phone/WhatsApp; apexaiarabia.com registered July 2026. Thin footprint.

### How to apply
Open the link → **Apply for this position** → upload `Ahmed_Dorra_CV_Apex_AI_Arabia.pdf`.

### Note to paste
```
Hello, I'm applying for the Junior Arabic NLP Engineer position at Apex AI Arabia. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, Egypt, available to start immediately, and happy to work remotely in any time zone. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Interview prep
- Ask for paid terms in writing before any work.

### Original post

> About the role
> Assist with Arabic text processing and language evaluations. Work under an assigned reviewer, document outputs, request feedback and follow project-specific access controls. This is a remote, flexible junior contributor opportunity suitable for candidates developing professional experience. No fixed salary or guaranteed income is implied; any compensation, scope, intellectual property, confidentiality and engagement terms require a separate written agreement before work begins.
> Required qualifications
> Arabic language fluency, Python and NLP fundamentals. Entry-level applicants, recent graduates and candidates with relevant portfolio projects are welcome. Ability to learn, communicate asynchronously, accept feedback and deliver documented work. Access to customer or sensitive data only with explicit authorization.


---

## AI Engineering Intern — MacroCoderz

- **Location:** Remote
- **Posting:** https://macrocoderz.com/careers/ai-engineering-intern
- **Source:** Ali Turky list (company careers page)
- **CV:** `Ahmed_Dorra_CV_MacroCoderz.pdf` (variant `cv/variants/macrocoderz.py`)
- **Tracker id:** `2026-11-28-macrocoderz-ai-engineering-intern` (priority #14)

### Verdict
**Backup.** Remote internship; the site returned an error today, so the post wasn't read. Try again later.

### Company check
Pakistan-based; macrocoderz.com since Aug 2024; posts many near-identical remote roles across Pakistani cities on job boards. Be cautious; no fees.

### How to apply
When the page loads, apply there with `Ahmed_Dorra_CV_MacroCoderz.pdf`.

### Note to paste
```
Hello, I'm applying for the AI Engineering Intern position at MacroCoderz. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, Egypt, available to start immediately, and happy to work remotely in any time zone. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

### Original post

> (Not readable automatically: summary from Ali Turky's list.)


---

## Repost check (28 Nov)
- **TP:** new post 4488896197 asks 1–3 years; the old one (3–4 years) is closed. Added.
- **Arabic.AI:** the Built In copy (24 Nov) is the same AI Engineer job; you applied on 16 Oct and 8 Nov. Separate new role: End-to-End ML Engineer for Arabic/English dashboards (Riyadh, on-site; Qlik/Power BI/Dataiku core), not added.
- **PwC ETIC:** Data Science Associate (657378WD) and AI Engineer Associate (752966WD) are the same requisitions you applied to; both still open.
- **SDG, Orascom, Numrah, Smarterminds, Vertex, Finalyze:** same postings, no reposts.
- **Lamdax:** same AI Engineer job; their new internship post is for current undergraduates only.
- **Capgemini YPP:** no AI repost; the open YPP roles need German/Turkish/French/Spanish.
- **Provectus:** a Serbia copy of the junior role (18 Nov) has gone from LinkedIn; their Lever board has no junior roles.
