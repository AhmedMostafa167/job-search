# AI Engineer (agent orchestration) — The HR Game (for a banking client)

- **Location:** Cairo
- **Posting:** https://eg.linkedin.com/jobs/view/4494141920
- **Source:** Ali Turky list (LinkedIn)
- **CV:** `Ahmed_Dorra_CV_The_HR_Game.pdf` (variant `cv/variants/hr_game.py`)
- **Tracker id:** `2026-11-28-the-hr-game-ai-engineer` (priority #2)

## Verdict
**Apply.** Agent orchestration, tool calling, agent evaluation, retries and failure recovery: all in your LangGraph agent with its code-graded evaluation. LinkedIn tags it Mid-Senior but no years are stated. Banking is a nice-to-have.

## Company check
Egyptian HR/recruitment firm (thehrgame.com, since 2023) hiring for a banking client; 200+ applicants on LinkedIn, so apply soon.

## How to apply
Open the LinkedIn link → **Apply** (Easy Apply or their form) → upload `Ahmed_Dorra_CV_The_HR_Game.pdf`. If there's a note field, paste the note.

## Note to paste
```
Hello, I'm applying for the AI Engineer position at The HR Game. Your post centres on agent orchestration, tool calling and evaluating agent reliability; that's the core of my recent work. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, available to start immediately, and can commute to anywhere in Cairo. Code: github.com/AhmedMostafa167 · Portfolio: ahmedmostafa167.github.io

Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com
```

## Interview prep
- Human approval checkpoints: how you'd add an interrupt/approve step in LangGraph before a risky tool call.
- Retries and failure recovery: bounded retries, the Research Assistant's self-correcting loop, guardrails.
- Agent evaluation: 12 tasks × 3 runs, code-graded; v2 12/12 vs 7 with 29% fewer paid calls.
- Access control / data privacy: per-user memory scoping, MAX_FACTS_PER_USER, refusing ungrounded prices (25/25).

## Original post

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
