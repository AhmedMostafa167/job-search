# Petrochoice Integrated Services — AI Engineer (oil & gas), Egyptian candidates only

- **Posting:** shared text (copied below). Seen 16 Oct 2026.
- **Apply:** send an email to **hr.Petrochoice@gmail.com**. The subject must be exactly **AI Engineer**. Attach `Ahmed_Dorra_CV_Petrochoice.pdf`.
- **Verdict: apply. Strong on deployment, one gap.**
  - You meet most of the requirements:
    - designing a system;
    - building APIs with FastAPI;
    - Docker;
    - deploying locally and in the cloud;
    - collecting data and training models (partly: LoRA fine-tuning on ~12k images).
  - The gap is **YOLO / object detection**, which isn't on your CV and isn't claimed anywhere.
- **Company:** a small oil and energy services firm in Maadi, Cairo, founded in 2023 with about 10–50 staff (per a directory listing). Its work includes drilling, wellhead, HSE (health, safety and environment) and logistics services. The Gmail HR address is normal for a company this size. Likely AI uses include safety checks from camera feeds (PPE detection, spotting people in danger zones), equipment and corrosion inspection, and reading documents and reports.

---

## Email

**To:** hr.Petrochoice@gmail.com
**Subject:** AI Engineer
**Attach:** Ahmed_Dorra_CV_Petrochoice.pdf

Dear Hiring Team,

I'd like to apply for the AI Engineer position; my CV is attached. I'm an Egyptian Computer Science graduate based in Giza.

I train models and deploy them. I fine-tuned Stable Diffusion with LoRA on about 12,000 images to generate floor plans from text, work that was published in 2025. I also designed and built an AI service end to end: a data pipeline, FastAPI APIs, Docker Compose packaging, monitoring and automated tests, with a second project deployed in the cloud on Hugging Face Spaces. I measure every model change before shipping it; on my latest project, that raised the right result ranked first from 23% to 43%.

I'd be glad to discuss how I could help build AI solutions for your oil and gas operations.

Best regards,
Ahmed Dorra
+20 100 614 8440
github.com/AhmedMostafa167 · ahmedmostafa167.github.io

---

## If they ask about YOLO

Be honest and specific: "I haven't trained YOLO in production yet. My vision training work is generative: LoRA fine-tuning of Stable Diffusion. For detection, I'd fine-tune a pretrained YOLO model with Ultralytics on labelled site images, check mAP (mean average precision) on a held-out set and per class, then serve it with FastAPI in Docker, the same deployment I've already built."

**This gap can be closed in about a week.** One small project would turn it into a strength for this job and for any other computer-vision job: fine-tune YOLO to detect PPE (helmets and vests), which is a real oil and gas safety use case, then serve it through FastAPI and Docker. If you want, we can build it together using our Pair/Solo approach. Say the word and I'll draft the plan first.

## Original post

> We're Hiring: AI Engineer. Petrochoice Integrated Services is looking for an AI Engineer to build smart solutions for the oil and gas industry. Requirements: collecting data and training models in Computer Vision or NLP; training and using CV models such as YOLO; building algorithms and designing the structure of a system; MLOps skills, including building APIs with FastAPI; using Docker; deploying models on local servers and in the cloud. Send your CV to hr.Petrochoice@gmail.com, subject: "AI Engineer". Only for Egyptian candidates.
