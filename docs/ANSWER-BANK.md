# Answer bank for application forms

Reusable answers written with Claude (Nov 2026). Every number is verified (see `docs/HANDOFF.md`, section 2).
Adapt the company-specific lines before sending; never send a "Why us?" answer to a second company unchanged.

## Standard fields
- **Years of experience:** [FILL IN, e.g. "Projects and research since 2023; teaching assistant since March 2026"]
- **Expected salary / notice period:** [FILL IN]
- **Work authorisation:** Egyptian citizen; I need visa sponsorship outside Egypt. No US work authorisation.
- **Relocation / remote:** open to both, any time zone.
- **Links:** github.com/AhmedMostafa167 · ahmedmostafa167.github.io · linkedin.com/in/ahmed-mostafa-dorra
- **Best demo link:** https://github.com/AhmedMostafa167/Shopping-Assistant (README has a 1:25 demo video)

## "Share your best project / a link to something you built" (+ what you'd do differently)
> https://github.com/AhmedMostafa167/Shopping-Assistant
>
> It's an AI shopping assistant for an online store: a LangGraph agent behind a FastAPI API that searches a 12,730-product catalogue with hybrid search (PostgreSQL full-text + pgvector + reranking) and remembers each customer's lasting preferences across conversations. I measured every step: on 127 labelled queries, hybrid search found the right product in the top 10 72% of the time vs 41% for vector search alone, and a rewritten prompt took the agent from 7 to 12 of 12 test tasks with 29% fewer paid API calls. What I'd do differently: build the evaluation set from realistic customer requests and gate every merge on it from day one. My worst bug (price and rating limits applied after search instead of inside it) only surfaced when I recorded the demo; fixing it raised correct results from 70% to 100%.

Shorter "rebuild" version (3–4 sentences):
> If I rebuilt it, I'd write the evaluation set first, with realistic and awkward customer requests, and make CI block any merge that lowers the score. My worst bug, price limits handled by a filter tool instead of inside search, only surfaced when I recorded the demo, and fixing it raised correct results from 70% to 100%. I'd also design for many stores from day one, with authentication and per-store data separation, because adding tenancy to a working system is harder than building it in. And I'd test local embedding and reranking models against the hosted ones early, since the paid rerank call was the only per-search cost.

## "Describe a hard bug. What did you think the cause was?" (139 words)
> In my Shopping Assistant, a LangGraph agent over a 12,730-product catalogue, asking for "a phone case under $15" returned about 15 product cards, many of them not phone cases. I first thought it was a display bug: the storefront was showing every product the tools returned, not just the ones the reply mentioned. I fixed the cards, but irrelevant products still came back. Reading the agent's tool calls showed the real cause: the prompt sent any request with a price limit to a filter tool that took no search query, so it returned the first ten products under $15, whatever they were. I moved price and rating limits inside the search as SQL conditions, before ranking, and removed the filter tool. Products of the requested kind went from 70% to 100%, with 15% fewer paid searches.

(It was found and fixed the same day. Alternative story: the Arabic classifier's official validation split leaked paraphrases into training, inflating scores by about 3 points, until he built a grouped split.)

## "Short intro: who are you and what are you obsessed with?" (5 sentences)
> I'm Ahmed Dorra, a Computer Science graduate from Egypt who builds and ships LLM and ML systems in Python. I teach Operating Systems to 700+ students and an MLOps course to about 500, and I mentor learners in the MLOps MENA community. Right now I'm obsessed with evaluation: proving with numbers whether an AI system actually works, not just whether the demo looks good. My latest project is an Arabic banking-intent classifier: fine-tuned AraBERT, served as ONNX behind a monitored API, with a promotion gate that blocks a model unless it beats the current one. I'd love to bring that "measure everything" habit to [COMPANY].

## "What's broken in our product that you'd rebuild with AI?" (HelloPrint example, e-commerce)
> Choosing the right product. Your catalogue is huge and the same item sits in several menus (business cards alone come in Classic, Eco, Deluxe, Special Materials and Multilayered), so a customer who thinks "I need something to hand out at a trade show for 300 people by Friday" has to translate that into a product, paper, finish and quantity, or fall back to a quote request. I'd build a conversational product finder: the customer describes the need, and an agent searches the catalogue and pricing API and returns two or three configured options with real prices and delivery dates, checking every price against the tool results before showing it. It's the pattern from my shopping assistant, where moving constraints like budget inside the search raised correct results from 70% to 100%. I'd measure it on a labelled set of real requests from quote forms and support chats (right product in the top 3), plus time-to-cart and how many quote requests it replaces.

## "Why [company]? Why you?" (Foodics example: agent infrastructure)
> Foodics runs the restaurants and payments of thousands of businesses across the Middle East, and you're building agent infrastructure where evaluation decides what ships; that's exactly the work I want to do, at a scale where reliability matters. I build tool-calling agents and test them like software: my LangGraph shopping agent runs behind FastAPI and PostgreSQL with 104 tests, and a code-graded evaluation (12 tasks × 3 runs) showed a prompt change lifting success from 7 to 12 of 12 with 29% fewer paid calls. I'm a native Arabic speaker who understands the region's merchants and customers, I explain complex systems weekly to the 700+ students I teach, and I'm ready to relocate to Riyadh.

## Short note for LinkedIn / email applications
> Hello, I'm applying for the <role> position. I build LLM agents, RAG and ML services in Python (FastAPI, PostgreSQL, Docker, tests) and measure them: reranking lifted right-product-first from 23% to 43% in my shopping assistant, and an Arabic AraBERT classifier I fine-tuned reaches macro-F1 0.919 and runs as ONNX behind a monitored API. I teach Computer Science to 700+ students and mentor learners in the MLOps MENA community. I'm in Giza, Egypt, and open to relocating or working remotely in any time zone. Code: github.com/AhmedMostafa167. — Ahmed Dorra

## Cover letters already written
Built from `cv/variants/*.py` (`COVER_LETTER`), PDFs in `cv/sent/`: Bending Spoons, CIB, Deeplight, Henkel GenAI, Plata, PwC, Vodafone, Advansys, Unifonic. Reuse their structure: why this role (their words) → main project with numbers → evidence-driven habits → teaching/background → relocation + thanks.
