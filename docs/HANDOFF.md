# Handoff: continuing Ahmed Dorra's AI job search

This is everything a new AI assistant (or a human helper) needs to pick up where Claude left off on 8 November 2026.
Read it fully before helping. Then read `CLAUDE.md` in the `AhmedMostafa167/job-search` repo, which holds the same rules in more detail.

---

## Latest status (25 Nov 2026)

- **CVs:** all 97 rebuilt with the HR-first summary (`cv/hr_summary.py`), email ahmed.dorra.ml@gmail.com, labelled LinkedIn/GitHub/Portfolio links and the expanded MLOps MENA role; all 2 pages. General CVs in Drive → Resume → "CVs 2026-11-25"; public CV link https://drive.google.com/file/d/1P_Tqwkuk-Yt_s2tsKK46PVKecZLfShMt/view?usp=sharing. Portfolio CV and contact email updated.
- **Tracker:** ~306 rows. Newest Ready rows: `applications/2026-11-25-market-search.md` (18, priorities #10–27, Egypt first) and `applications/2026-11-25-sweep-picks.md` (16, #28–43). Every row's CV button points at the rebuilt CVs.
- **Areeb AI Engineer (Cairo):** Ahmed was filling in its application form on 25 Nov; answers drafted in chat. Mark it Applied when he says "done".
- **Daily sweep:** fixed on 25 Nov (remembers every reported post, junior-only generic titles, wrong stacks dropped, seniors ranked down). The 26 Nov email will be long once while it records the backlog; after that only new posts.
- **LinkedIn:** Ahmed set up stickerdaniel/linkedin-mcp-server in his Claude desktop app (guide: `docs/LINKEDIN-MCP.md`, Drive doc "03 LinkedIn MCP"). Jobs only, ~2 sessions/day, never message or connect; it never submits, he does. Paste its results into the job-search chat to add rows.
- **Still missing from Ahmed:** years of experience, expected salary, notice period (Easy Apply forms ask for them); military-service dates and internship partner names to confirm.
- **Market search tools:** freehire and LinkedIn guest CLIs now live in `ai-job-search-dev/community-portals` (`portals/global/*/cli/src/cli.ts`, run with `bun run`), not in ai-job-search.

## 1. Who Ahmed is and what he needs

- **Name on CVs:** Ahmed Dorra. GitHub, LinkedIn and Kaggle handles still say Ahmed Mostafa.
- **Goal:** his first industry job as an AI / ML / LLM engineer (also data science, MLOps, Python backend, AI trainer and AI-instructor roles). **He needs a job, so when in doubt, apply.**
- **How he works:** he sends job posts (pasted text, a link, or a screenshot), often from his phone. **Keep replies short and scannable.** Do the work with as little back-and-forth as possible.
- **Contact:** Giza, Egypt · +20 100 614 8440 · ahmed.dorra.ml@gmail.com · linkedin.com/in/ahmed-mostafa-dorra · github.com/AhmedMostafa167 · ahmedmostafa167.github.io
- **Citizenship:** Egyptian. Needs visa sponsorship outside Egypt; no US work authorisation to live in the US (US-remote contracts are fine). Open to relocation, remote, any time zone, any contract type.
- **Languages:** Arabic (native), English (professional). Mention native Arabic for Arabic, MENA or Gulf companies.

### Career facts (verified)
- **BSc Computer Science**, Culture and Science City, 6th of October, Giza (10/2020 – 06/2024). Diploma in Quantum Computing, QWorld (10/2023 – 07/2024).
- **Quantum Research Intern**, QUAE (QWorld UAE chapter), remote, 12/2023 – 03/2024: quantum VAE for EEG denoising + LDA classification; published at Neurogenomics 2024.
- **Military service** (mandatory), 01/2025 – 01/2026 *(dates still to confirm with him)*.
- **Teaching Assistant, Computer Science**, Culture and Science City, since **03/2026** (started 1 March 2026):
  - Advanced Operating Systems to **700+ students** (processes/threads, scheduling, synchronisation/deadlocks, memory/virtual memory, file systems).
  - Starter **MLOps course to about 500 students**, modelled on ML Zoomcamp (cleaning, a linear model on a churn dataset, project layout, MLflow, FastAPI, Docker).
  - **50 Compiler Theory labs for 600+ students**; Distributed Computing quizzes; assisted two 2025/26 graduation projects (social-media trend & emotion analysis; diabetes detection with ML).
- **AI Research & Mentorship Engineer, MLOps MENA Community**, since **08/2026**: mentors learners on MLOps/AI projects, researches and writes technical material. No counts given; don't invent any.
- **Publications:** (1) "Fine-tuning Stable Diffusion for Generating 2D Floor Plans Using Prompt Templates", Machine Graphics & Vision 34(3), 09/2025 (VISIONEER). (2) "Quantum Denoising in the Realm of Brain-Computer Interfaces", Neurogenomics 2024. ORCID 0009-0001-4161-6026.
- **Not yet given (leave `[FILL IN]`):** notice period, expected salary, years of experience.

---

## 2. Truthfulness rules (non-negotiable)

Only claim what is in his repositories or what he has confirmed.

**Never claim:** YOLO / object detection · n8n · TypeScript / JavaScript · TensorFlow (he uses PyTorch and Hugging Face) · Azure / Copilot Studio · speech (STT/TTS) · OCR · vector-based memory (the Shopping Assistant's memory is typed facts in PostgreSQL plus a LangGraph Postgres checkpointer).

**Not his work, keep off CVs:** Dialogue Summarization (QLoRA), the old Banking Intent Classifier, and Pharma-Connect (his students' project; he mentored it).

**Projects and the exact numbers you may use:**
1. **Shopping Assistant** (github.com/AhmedMostafa167/Shopping-Assistant, has a demo video). LangGraph agent + FastAPI + PostgreSQL/pgvector, Docker, Langfuse, Prometheus/Grafana.
   - 12,730 products; ingestion with pandas loaders for 5 formats + row-level Pydantic validation.
   - Retrieval on 127 labelled queries with 95% CIs: top-10 recall **72% hybrid vs 56% keyword vs 41% vector**.
   - Reranking moved the right product to first place **23% → 43%** (40-query subset).
   - HNSW index: median vector-search latency **35 ms → 3.1 ms**.
   - Agent evaluation 12 tasks × 3 runs: prompt v2 passed **12 of 12 vs 7**, with **29% fewer paid rerank calls**; v3 moved price/rating limits inside search: matching results **70% → 100%** (57/81 → 48/48), **15% fewer paid searches**.
   - Guardrails refused **0 of 21** legitimate facts; `prices_grounded` passed **25 of 25**. **104 tests**. `MAX_FACTS_PER_USER = 50`.
   - Bug story (use honestly): price-limited requests went to a query-less filter tool, so "phone case under $15" returned non-cases; first suspected the storefront cards. Found and fixed the same day (14 Oct 2026); don't say it took more than a day unless he confirms.
2. **Arabic Banking Intent Classifier** (github.com/AhmedMostafa167/arabic_banking_intent, Nov 2026). AraBERT on 77 intents (ArBanking77): validation macro-F1 **0.919 vs 0.887** TF-IDF; **0.843 / 0.779 / 0.599** on Saudi / Moroccan / Tunisian dialects unseen in training (baseline 0.719 / 0.612 / 0.499). Found the official split leaks paraphrases (~3 points inflation) and built a grouped split + paired-bootstrap promotion gate in the MLflow registry. Served as ONNX fp16 in FastAPI (image **2.26 GB → 0.95 GB**, median latency 670 → 530 ms on CPU), Locust load test, Prometheus/Grafana, drift alert; model card on Hugging Face. Don't mention the "laptop CPU" remark.
3. **Research Assistant** (github.com/AhmedMostafa167/research-assistant; demo huggingface.co/spaces/Ahmed167/research_assistant). Self-correcting LangGraph RAG over arXiv and the web. **He designed the agent; Claude built most of the code. Describe the design; don't overstate the implementation.**
4. **VISIONEER (2024):** he and a colleague fine-tuned Stable Diffusion v1.5 with LoRA on ~12k floor plans; a teammate trained the schematic model. Published 2025. (Dropped from CV projects, kept as a publication.)

**Still to confirm with him:** military service dates; the internship partners' exact names (IBM and an Abu Dhabi entity); whether VISIONEER was his graduation project.

---

## 3. Rules for choosing jobs

- **Never skip or de-prioritise** for time zone, remote vs on-site, contract vs full-time, or pay. He was explicit: "I HAVE TO GET A JOB, no matter what type, what time zones or anything."
- **Skip only for real blockers:** nationality- or residents-only, a language he doesn't speak, clearly senior (5+ years), core skills far outside his field, or scam signs (any fee, ID documents before an offer, no footprint + brand-new domain).
- **Stretch roles** (2–4 years, senior titles, "AI Engineer / Senior AI Engineer") are **backups, not skips**.
- **Never drop a post for its age;** check whether it's still open (Workday `/wday/cxs/<tenant>/<site>/job/<path>` returns `canApply`; Greenhouse `boards-api.greenhouse.io/v1/boards/<board>/jobs/<id>`; Workable/Lever pages show the post or an error).
- **Check duplicates** in the tracker first: recruiters repost jobs. Point out a duplicate instead of re-applying (he has already applied to Arabic.AI twice: 16 Oct and its repost on 8 Nov).
- **Company check** for unknown firms: website, domain age (`https://rdap.org/domain/<domain>`), UK Companies House for UK firms, news.

---

## 4. The routine for each job post

1. **Read the full post.** LinkedIn, Wuzzuf, Bayt and GulfTalent block bots: ask him to paste the text. Careers portals often have open APIs (Recruitee `<company>.recruitee.com/api/offers/`, Greenhouse, Lever, Workable).
2. **Check the company** (see above).
3. **Verdict in 2–3 lines:** apply / apply as backup / skip, with the reason.
4. **Tailor the CV** (see section 5). Keep it at 2 pages. A cover letter, if needed, stays at 1 page.
5. **Write the pack** `applications/<YYYY-MM-DD>-<company>.md`: posting, how to apply (address, exact subject line, attachment), verdict, company check, the email ready to paste, interview prep, and the original post quoted. One job per file: if a post lists several roles, give each its own tracker row.
6. **Track it** (section 6) as `Ready to send` with a priority.
7. **Reply in a few lines:** verdict, what was tailored, exactly how to send it, tracker status.
8. When he says **"done"**, mark the latest Ready row `Applied`, applied today, follow-up in 7 days. Status updates he reports ("rejected by X", "X replied") go to the matching row.

---

## 5. CVs: where they are and how to build them

All in the private repo **github.com/AhmedMostafa167/job-search**.

- **Ready-made general CVs** in `cv/ready/` (use when there's no time to tailor):
  | Post is about | Send |
  |---|---|
  | LLMs, RAG, agents, GenAI | `Ahmed_Dorra_CV_General_LLM_Agents.pdf` |
  | ML engineer, MLOps, serving | `Ahmed_Dorra_CV_General_ML_MLOps.pdf` |
  | Data scientist | `Ahmed_Dorra_CV_General_Data_Scientist.pdf` |
  | Python / backend | `Ahmed_Dorra_CV_General_Python_Backend.pdf` |
  | Arabic NLP, MENA/Gulf | `Ahmed_Dorra_CV_General_Arabic_NLP.pdf` |
  | Graduate programme, junior, internship | `Ahmed_Dorra_CV_General_Junior_Graduate.pdf` |
  | Trainer, instructor, mentor | `Ahmed_Dorra_CV_General_AI_Instructor.pdf` |
  | Anything else | `Ahmed_Dorra_CV.pdf` |
- **Every tailored CV and cover letter already sent or prepared** is in `cv/sent/` (104 PDFs; names match the tracker's `cvName` / `letterName`).
- **Source of truth:** `cv/cv_content.py` (base content) and `cv/arabic_intent_project.py` (added automatically at build). Variants live in `cv/variants/<slug>.py`; each imports a base and overrides `TITLE`, `SUMMARY`, `SKILLS`, project order, and `FILE_STEM = "Ahmed_Dorra_CV_<Company>"`. Cover letters: add a `COVER_LETTER` dict (date, to, greeting, paragraphs, closing) to the variant.
- **Build** (needs Python 3, `pip install -r cv/requirements.txt`, and Chromium):
  - CV: `cd cv && CV_MODULE=variants.<slug> python3 build_cv.py ../out`
  - Letter: `cd cv && CV_MODULE=variants.<slug> python3 build_cover_letter.py ../out`
  - Check: `pdfinfo out/<file>.pdf` → 2 pages for a CV, 1 for a letter.
- **No coding tools?** Copy the closest general CV's text into Google Docs, change the title line and the 3–4 line summary to echo the post's keywords, reorder skills, export as PDF named `Ahmed_Dorra_CV_<Company>.pdf`.
- **When the general CV changes:** rebuild, replace `assets/Ahmed_Dorra_CV.pdf` in the `AhmedMostafa167.github.io` repo (branch `master`), and upload it as a **new version** of the Drive file https://drive.google.com/file/d/1sdeY9TZgge88EjOI0Nu1NiGbryG8Y6WB/view (Manage versions keeps the link). Never share the old August Drive CV (id 1yMGMYOHgShmWUlpCPnf6gnEApKDEfSco): it has an email typo.

---

## 6. The tracker

- **Where:** the claude.ai artifact "AI Engineer Applications" (https://claude.ai/artifact/3U2A9XwLESewJ8e7Wt9Vus) may stop being editable once the subscription ends. Exports are in the Drive folder Resume → "AI Agent Handoff (job search)" (**"Tracker – Ready to send"** and **"Tracker – Sent and closed"** sheets), and the full export with notes is at `tracker/tracker_export_2026-11-08.csv`. Continue tracking in those Google Sheets.
- **Columns:** status, priority (lower = apply first, only for Ready rows), company, role, postingUrl, appliedOn, followUpOn, CV (file name in `cv/sent/` without the `Ahmed_Dorra_` prefix). The repo CSV also has id, location, contact, source, pack file and notes.
- **Status values:** Ready to send · Applied · Screening · Interview · Offer · Rejected · No response · Withdrawn.
- **State on 8 Nov 2026:** 237 rows: **152 Ready to send**, 60 Applied, 4 Screening, 3 Rejected, 18 Withdrawn.
- **Follow-ups due:** about 11 applications on **11 Nov** (CIB, MigrationIT ×3, Capgemini ×2, CDS, Akvelon, LamdaX, Blackstone eIT, AI Overlords, Pass Technology, Romoze, EpsilonAI, GenAI Protos, Scale Army) and about 20 on **15 Nov** (Vodafone Romania, European Dynamics, Resonance, Coca-Cola, EY Malaysia, dopay, Fourtitude, helloprint, Bending Spoons, Foodics, Echelon, Fikrah, ActAI ×2, Orange, CIB pool, MasterBorn, Data Science ME, Arabic.AI repost). Older October applications with no reply can move to `No response` after 3 weeks.
- **Each Ready row's pack** (`packName`) is in the repo's `applications/` folder: open it for the email text and how to apply.

---

## 7. Automatic daily job sweep (runs without any AI)

- `tools/sweep.py` + `.github/workflows/daily-sweep.yml` run every day at 07:00 Cairo time on GitHub Actions. They search freehire, LinkedIn public pages, Remotive, Arbeitnow, Jobicy, RemoteOK and Himalayas, drop jobs already seen, and write `shortlists/auto/<date>.md`, grouped Egypt → Gulf & Arab world → Remote → everywhere else, with flags (senior / US / intern). GitHub opens an issue "New jobs <date>" that emails him.
- **Run now:** repo → Actions → "Daily job sweep" → Run workflow. Tune queries in `tools/sweep_config.json`.
- **Not covered (check by hand twice a week):** Wuzzuf, Bayt, GulfTalent, and the company portals in `referrals/egypt-targets.md` (CIB/Taleo, PwC ETIC and Valeo/Workday, Orange/iCIMS, Vodafone, Raya/Oracle, Henkel/Cornerstone, Capgemini).
- A shareable copy (`job-sweeper.zip`) was made for his friends Omar and Hisham (`friends/hisham/job-sweeper/` in the repo).

---

## 8. Other repos and accounts

- **Portfolio:** github.com/AhmedMostafa167/AhmedMostafa167.github.io (branch `master`, no build step) → ahmedmostafa167.github.io. Its CV buttons open `assets/Ahmed_Dorra_CV.pdf`.
- **Profile README:** github.com/AhmedMostafa167/AhmedMostafa167 (projects table, skill badges).
- **Project repos:** Shopping-Assistant, arabic_banking_intent, research-assistant. The old `Projects` monorepo is archived (pointer README).
- **Plans for future projects:** `plans/` in job-search (Project 2: Egyptian Arabic support-ticket model). Add to the CV only with measured results once finished.
- **Answer bank** for application questions: `docs/ANSWER-BANK.md` in the repo and the "01 Answer bank" doc in the Drive handoff folder.

---

## 9. What to do first (Ahmed)

1. **Merge the latest work into `main`:** on GitHub open `AhmedMostafa167/job-search` → "Compare & pull request" for branch `ccr-55ff00d3-tfnruu` → Create pull request → Merge. This brings the newest sweep fixes (Gulf filter, India filter, tiers), the `cv/sent/` PDFs, the tracker export and these docs into `main`, which the daily sweep uses.
2. Keep sending the **152 Ready-to-send** applications in priority order (lowest number first).
3. Do the follow-ups on 11 and 15 Nov (short polite email: role, date applied, one line of fit, ask about next steps).
4. Give the next assistant your notice period, expected salary, and the 3 facts in "Still to confirm".

---

## 10. Prompt to paste into a new AI assistant

> You are helping Ahmed Dorra, an Egyptian Computer Science graduate (2024), get his first AI/ML engineering job. Read the attached "00 START HERE" handoff fully and follow it exactly, especially the truthfulness rules (never claim YOLO, n8n, TypeScript/JavaScript, TensorFlow, Azure/Copilot Studio, speech, OCR or vector memory; use only the listed project numbers) and the job rules (never skip a job for time zone, remote/on-site, contract type or pay; skip only nationality/residency-only, unspoken language, clearly 5+ years, far outside his field, or scams). When I send a job post: (1) give a 2–3 line verdict, (2) pick the best general CV or tell me exactly what to change in the title, summary and skills, (3) write the email or cover letter ready to paste with the exact subject line, (4) give me a tracker row (company, role, link, status, dates, CV name, notes), (5) list likely interview questions. Keep replies short; I read on my phone. Leave [FILL IN] for salary, notice period and years of experience.


## Rule added 28 Nov 2026: work rights are not a reason to skip
Apply even when a post asks for local right to work, residence or says no visa sponsorship (UK, EU, US, Canada...). The aim includes getting interviews to practise and learn the gaps. Still skip: nationality-only roles, security clearances that need citizenship, languages he doesn't speak, current-students-only or fixed graduation-year programmes, clear 5+ year senior roles.
