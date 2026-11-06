# Job search — how Claude works in this repo

Ahmed is applying for AI engineer roles. His CV name is **Ahmed Dorra**, and the portfolio (ahmedmostafa167.github.io) now shows Ahmed Dorra too; his GitHub, LinkedIn and Kaggle handles still say Ahmed Mostafa. The portfolio source now lives in its own repo, `AhmedMostafa167/AhmedMostafa167.github.io` (branch `master`, no build step; since 6 Nov 2026; the old Projects monorepo only holds a pointer README). Its CV buttons open `assets/Ahmed_Dorra_CV.pdf` directly, so the site always serves the current CV. A Google Drive copy also exists for links he has already shared (https://drive.google.com/file/d/1sdeY9TZgge88EjOI0Nu1NiGbryG8Y6WB/view, shared with anyone who has the link). The Drive tools here can't replace a file's content. Whenever the general CV changes, rebuild it, replace that asset, push the github.io repo, and ask Ahmed to upload it as a new version of the Drive file (Manage versions keeps the link); the old August Drive CV (id 1yMGMYOHgShmWUlpCPnf6gnEApKDEfSco) has an email typo and should not be shared. He sends job postings (pasted text, a link, or a company website), often from his phone during commutes. For each one, run the routine below with as little back-and-forth as possible, and keep replies short: he reads them on a phone.

## Tracker

- Dashboard: https://claude.ai/artifact/3U2A9XwLESewJ8e7Wt9Vus (private artifact "AI Engineer Applications").
- Page source: `tracker/applications.html`. To change the page, edit it and publish with the Artifact tool using the tracker `url` (it was published from another session, so read it first). The capabilities it declares are kept on redeploy when `capabilities` is omitted.
- Data lives in the artifact's database (`ArtifactData` tool). Collection `applications`; document id `YYYY-MM-DD-<company-slug>`.
- Fields: `company, role, location, source, postingUrl, contact, status, postedOn, appliedOn, followUpOn, cvAsset, cvName, letterAsset, letterName, packAsset, packName, notes, createdAt, updatedAt`. Dates are `YYYY-MM-DD`; unknown values are `null`.
- `priority` (optional number, 1 = apply first) orders the `Ready to send` rows on the page; the row shows `#N`. When adding a Ready row, give it a priority by fit, junior level, Egypt/remote (no visa needed) and deadlines, and shift the others down if needed.
- `status` is one of: `Ready to send`, `Applied`, `Screening`, `Interview`, `Offer`, `Rejected`, `No response`, `Withdrawn`.
- Files: upload the tailored CV PDF, the cover letter PDF when there is one, and the application `.md` to the artifact's asset store (`Artifact` publish with the tracker `url` and `asset: true`; a `.md` file goes in a call of its own) and store the returned ids in `cvAsset` / `letterAsset` / `packAsset`. The page shows each as a button on the row.
- Before adding a row, `list` the collection: recruiters repost the same job, and a duplicate should be pointed out, not re-applied.
- **"done"** from Ahmed means he sent the latest `Ready to send` application: update that row to `status: Applied`, `appliedOn: today`, `followUpOn: today + 7` (pin the write with `if_version`).
- Status updates he reports ("Raya replied", "rejected by X") go to the matching row the same way.

## Routine for each posting

1. **Read it fully.** For a link, fetch the page. For a company website, find its careers portal: Recruitee (`<company>.recruitee.com/api/offers/`), Workable, Greenhouse or Lever all publish open jobs in machine-readable form. LinkedIn and Wuzzuf block automated reads, so ask him to paste the text.
2. **Check the company.** Look at its website, the domain's age (`https://rdap.org/domain/<domain>`), the UK company register for UK firms, and any news. Red flags: any fee, ID documents before an offer, no footprint plus a brand-new domain, US-only work authorisation, nationals-only roles.
3. **Give a verdict:** apply, apply as a backup, or skip, with the reason in two or three lines. Skip without tailoring when he isn't legally eligible to work there, when the core requirements are outside his field, or when it's a 3+ year senior role. When a post has no details at all, use the base CV and an email that asks for the details.
4. **Tailor the CV.** Add `cv/variants/<slug>.py`: import from `cv_content` (or from another variant whose requirements match), override `TITLE`, `SUMMARY`, `SKILLS` and project bullets or order, and set `FILE_STEM = "Ahmed_Dorra_CV_<Company>"`. Build it with `cd cv && CV_MODULE=variants.<slug> python3 build_cv.py ../out`. It must stay at 2 pages: check with `pdfinfo`, render page 1 with `pdftoppm -r 70 -png -f 1 -l 1`, and look at the image. When a cover letter file is needed, add `COVER_LETTER` (date, to, greeting, paragraphs, closing) to the variant and build it with `cd cv && CV_MODULE=variants.<slug> python3 build_cover_letter.py ../out`; it must stay at 1 page.
5. **Write `applications/<doc-id>.md`.** Include: the posting, how to apply (address, the exact subject line they ask for, the attachment), the verdict and the company check; the email, ready to paste; likely questions or interview prep; and the original post, quoted.
6. **Deliver.** Upload both files to the tracker, add the row as `Ready to send`, send him the PDF and the `.md` with `SendUserFile`, then commit and push to this repo.
7. **Reply in a few lines:** the verdict, what was tailored, exactly how to send it, and the tracker status.

## Searching for openings (when he asks what to apply for)

A missed opening costs him more than a slow search. Be exhaustive and say what was covered.

- **Never drop a post for its age.** Older posts are often still open. Check whether each one is open instead:
  - Workday: `/wday/cxs/<tenant>/<site>/job/<path>` returns `canApply`.
  - Greenhouse: `boards-api.greenhouse.io/v1/boards/<board>/jobs/<id>`.
  - Workable, Lever and Zoho pages show the post or an error.
- **Search every source, every time.** Use the CLIs in `ai-job-search-dev/ai-job-search` (clone it):
  - freehire: `--country EG` or `--region mena|global`, with no `--jobage`, paging until the results run out.
  - LinkedIn guest search: no `--jobage`, pages 1–5 per query.
  - The careers portals of the big Egyptian AI employers listed in `referrals/egypt-targets.md`: CIB (Taleo), PwC ETIC and Valeo (Workday), Orange (iCIMS), Vodafone, Raya (Oracle), Henkel (Cornerstone) and Capgemini.
- **Keep combined-level titles.** "AI Engineer / AI Senior Engineer" has a junior level, so don't filter it out for containing "Senior".
- **Wuzzuf, GulfTalent and Bayt block automated reads.** Say so and ask him to paste posts or forward alerts. Don't try to get around the blocks.
- **Report coverage in the reply:** which sources were searched, how many posts were read, and what was skipped and why.

## Truthfulness rules (non-negotiable)

Only use claims verified against his repositories or confirmed by him.

- **Never claim:**
  - YOLO / object detection
  - n8n
  - TypeScript / JavaScript
  - TensorFlow (he's stronger in PyTorch and Hugging Face)
  - Azure / Copilot Studio
  - speech (STT / TTS)
  - OCR
  - vector-based memory: the Shopping Assistant's long-term memory is typed facts in PostgreSQL, plus a LangGraph Postgres checkpointer for conversation state
- **Arabic Banking Intent Classifier** (repo `arabic_banking_intent`, finished Nov 2026) is added to every CV at build time by `cv/arabic_intent_project.py` (full entry on ML/NLP-titled CVs, one bullet elsewhere; VISIONEER is dropped from CV projects but stays on the portfolio and as a paper). Numbers are from that repo's README; don't mention the laptop-CPU remark.
- **Not his work, so keep them off the CV:** Dialogue Summarization (QLoRA) and the old Banking Intent Classifier. Their replacements are planned in `plans/` (Project 1: Arabic banking intents; Project 2: the Egyptian support-ticket model). Add them to the CV only with their measured results, once finished.
- **Research Assistant:** he designed the agent, and Claude built most of the rest. Describe the design; don't overstate the implementation.
- **VISIONEER (2024):** he and a colleague did the LoRA fine-tuning; the teammate trained the schematic model.
- **Shopping Assistant numbers**, verified in that repo's `README.md`, `docs/evaluation.md` and `eval/IMPROVEMENT_LOG.md`:
  - 12,730 products.
  - Retrieval was measured on 127 labelled queries with 95% confidence intervals. Top-10 recall: 72% hybrid vs 56% keyword vs 41% vector.
  - Reranking moved the right product to first place from 23% to 43% (40-query subset).
  - The HNSW index cut median vector-search latency from 35 ms to 3.1 ms.
  - The agent evaluation used 12 tasks × 3 runs:
    - Prompt v2 passed 12 of 12 tasks vs 7, with 29% fewer paid rerank calls.
    - v3 moved price and rating limits inside search: matching results 70% to 100% (57/81 → 48/48), with 15% fewer paid searches.
  - Guardrails refused 0 of 21 legitimate facts. The `prices_grounded` check passed in 25 of 25 applicable runs.
  - 104 tests. `MAX_FACTS_PER_USER = 50`.
  - Ingestion uses pandas loaders for 5 file formats plus row-level Pydantic validation.
- **Still to confirm with him:**
  - military service dates (the CV assumes 01/2025 – 01/2026);
  - the internship partners' exact names (IBM and an Abu Dhabi entity);
  - whether VISIONEER was his graduation project.

## Profile facts

- Giza, Egypt · +20 100 614 8440 · newahmed1672022@gmail.com · linkedin.com/in/ahmed-mostafa-dorra · github.com/AhmedMostafa167 · ahmedmostafa167.github.io
- Egyptian; open to relocation and remote work. He has no US work authorisation.
- BSc Computer Science (06/2024). Military service after graduating, then Teaching Assistant since 03/2026 (he started on 1 March 2026; there was no earlier TA period).
- Also AI Research & Mentorship Engineer at the MLOps MENA Community since 08/2026 (confirmed 1 Nov 2026): mentors community learners on their MLOps/AI projects (reviews their work, answers questions) and researches AI/MLOps topics and writes technical material. No numbers given yet, so don't invent counts.
- TA work (confirmed 29 Oct 2026): teaches Advanced Operating Systems to 700+ students (processes and threads, CPU scheduling, synchronization and deadlocks, memory management and virtual memory, file systems) and a starter MLOps course to about 500 students modelled on ML Zoomcamp (preprocessing and cleaning, a linear model on a churn dataset, project layout, MLflow, FastAPI, Docker). Also: 50 Compiler Theory labs for 600+ students, Distributed Computing quizzes, assisted two 2025/26 graduation projects (social-media trend and emotion analysis; diabetes detection with ML).
- Native Arabic speaker: mention it for Arabic, MENA or GCC-facing companies.
- Notice period, expected salary and years of experience haven't been given yet, so leave `[FILL IN]` placeholders.

## Setup

`.claude/settings.json` installs `cv/requirements.txt` when a session starts. The cloud image already has Chromium at `/opt/pw-browsers/chromium` and poppler (`pdfinfo`, `pdftotext`, `pdftoppm`). Build outputs go to `out/`, which is git-ignored, and the tracker keeps every PDF that was sent.
