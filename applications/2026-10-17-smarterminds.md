# AI Engineer Intern (paid) — Smarterminds, Giza

- **Posting:** Smarterminds' own careers page (their SmarterATS system), posted 14 Oct 2026, which the LinkedIn post links to. Seen 17 Oct 2026. It's a **paid internship of 3–6 months, with a path to a full-time offer**, for final-year students and recent graduates. No experience is needed. The office is in Giza.
- **Apply:** <https://smarterminds.smarterats.com/careers/262> → **Apply Now** → upload `Ahmed_Dorra_CV_Smarterminds.pdf`. The form starts with the CV upload and probably reads it to fill the fields, so check what it fills in. If there's a message or cover-letter box, paste the note below.
- **Verdict: apply as a backup.** It's a solid local option, but not a top fit.
  - **Why it's worth applying:** the AI work they describe is your strength: "connect LLMs to real product workflows: write prompts, call the APIs, and check whether the output is actually good". Prompt versioning plus code-graded evaluation is what your Shopping Assistant does. It's also paid, near you, and leads to a full-time offer.
  - **The gap:** their stack is **JavaScript, HTML/CSS, React**, SQL and REST APIs, with TypeScript, Next.js and Node.js as a bonus. You have SQL and REST APIs, but none of the JavaScript side, and the CV doesn't claim it. Expect a coding question in JavaScript or React.
  - **If you want this one:** spend a weekend building a small React page that calls your Shopping Assistant API yourself. After that, "basic React" is true and you can add it to the CV.
- **Company check:** no red flags.
  - Smarterminds is a Belgian software firm, founded in 2018 with 11–50 people. Its office is in Brugge. It mainly does embedded and automotive software (AUTOSAR).
  - Its Egypt office is at **Arkan Plaza, Plot 31, Sheikh Zayed (Regus), Giza**, which is close to you.
  - Its domain, smarterminds.net, dates from 2018, the site links to this careers page, and it has a LinkedIn company page and a Wuzzuf profile.
  - SmarterATS, an AI hiring tool, is their own product, and you'd work on it.
  - Nothing asks for a fee or for ID.

---

## Cover note (paste into the form if it has a box, or send on LinkedIn)

**Subject (LinkedIn/email only):** AI Engineer Intern — Ahmed Dorra

Hello Smarterminds team,

I've applied for the AI Engineer Intern position in Giza.

The work you describe, connecting LLMs to real product workflows and checking whether the output is actually good, is what I've spent the last year doing. I built an AI shopping assistant over 12,730 products: a LangGraph agent behind a FastAPI REST API on PostgreSQL, with a storefront that calls it. I versioned its prompts in Langfuse and only promoted a new version after it passed a code-graded evaluation. That process took task success from 7 to 12 of 12 tasks, and a check that every price in a reply comes from real search results passed in all 25 applicable runs.

Matching candidates to jobs in SmarterATS is a retrieval-and-ranking problem much like the one I measured on that project, so I'd be glad to apply the same methods there. My backend is Python and SQL, and I'm keen to work in your JavaScript and React stack and pick it up quickly.

I live in Giza and can be at the Sheikh Zayed office full-time.

Best regards,
Ahmed Dorra
+20 100 614 8440 · newahmed1672022@gmail.com
github.com/AhmedMostafa167 · ahmedmostafa167.github.io

---

## Interview prep

**HR screen**
- **Graduation:** BSc in Computer Science, 06/2024, then military service (01/2025 – 01/2026), then teaching assistant since 02/2026. An internship with a full-time path suits that.
- **Notice period at the TA job:** `[FILL IN]`
- **Expected internship pay:** `[FILL IN]`. Ask what the internship pays first, and what the full-time offer depends on.
- **Start date and hours:** `[FILL IN]`

**Technical (rehearse 1–2 minutes each)**
1. **"Explain one AI thing you built":** this is their main ask. Do the Shopping Assistant in 2 minutes: problem → architecture (agent, hybrid search, reranking, memory) → how you knew it worked (evaluation numbers) → one thing that failed and how you fixed it (prompt v1 stored one-off requests as preferences; v2 fixed it).
2. **Checking whether LLM output is good:** code-graded checks vs LLM-as-a-judge vs human review; when each is worth its cost; groundedness checks (your prices check); running several times because outputs vary.
3. **Prompt workflow:** versioning, staging vs production labels, evaluating before you promote, and tracing each call back to the prompt version that produced it.
4. **An AI feature for SmarterATS:** e.g. matching CVs to a job. Use structured output to parse each CV into fields, then embeddings + keyword search + a reranker, and evaluate against recruiter-labelled matches. Then cover bias and fairness, explaining why a candidate ranked where they did, and keeping a human in the loop ("AI as a partner in hiring").
5. **SQL:** joins, GROUP BY / HAVING, indexes (your HNSW and full-text indexes), and migrations (you used Alembic).
6. **REST APIs:** methods, status codes, validation, pagination, authentication basics.
7. **JavaScript and React basics (the gap):** `let`/`const`, arrow functions, promises and `async/await`, `fetch` to a REST API, React components, props vs state, `useState` and `useEffect`. Learn enough to answer, and say honestly that it's new to you.

---

## Original post (LinkedIn, translated summary)

> 💻 Paid AI Engineering Internship | Smarterminds — شركة Smarterminds فاتحة التقديم على تدريب مدفوع في مجال AI Engineering للطلبة في السنة الأخيرة وحديثي التخرج. 📌 تفاصيل التدريب: مدفوع لمدة 3–6 شهور. المكان: الجيزة، مصر. مش مطلوب خبرة عمل سابقة. إمكانية الحصول على Full-Time Offer بعد التدريب. 🔗 للتقديم: https://lnkd.in/eAdgD4GG
>
> (Paid AI engineering internship for final-year students and recent graduates; 3–6 months; Giza, Egypt; no prior work experience needed; possible full-time offer afterwards.)

## Full posting (careers page)

> **AI Engineer Intern** — Giza, Egypt · Posted October 14, 2026 · Full-Time · Engineering
>
> Interested in building with AI? Come build it with Smarterminds. Smarterminds builds software for clients in Europe. Our SmarterAI team uses LLMs and modern web technology to build tools that solve real problems for real users. One of them is SmarterATS, our AI-powered applicant tracking system for startups and small companies, and it treats AI as a partner in hiring, not an obstacle. As an intern, you won't get side tasks. You'll ship features in SmarterATS and our other AI projects that go live, with senior engineers reviewing your code and direct contact with leadership. At the end there's a clear path to a full-time offer.
>
> **What you'll do:** Build AI-powered features end to end. Connect LLMs to real product workflows: write prompts, call the APIs, and check whether the output is actually good. Learn fast in a small team, where your work gets feedback within days, not months.
>
> **About you:** A recent graduate or final-year student. No professional experience needed. Based in Cairo and able to commute to our office in Giza. You've built one thing that uses AI (an app, chatbot, agent, automation or tool), and you can explain how it works. You are skilled in JavaScript, HTML & CSS, React.js, SQL and database management, and RESTful APIs. Bonus if you know TypeScript, asynchronous JavaScript, Next.js or Node.js backend development.
>
> **What we offer:** Paid internship (3–6 months) with the opportunity for a full-time job offer at the end. Career development path with growth opportunities. Exposure to an international, forward-thinking environment, working closely with senior leadership. A collaborative and supportive workplace where you can be involved and make a real impact. Develop skills in AI working on real projects.
