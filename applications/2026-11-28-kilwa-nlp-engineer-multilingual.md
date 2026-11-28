# NLP Engineer — Multilingual (French / Arabic / Swahili) — Kilwa Technologies

- **Location:** Remote (full-time)
- **Posting:** https://www.kilwa.io/careers/nlp-engineer-multilingual
- **Source:** Ali Turky list (company careers page)
- **CV:** `Ahmed_Dorra_CV_Kilwa.pdf` (variant `cv/variants/kilwa.py`)
- **Tracker id:** `2026-11-28-kilwa-nlp-engineer-multilingual` (priority #3)

## Verdict
**Apply.** Remote full-time NLP role that needs fluency in Arabic *or* French *or* Swahili, so your native Arabic plus the AraBERT classifier (dialect results, grouped split against leakage) is a direct fit. They want a short note on what you'd own and links to shipped work.

## Company check
Chicago-based, remote-first; site lists 9 roles, published research briefs, partners, US SBA SDVOSB certification. kilwa.io registry date not public (.io RDAP). No fees asked.

## How to apply
Email **info@kilwa.io** · Subject: `NLP Engineer — Multilingual (Arabic): Ahmed Dorra` · attach `Ahmed_Dorra_CV_Kilwa.pdf` · body below.

## Email
```
Hello Kilwa team,

I'm applying for the NLP Engineer — Multilingual role. I'm a native Arabic speaker and I build Arabic NLP systems directly in the source language. My latest project fine-tunes AraBERT on 77 Arabic banking intents (macro-F1 0.919 vs 0.887 for TF-IDF) and reports dialect-level results on Saudi, Moroccan and Tunisian text the model never saw. I found that the official validation split leaked paraphrases into training, rebuilt it as a grouped split, and gated promotion in the MLflow registry on a paired bootstrap; the model runs as ONNX behind a monitored FastAPI API.

What I'd want to own: Arabic sentiment and policy-signal extraction, starting with a labelled evaluation set per region and register (Gulf vs North African media), so every model change is measured against translate-first baselines.

Work I've shipped:
- Arabic Banking Intent Classifier: github.com/AhmedMostafa167/arabic_banking_intent
- Shopping Assistant (LLM agent + hybrid RAG, measured on 127 labelled queries): github.com/AhmedMostafa167/Shopping-Assistant
- Portfolio: ahmedmostafa167.github.io

I'm in Egypt, available to start immediately, and happy to work US hours. CV attached.

Best regards,
Ahmed Dorra
+20 100 614 8440 · ahmed.dorra.ml@gmail.com · linkedin.com/in/ahmed-mostafa-dorra
```

## Interview prep
- Why translation pipelines lose nuance: negation, hedging, dialect words, named entities; your answer: evaluate natively per register.
- Low-resource tricks: multilingual encoders (AraBERT/XLM-R), grouped splits, small labelled sets with confidence intervals.
- Be honest: no French/Swahili; Arabic is your lane.
- Sentiment vs intent: same fine-tuning recipe; what changes is labels and evaluation.

## Original post

> NLP Engineer — Multilingual (French / Arabic / Swahili)
> Own the capability almost nobody else in this market has: reading the languages African investment decisions are actually made in.
> LOCATION
> Remote
> TYPE
> Full-time
> TEAM
> Engineering
> What you'll do
> Build and improve sentiment and policy-signal extraction natively in French, Arabic and Swahili.
> Keep nuance intact by processing source languages directly rather than translating to English first.
> Expand regional source coverage and adapt models to region-specific media registers.
> Feed Sentiment Pulse output into the ISI and METI models as a first-class input.
> What you bring
> Multilingual NLP experience, ideally in lower-resource language settings.
> Working fluency in at least one of French, Arabic or Swahili.
> An understanding of where translation pipelines quietly destroy policy nuance.
> How to apply
> Email us with your CV and a short note on what you'd want to own here. Links to work you've shipped are worth more than a cover letter.
> Apply for this role
