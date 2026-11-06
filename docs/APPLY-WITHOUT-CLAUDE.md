# Applying without Claude: the routine

## Every morning (10 minutes)
1. You get an email from GitHub: **"New jobs <date>"** (issue in this repo). It lists new junior AI/ML/data/backend posts, best first.
   - No email? Open the repo → **Actions** → **Daily job sweep** → **Run workflow**, then open the newest file in `shortlists/auto/`.
2. Twice a week, also check by hand what the sweep can't read: **Wuzzuf, Bayt, GulfTalent** and the company portals in `referrals/egypt-targets.md` (CIB, PwC ETIC, Valeo, Orange, Vodafone, Raya, Henkel, Capgemini). Set up job alerts on those sites with the same keywords.
3. Open each promising post and decide in two minutes:
   - **Skip** if it needs 3+ years, a US work permit, or a nationality you don't have, or if it asks for any fee or ID before an offer.
   - **Apply** if most of the core skills match your CV.
   - **Backup** if it's a stretch but possible.

## Pick the CV (all in `cv/` → build, or use the ready PDFs in `cv/ready/`)
| The post is about… | Send |
|---|---|
| LLMs, RAG, agents, GenAI | `Ahmed_Dorra_CV_General_LLM_Agents.pdf` |
| ML engineer, MLOps, model serving | `Ahmed_Dorra_CV_General_ML_MLOps.pdf` |
| Data scientist, analytics + ML | `Ahmed_Dorra_CV_General_Data_Scientist.pdf` |
| Python/backend with some AI | `Ahmed_Dorra_CV_General_Python_Backend.pdf` |
| Arabic NLP, MENA/Gulf companies | `Ahmed_Dorra_CV_General_Arabic_NLP.pdf` |
| Graduate programme, junior, internship | `Ahmed_Dorra_CV_General_Junior_Graduate.pdf` |
| Trainer, instructor, mentor | `Ahmed_Dorra_CV_General_AI_Instructor.pdf` |
| None of these | `Ahmed_Dorra_CV.pdf` (the general one) |

Rename nothing: the file name `Ahmed_Dorra_CV_...pdf` already looks professional.

## Tailor in 5 minutes (when a post is a close fit)
1. Copy the closest file in `cv/variants/` (for example `general_llm.py`) to `cv/variants/<company>.py`.
2. Change `FILE_STEM`, `TITLE` (echo the post's job title) and `SUMMARY` (two sentences using the post's own keywords).
3. Reorder `SKILLS` so the post's tools come first. Only list tools you have really used.
4. Build: `cd cv && CV_MODULE=variants.<company> python3 build_cv.py ../out` (needs `pip install -r cv/requirements.txt` and Chromium). It must stay at 2 pages.
5. Never add: YOLO, n8n, TypeScript/JavaScript, TensorFlow, Azure/Copilot Studio, speech (STT/TTS), OCR, vector memory.

## Send
- Use `templates/email.md` or `templates/cover-letter.md`, and the exact subject line the post asks for.
- Always attach the PDF. Check the email address twice.
- For portals (Workday, Taleo, Zoho): create one account per company, upload the CV, paste the answers from `templates/answers.md`.

## Track
Keep a row per application in the tracker (or `tracker/applications-template.csv` if the claude.ai tracker is unavailable): company, role, link, CV sent, date applied, follow-up date (7 days later), status. Follow up once after 7 days, politely.

## Truthfulness rules (never break them)
Only claim what is in your repos or what you can explain in an interview. Details: `CLAUDE.md`, section "Truthfulness rules".

## Keep the CVs current
Edit `cv/cv_content.py` (and `cv/arabic_intent_project.py` for the Arabic project) when something changes, rebuild, and upload the new general CV to Drive (Manage versions) and `assets/Ahmed_Dorra_CV.pdf` in the `AhmedMostafa167.github.io` repo.
