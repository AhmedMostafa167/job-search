# Project plans

These are the fine-tuning projects that complete Ahmed's CV, agreed on 2026-10-23. **No retrieval (RAG) in these projects:** he already has two RAG projects.

- `WORKING_AGREEMENT.md`: how Claude and Ahmed work (plumbing vs core work, Drive / Pair / Solo, plan approval, predictions, lessons log). It applies in every project session.
- `01-arabic-banking-intents.md`: Project 1. Start here.
- `02-masry-support-ticket.md`: Project 2, the flagship, which comes after Project 1.

## Starting a project session

1. Ahmed creates an empty repo for the project (Claude can't create repos) and opens a Claude Code session on it.
2. He says something like: "Read `plans/WORKING_AGREEMENT.md` and `plans/01-arabic-banking-intents.md` from AhmedMostafa167/job-search and set up this repo."
3. In that session, Claude adds `AhmedMostafa167/job-search` (read access is enough) and reads the two files. Then it:
   - copies the working agreement into the project's `CLAUDE.md`, adding a project section that points to `docs/PLAN.md`;
   - copies the plan into `docs/PLAN.md`;
   - sets up the plumbing (repo layout, DVC, MLflow, CI, Docker) — this is plumbing, so it just does it;
   - asks Ahmed which mode (Drive, Pair or Solo) to use for the first core task, and writes the detailed plan for his approval before any core code.
4. When a project finishes, update its status here and in the job-search `CLAUDE.md` (truthfulness rules and CV facts) so the CV can use the real numbers.
