# AI Engineer (89184) and Software Developer – GEN AI Solutions (89134) — Henkel (New Cairo, hybrid)

- **Postings:** two Henkel Cornerstone requisitions with the same profile, both open on 29 Oct 2026:
  - AI Engineer, req **89184**, posted 5 Oct 2026: https://henkel.csod.com/ux/ats/careersite/1/home/requisition/89184?c=henkel
  - Software Developer – GEN AI Solutions, req **89134**: https://henkel.csod.com/ux/ats/careersite/1/home/requisition/89134?c=henkel
- **Apply:** open each link → **Apply now** → sign in or create a Henkel candidate profile (the same one works for req 86074) → upload `Ahmed_Dorra_CV_Henkel_GenAI.pdf` → paste the note below where it asks for a message. Apply to **both**; one CV covers them.
- **Verdict: apply (stretch on years).**
  - They ask for 3–4 years. The work is generative models: **fine-tuning LLMs and diffusion models**, prompt strategies, PyTorch, transformers, NLP and computer vision, Docker, GenAI apps, and chatbots connected to services through REST APIs.
  - VISIONEER (LoRA fine-tuning of Stable Diffusion, published) is a rare match for the diffusion ask. The Shopping Assistant covers the chatbot, REST API and Docker asks.
  - **Gaps (not claimed):** TensorFlow, Kubernetes, C#/.NET, Power BI, Azure Cognitive Services / Azure OpenAI, RLHF, audio, and Databricks (89134).
  - You already have Henkel's agentic AI Engineer role (req 86074) as Ready to send. These are separate requisitions, so it's fine to apply to all three.
- **Company check: no red flags.** Henkel is a German multinational (adhesives and consumer brands) with a digital hub in New Cairo. The posts are on Henkel's own Cornerstone portal. No fee, no ID.

---

## Note to paste (message box or cover note)

Hello Henkel Talent Acquisition team,

I'm applying for the AI Engineer role (req 89184) and the Software Developer – GEN AI Solutions role (req 89134) in New Cairo. Your posts ask for fine-tuning of LLMs and diffusion models, and that's the work I know best. With a colleague, I fine-tuned Stable Diffusion with LoRA on about 12,000 captioned floor plans to generate furnished layouts from text, published in Machine Graphics & Vision (2025). I also build LLM applications in Python: a LangGraph chatbot agent with RAG and tool calling, served through a FastAPI REST API in Docker, with tests, tracing and monitoring. On that assistant, a revised prompt raised task success from 7 to 12 of 12 test tasks with 29% fewer paid rerank calls.

I have less than the 3–4 years you list, and I haven't worked with C#/.NET or Power BI yet. I learn fast and measure what I build. I'm based in Giza and can start soon.

GitHub: github.com/AhmedMostafa167
Portfolio: ahmedmostafa167.github.io
LinkedIn: linkedin.com/in/ahmed-mostafa-dorra

Best regards,
Ahmed Dorra
+20 100 614 8440 · newahmed1672022@gmail.com

---

## Interview prep

- **VISIONEER in depth:** why LoRA instead of full fine-tuning (memory, a small dataset of ~12k images), how the captions were built, rank and learning-rate choices, how you judged layout quality, and what the teammate's schematic model did. Say clearly that the fine-tuning was shared with a colleague.
- **Diffusion basics:** the forward/backward noising process, the U-Net and text encoder, classifier-free guidance, schedulers, and where LoRA adapters attach (attention layers).
- **LLM fine-tuning (no shipped project):** explain LoRA/QLoRA for LLMs, SFT data formats, and when RAG beats fine-tuning. Be honest that your LLM work is RAG and agents, not LLM fine-tuning.
- **RLHF (asked as "experiment with"):** reward model, PPO vs DPO, preference data. Theory only.
- **Chatbot + REST:** the Shopping Assistant's FastAPI endpoints, Pydantic schemas, Docker Compose, Langfuse tracing and the 104 tests.
- **Azure gap:** say you've used Anthropic, OpenAI, Groq and Hugging Face APIs through one provider factory, so switching to Azure OpenAI is a configuration change.
- **Ask them:** which business units the GenAI team serves, how image/multimodal work splits from LLM work, and whether the two requisitions are the same team.

---

## Original post

### AI Engineer (89184)

> Source: https://henkel.csod.com/ux/ats/careersite/1/home/requisition/89184?c=henkel (read 2026-10-29)
>
> AI Engineer
> 2 locations available
> |
> 26102264
> Apply now
> Share
>  Save Job
> Posted on: 05/10/2026 – Application Deadline: -
>  Back to Search
> Job available in these locations:
> New Cairo, Egypt
> Cairo, CAIRO, Egypt
> About this Position
> The AI Engineer focuses primarily on the development of GenAI Solutions and is involved in Data Science Projects. They design, develop, and deploy advanced AI models that leverage generative techniques for text, image, audio, and multimodal applications. They have a broad technical knowledge with Microsoft Azure and OpenAI technologies that can help them develop solutions that meet business requirements. They exchange with different stakeholders to share advice & knowledge. They help evaluate new technologies in the area of GenAI, and they support to govern the environment.
>
> What you´ll do
> Design and implement generative AI models using frameworks like PyTorch or TensorFlow.
> Fine-tune pre-trained LLMs (e.g., GPT, LLaMA) and diffusion models for domain-specific tasks.
> Develop effective prompts and strategies for improving model outputs.
> Experiment with reinforcement learning from human feedback (RLHF) and other optimization techniques.
> Manage business requests for new solutions.
> Work closely with the business analyst to reach optimum solution for the business.
> Work Closely with Data Engineers & DevOps Engineers to ensure scalable data pipelines & deployment.
> Stay updated with the latest advancements in generative AI, LLMs, and multimodal models.
> Evaluate new technologies that are being published by Microsoft and OpenAI.
> Maintain and enforce rules and standards and foster guiding principles.
> Run the quality gate to review and check development before final deployment.
> Regular review and maintenance of services and site catalogs incl. channel integration and more.
> Identify the best technology to be used for each use case.
> What makes you a good fit
> Bachelor's degree in Computer Science, Business informatics, Development, or any relevant study
> 3-4 years of relevant work experience
> Fluent English speaker with excellent communication skills (both verbal and written) and teamwork abilities.
> Strong proficiency in Python and ML frameworks (PyTorch, TensorFlow).
> Experience with LLMs, transformers, and diffusion models.
> Knowledge of NLP, computer vision, and multimodal AI.
> Familiarity with cloud services and containerization (Docker, Kubernetes).
> Experience in designing, developing, and deploying GEN AI applications.
> Experience in integrating chatbots with third-party services via RESTful APIs.
> Familiar with C# and .NET Framework
> Experience in PowerBI in analytics and reporting
> Experience in Microsoft Azure Cognitive services (Azure search, Document Inteliigence, Azure Open AI) is a plus.
> Some perks of joining Henkel
> Flexible work scheme with flexible hours, hybrid work model, and work from anywhere policy for up to 30 days per year
> Diverse national and international growth opportunities
> Global wellbeing standards with health and preventive care programs
> Gender-neutral parental leave for a minimum of 8 weeks
> Employee Share Plan with voluntary investment and Henkel matching shares
> Comprehensive Health Insurance for employee + dependents
> Employee Assistance Programme provides a wide range of mental health and wellbeing benefits
>
> At Henkel, we come from a broad range of backgrounds, perspectives, and life experiences. We believe the uniqueness of all our employees is the power in us. Become part of the team and bring your uniqueness to us! We look for a diverse team of individuals who possess different backgrounds, experiences, personalities and mindsets.

### Software Developer – GEN AI Solutions (89134)

> Source: https://henkel.csod.com/ux/ats/careersite/1/home/requisition/89134?c=henkel (read 2026-10-29)
>
> Software Developer - GEN AI Solutions
> 2 locations available
> |
> 26102153
> Apply now
> Share
>  Save Job
>  Back to Search
> Job available in these locations:
> New Cairo, Egypt
> Cairo, CAIRO, Egypt
> About this Position
> The GENI AI Developer focuses primarily on the development of GenAI Solutions and is involved in Data Science Projects. The GEN AI developer designs, develops, and deploys advanced AI models that leverage generative techniques for text, image, audio, and multimodal applications.
>
> What you´ll do
> Development of GenAI Solutions and involvement in Data Science Projects.
> Designs, develops, and deploys advanced AI models that leverage generative techniques for text, image, audio, and multimodal applications.
> Broad technical knowledge with Microsoft Azure and OpenAI technologies that can help them develop solutions that meet business requirements.
> Exchanges with different stakeholders to share advice & knowledge.
> The developers help evaluate new technologies in the area of GenAI, and they support to govern the environment.
> What makes you a good fit
> Bachelor's degree in Computer Science, Business informatics, Development, or any relevant study
> 3-4 years of relevant work experience
> Fluent English speaker with excellent communication skills (both verbal and written) and teamwork abilities.
> Have a strong ability to grasp new concepts with ease.
> Have excellent presentation skills.
> Strong proficiency in Python and ML frameworks (PyTorch, TensorFlow).
> Experience with LLMs, transformers, and diffusion models.
> Knowledge of NLP, computer vision, and multimodal AI.
> Familiarity with cloud services and containerization (Docker, Kubernetes).
> Experience in designing, developing, and deploying GEN AI applications.
> Experience in integrating chatbots with third-party services via RESTful APIs. Familiar with C# and .NET Framework
> Experience in PowerBI in analytics and reporting.
> Databricks.
> Experience in Microsoft Azure Cognitive services (Azure search, Document Inteliigence, Azure Open AI) is a plus.
> Some perks of joining Henkel
> Flexible work scheme with flexible hours, hybrid work model, and work from anywhere policy for up to 30 days per year
> Diverse national and international growth opportunities
> Global wellbeing standards with health and preventive care programs
> Gender-neutral parental leave for a minimum of 8 weeks
> Employee Share Plan with voluntary investment and Henkel matching shares
> Comprehensive Health Insurance for employee + dependents
> Employee Assistance Programme provides a wide range of mental health and wellbeing benefits
>
> At Henkel, we come from a broad range of backgrounds, perspectives, and life experiences. We believe the uniqueness of all our employees is the power in us. Become part of the team and bring your uniqueness to us! We look for a diverse team of individuals who possess different backgrounds, experiences, personalities and mindsets.
