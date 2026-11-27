# LinkedIn MCP: setup and rules

Server: [stickerdaniel/linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server) (free, Apache-2.0), pinned to **4.31.0**.
It runs on Ahmed's own computer, in the Claude desktop app, using his own LinkedIn login. It can search jobs, read
posts, list saved jobs, tell Easy Apply from external applications, and read Easy Apply forms. **It never submits an
application.** Ahmed clicks Apply himself.

## Setup in the Claude desktop app (easiest: one-click bundle, no terminal)

1. Install the **Claude desktop app** from claude.ai/download and sign in.
2. Download the `.mcpb` file from the server's latest release:
   https://github.com/stickerdaniel/linkedin-mcp-server/releases/latest (under "Assets").
3. Double-click the downloaded `.mcpb` file. The desktop app opens and asks to install the LinkedIn extension: click **Install**.
   The bundle is a fixed version, so it doesn't silently update itself.
4. In a new chat, ask: "Check my LinkedIn session status." The first time, a LinkedIn sign-in opens (in the chat or a browser window).
   Sign in and approve on your phone if LinkedIn asks. If you're already signed in to LinkedIn in Chrome/Edge, it may reuse that.
   Early calls can say "setup in progress" while it downloads its browser: wait a minute and ask again.
5. Settings → Extensions (or the 🔨 tools menu) → LinkedIn: set `send_message`, `connect_with_person`,
   `reply_to_conversation`, `archive_conversation` and `get_inbox` to **Never allow / off**. Leave the job tools on, set to "Ask" if you want to approve each call.
6. Paste the starter prompt below.

Windows only: if it fails with "DLL load failed ... _greenlet", install the Microsoft Visual C++ Redistributable
(https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist) and restart the app.

### Alternative: config file + uv (if the bundle doesn't work)

1. Install uv — Windows PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`; Mac: `curl -LsSf https://astral.sh/uv/install.sh | sh`.
2. Run `uvx mcp-server-linkedin@4.31.0 --login` and sign in.
3. Settings → Developer → Edit Config:
   ```json
   { "mcpServers": { "linkedin": { "command": "uvx", "args": ["mcp-server-linkedin@4.31.0"], "env": { "UV_HTTP_TIMEOUT": "300" } } } }
   ```
4. Quit and reopen the app.

## Safety rules (to protect the LinkedIn account)

- Use it only for jobs: `search_jobs`, `get_job_details`, `get_saved_jobs`, `get_job_apply_url`, `get_easy_apply_form`, `get_company_profile`.
- **Do not** use `send_message`, `connect_with_person`, `reply_to_conversation`, `get_inbox` or `search_people` for automation. In the desktop app, set these tools to "Never allow".
- Keep it light: at most ~2 sessions a day and ~20 searches per session. No overnight loops.
- Keep the version pinned. Update deliberately (change `4.31.0` to a newer release) if LinkedIn changes break it.
- If LinkedIn shows a warning or a captcha, stop for a few days.

## Starter prompt for the desktop app

> You're helping me (Ahmed Dorra) find and apply to AI/ML jobs. Read the "00 START HERE" and "02 CLAUDE.md" documents in my Google Drive (Resume → AI Agent Handoff), or the job-search repo if you have it. Follow the truthfulness rules exactly. Using the LinkedIn tools, search for: Junior AI Engineer, AI Engineer, Machine Learning Engineer, LLM Engineer, Generative AI Engineer, Data Scientist, MLOps Engineer, in Egypt, United Arab Emirates, Saudi Arabia, Qatar and Remote, posted in the past week. Skip jobs needing 5+ years, a nationality I don't have, or a language I don't speak. For each good one, give me: title, company, location, link, Easy Apply or external, a 2-line verdict, and which of my general CVs to use. Don't message anyone or send connection requests. Then, for each Easy Apply job I pick, read the form with get_easy_apply_form and give me the answers to paste, using my Easy Apply answer sheet. Never submit anything yourself.

## Easy Apply answer sheet

Contact and links
- Name: Ahmed Dorra
- Email: ahmed.dorra.ml@gmail.com
- Phone: +20 100 614 8440 (Egypt, +20)
- City: Giza, Egypt
- LinkedIn: https://www.linkedin.com/in/ahmed-mostafa-dorra
- GitHub: https://github.com/AhmedMostafa167
- Portfolio / website: https://ahmedmostafa167.github.io
- CV link (public): https://drive.google.com/file/d/1P_Tqwkuk-Yt_s2tsKK46PVKecZLfShMt/view?usp=sharing
- CV file to upload: pick from cv/ready (or Drive → Resume → CVs 2026-11-25):
  LLM/agents → General_LLM_Agents · ML/MLOps → General_ML_MLOps · Data science → General_Data_Scientist ·
  Python backend → General_Python_Backend · Arabic NLP / Gulf → General_Arabic_NLP · Graduate / junior / intern →
  General_Junior_Graduate · Trainer / mentor → General_AI_Instructor · anything else → Ahmed_Dorra_CV

Eligibility
- Work authorisation: Egyptian citizen. Authorised to work in Egypt. Needs visa sponsorship anywhere else (answer "Yes, I will require sponsorship" outside Egypt).
- Willing to relocate: Yes. Remote: Yes. Hybrid/on-site in Cairo or Giza: Yes. Any time zone: Yes.
- Military service: Completed (01/2025 – 01/2026) [confirm dates].
- Driver's licence, disability, gender, ethnicity: answer yourself or "Prefer not to say".

Education and languages
- Highest degree: Bachelor of Science in Computer Science, Culture and Science City, Giza (2020–2024).
- English: Professional working proficiency. Arabic: Native.

Experience questions (answer honestly; adjust to the exact wording)
- Total professional experience: [FILL IN — suggested: "about 1 year" (TA since 03/2026, MLOps MENA since 08/2026, research internship 12/2023–03/2024); confirm before using]
- Python: [FILL IN — suggested 2+ years incl. projects since 2023]
- Machine learning / deep learning (PyTorch, Hugging Face): [FILL IN — suggested 2 years]
- LLMs / RAG / LangChain / LangGraph: [FILL IN — suggested 1 year]
- FastAPI, SQL/PostgreSQL, Docker, Git: [FILL IN — suggested 1–2 years]
- Tools never to claim: YOLO/object detection, n8n, TypeScript/JavaScript, TensorFlow, Azure/Copilot Studio, speech (STT/TTS), OCR.

Money and timing
- Expected salary: [FILL IN]
- Notice period / start date: Available to start immediately.

Short answers
- "Why are you interested?": write 2 sentences specific to the company (the desktop app can draft from the post).
- "Tell us about a project": use the Answer bank doc (Shopping Assistant or the Arabic Banking Intent Classifier).
- Cover letter field (optional): use the short note from the tracker row, or ask the app to draft one.
