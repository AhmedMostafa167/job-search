# Capgemini Egypt: Software Engineer (GenAI), Cairo

## The posting

- **Company:** Capgemini Egypt, Cairo.
- **Role:** Software Engineer, "Experienced Professionals" level.
- **Post:** https://careers.capgemini.com/job/Cairo-Software-Engineer/1453382933/ (new on 2 Nov 2026; Capgemini's job API, id 1453382933).
- **Experience:** "preferably at least 2 years" in generative AI and software development.
- **What you'd do:** build secure, scalable services; build AI-driven solutions; tune performance and security; work with project managers and product owners.
- **What they want:**
  - LLMs connected to external knowledge sources;
  - RAG architectures;
  - embeddings, semantic search and vector databases;
  - Python (JavaScript/TypeScript is a plus);
  - LangChain and LangGraph;
  - REST APIs and back-end services;
  - Git (GitFlow).
- **Nice to have:** AI/ML training and deployment services; speech-to-text and text-to-speech.

## How to apply

1. Open the link and tap **Apply**. Use the same Capgemini account as your other two Capgemini applications.
2. Upload `Ahmed_Dorra_CV_Capgemini_GenAI.pdf`.

## Verdict: apply (a strong match)

The core asks line up with your projects:
- RAG with embeddings and pgvector, plus hybrid search;
- LangGraph and LangChain;
- FastAPI REST services;
- Git and CI.

"Preferably 2 years" is soft.

**Gaps:**
- JavaScript/TypeScript;
- GitFlow by name (you do use Git branches and CI);
- speech (STT/TTS);
- cloud AI services.

None of these are claimed.

## Company check

Capgemini is a global company (340,000 people) and this post is on its official careers site. No red flags.

## Short note (for a cover-letter box or a recruiter message)

```
I build the kind of GenAI services this role describes: RAG over enterprise-style data (chunking, embeddings, hybrid search on pgvector and PostgreSQL full-text, reranking) and LangGraph workflows behind FastAPI REST APIs, with Pydantic-validated outputs, guardrails, 104 tests and CI. I measure retrieval and speed: 72% top-10 recall vs 41% for vector search alone, and an HNSW index that cut median search latency from 35 ms to 3.1 ms. — Ahmed Dorra
```

## Interview prep

- **Walk through your RAG design:**
  - chunking choices;
  - why hybrid search plus Reciprocal Rank Fusion;
  - when reranking pays off;
  - how you measured each stage (127 labelled queries, 95% confidence intervals).
- **"Securing an LLM service":**
  - input guardrails;
  - Pydantic validation of model output;
  - not trusting tool arguments;
  - keeping secrets out of prompts;
  - tests in CI.
- **"Performance":** the HNSW index (35 → 3.1 ms median) and reranking only the top candidates.
- **GitFlow:** know the branch model (feature, develop, release, hotfix) before the interview.
- **Notice period / expected salary:** [FILL IN]

## Original post (quoted)

> We are looking for a professional with preferably at least 2 years of experience and a strong background in Generative AI and software development. The main responsibilities include: Designing, developing, and maintaining secure, scalable, and reliable software services. Implementing and evolving AI-driven solutions in line with application architecture guidelines. Improving code quality, performance, and security through tuning and assessments. Collaborating with cross-functional teams, Project Managers, and Product Owners. Supporting impact analyses, effort estimations, and project delivery activities. Contributing to technical discussions and the definition of implementation strategies.
> Key technical requirements: Strong knowledge of LLMs and their integration with external knowledge sources. Hands-on experience with RAG (Retrieval-Augmented Generation) architectures. Experience with embeddings, semantic search, and vector databases. Good knowledge of Python (JavaScript/TypeScript is a plus). Experience with LangChain and LangGraph. Integration with RESTful APIs and backend services. Git version control (GitFlow model). Strong problem-solving and teamwork skills.
> Nice-to-have: Experience with AI/ML services for training and deployment of advanced models. Experience with Speech-to-Text and Text-to-Speech APIs, including streaming capabilities. Technical degree in Computer Engineering, Computer Science, or a related field. Good spoken and written English.
