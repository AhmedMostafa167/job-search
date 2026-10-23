# Project 1 — Arabic banking intents across dialects

Status: **approved in outline on 2026-10-23; the detailed plan still needs Ahmed's approval** (working agreement §2–§3).
Suggested repo: `arabic-banking-intents` (standalone, private until release). Expected time: about 1 week part-time.
This is the first of two linked fine-tuning projects on one theme, **Egyptian banking customer support**. Project 2 is `02-masry-support-ticket.md`.

## The question it answers

When a model is trained only on standard Arabic (MSA) and Palestinian banking messages, **which approach copes best with Egyptian dialect and Franco (Arabizi) it never saw?** And what does each approach cost in speed and money?

## Data (checked on 2026-10-23)

- `SinaLab/ArBanking77` on the Hugging Face Hub, the Arabic version of BANKING77 with 77 intents. Its public files are a sample:
  - `Banking77_Arabized_MSA_PAL_train_sample.csv`: 1,078 rows, columns `label` (the Arabic intent name) and `text`;
  - `..._MSA_PAL_val_sample.csv`, `..._MSA_test_sample.csv`, and `..._PAL_test_sample.csv` (191 rows);
  - `Banking77_intents.csv`: the intent names.

  First task: check whether the full dataset from the ArBanking77 paper (SinaLab, 2023) is published elsewhere. If it isn't, work with the sample and say so in the README.
- The English `PolyAI/banking77` (CC-BY-4.0, about 13k rows) is optional, for cross-lingual experiments.
- **Ahmed's Egyptian test set:** about 150–200 messages that Ahmed writes himself, in Egyptian Arabic script and in Franco, labelled with the ArBanking77 intents. Write it before looking at any model's errors. Version it with DVC, and **never** use it for training or tuning.

## Approaches compared, all on the same test sets

1. **Baseline:** TF-IDF plus logistic regression. Try character n-grams too, since they cope better with dialect spelling.
2. **A fine-tuned Arabic encoder:** a dialect-aware BERT, either `CAMeL-Lab/bert-base-arabic-camelbert-da` or `UBC-NLP/MARBERTv2`, picked on the validation set.
3. **LoRA on a small LLM:** `Qwen3-0.6B` with a sequence-classification head, using PEFT.
4. **A prompted LLM, zero-shot and few-shot,** given the 77 intent names.

## Metrics

- Accuracy and **macro-F1**, reported separately for each test set: MSA, Palestinian, Egyptian Arabic script, Egyptian Franco.
- The pairs of intents most often confused with each other, and one targeted fix that is then measured.
- Response time (p50 and p95, on CPU and GPU) and cost per 1,000 requests.

## Standards (`mlops-model-lifecycle` skill)

- DVC for the data and the Egyptian test set; MLflow for runs and the model registry.
- A promotion gate: the model is promoted only if its macro-F1 on the Egyptian set beats the baseline by an agreed margin and its p95 CPU response time stays under an agreed limit. Agree both numbers before training.
- The tokenizer and label map travel with the model; publish on the Hub with a model card.
- A FastAPI `/predict` endpoint that returns the top 3 intents with confidence scores. Docker, pytest and GitHub Actions CI.
- README with a results table; `eval/IMPROVEMENT_LOG.md` (each entry includes Ahmed's prediction next to the result); `docs/LESSONS.md`.

## Learning prerequisites

- Hugging Face LLM course chapter 3 (done); chapter 4 sections 3–4 (sharing models, model cards).
- The PEFT library's LoRA quick tour.

## Compute

A free Kaggle or Colab GPU (T4). The cloud Claude session has no GPU: Claude prepares the code and configs, and Ahmed runs the training.

## Outcome for the CV

One bullet with the real numbers, for example: "Fine-tuned Arabic BERT and LoRA-on-LLM intent classifiers; measured the dialect gap (MSA → Egyptian / Franco) and cost per 1k requests against a prompted LLM." Write the final wording only once the numbers exist.
