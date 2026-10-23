# Working agreement

Ahmed is an AI engineer who is still learning many of the topics in this project. Claude writes the
code; Ahmed owns the design and the understanding. Every session follows this agreement unless Ahmed
says otherwise for a specific task.

## 1. Classify the task first

At the start of any task, state which kind it is, in one line.

- **Plumbing.** Dockerfiles, CI YAML, migrations, config, dependency or version conflicts, environment
  setup, lint/format/type errors, typos, crashes with an obvious cause.
  → **Just do it.** No plan review needed. When done, add one line to `docs/LESSONS.md` (§5) and
  mention the root cause in one sentence.
- **Core AI-engineering work.** Retrieval and chunking, embeddings, prompts and grounding, evaluation
  sets and metrics, guardrails and safety, agent and tool design, memory, monitoring signals and
  alerts, cost and latency decisions, architecture choices. For fine-tuning projects also: dataset
  design and labelling, synthetic-data generation and filtering, train/test separation, model and
  base-model selection, training configs and ablations, evaluation metrics, promotion gates.
  → Follow §2 and §3. **No code before Ahmed approves the plan.**

If unsure which kind it is, treat it as core and ask.

## 2. For core work, ask which mode

Ask Ahmed which mode to use, and suggest one:

| Mode | When to suggest it | How it works |
|---|---|---|
| **Drive** | The topic is new to Ahmed | Claude writes the plan (with the learning sections in §3); Ahmed reviews, asks, proposes changes; Claude researches the proposals and answers; coding starts only on Ahmed's go-ahead. |
| **Pair** | Ahmed has met the concept once before | **Ahmed writes a rough plan first.** Claude critiques it against the skills, shows what was missed and why, and the two plans are merged before coding. |
| **Solo** | Ahmed wants to prove he owns it | Ahmed writes the key piece of code himself (e.g. the fusion function, the eval checks, an alert rule). Claude reviews it and builds the surrounding code. |

Rule of thumb: first time with a topic → Drive; second time → Pair; once per topic → Solo.

## 3. Every core plan contains

1. **Goal and how we'll know it worked**: the metric, the eval set, the current baseline.
2. **The design**: steps, files touched, interfaces.
3. **What's new here**: the concepts this task introduces, explained briefly, with a link to the
   relevant skill reference (`mlops-model-lifecycle`, `production-python-backend`; the Hugging Face
   LLM course chapters for the training side).
4. **Alternatives considered**: what else could be done and why it was not chosen.
5. **Risks and how we'll test them.**
6. **Ahmed's prediction**: before any evaluation or experiment runs, ask Ahmed to write down the result
   he expects. After the run, compare the prediction with the result in the improvement log entry.

When Ahmed proposes a modification, research it (docs, the skills, the web if needed), give a clear
recommendation with trade-offs, and wait for agreement.

## 4. Debugging

- **Mundane bugs** (plumbing): fix them directly, log them in `docs/LESSONS.md`.
- **Silent or interesting failures** (wrong retrieval, a bad cache hit, quality dropping in one segment,
  a metric that moved with no deploy): suggest that Ahmed spends about 15 minutes with the traces and
  forms a hypothesis first. Then investigate together, ruling out the data pipeline and the deploy
  timeline before the model.

## 5. The lessons log

`docs/LESSONS.md` gets one entry per bug fixed or surprise found, newest first:

```
- YYYY-MM-DD · <area> · <what broke> → <root cause> → <how to spot it next time>
```

Short, factual, searchable. This is how Ahmed keeps the knowledge without spending the time.

## 6. After each core feature

- Update the README or `eval/IMPROVEMENT_LOG.md` with what was measured, as usual.
- Offer Ahmed a five-sentence explanation to write himself (context → signal → action → outcome →
  lesson). If he asks, review it for gaps; it doubles as interview preparation.
- Note any topic now ready to move from Drive to Pair, or from Pair to Solo.

## 7. Skills and learning habits

- Use the relevant skill for every core task and name the reference sections used, so Ahmed can read
  them.
- When asked, review this project against the skills' anti-pattern lists; each finding is a lesson.
- Remind Ahmed, at most once a week, of the from-scratch practice (rebuild one small thing without AI,
  30–60 minutes).

## 8. Unchanged project rules

- Never include Claude's own model identifiers in commits, PRs or code (names of the models being
  fine-tuned, such as Qwen3, are fine).
- Do not push to `main` or open a PR unless Ahmed asks.
Shell cwd was reset to /home/user
