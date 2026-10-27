# Canonical (Ubuntu): 3 remote roles, worldwide / EMEA

- **Roles (all open on Greenhouse, 27 Oct 2026):**
  1. **Software Engineer – Edge AI**, home-based, EMEA (Egypt counts): https://job-boards.greenhouse.io/canonical/jobs/2614095. **Best fit.** It asks for your work with AI agents and LLM applications.
  2. **Python and Kubernetes Software Engineer – Data, Workflows, AI/ML & Analytics**, home-based worldwide: https://job-boards.greenhouse.io/canonical/jobs/5703396
  3. **Junior Ubuntu Software Engineer**, home-based worldwide: https://job-boards.greenhouse.io/canonical/jobs/6707669
- **Skipped:** the Graduate Software Engineer role, which only accepts degrees completed in 2025 or 2026 (yours was 2024), and the MLOps Field Engineer role, which needs customer-facing professional experience.
- **Apply:** on each Greenhouse link (no account needed). Upload `Ahmed_Dorra_CV_Canonical.pdf`.
- **Important: the form says answers must be in your own words. AI-written text disqualifies you.** So this pack only lists points to cover; write every answer yourself.
- **Verdict: apply to all three.** Canonical hires worldwide, home-based, and is one of the few big companies that really does hire from Egypt. They weigh academic record, personal projects and writing heavily.
  - **Gaps (not claimed):** Linux beyond everyday use, Kubernetes, Go, C++, Rust, and upstream open-source contributions.
  - Be honest about how much you've used Ubuntu or Linux. If you have, say what for (servers, Docker hosts, WSL, the cloud container you deploy from).
  - Expect a written-interview stage and assessments; the process is long (weeks).
- **Company check: no red flags.** Canonical is the company behind Ubuntu, with 1,200+ people in 75+ countries. It hires through Greenhouse and asks for no fee.

---

## Points to cover in your own words (do NOT paste AI text)

- **Your best personal project:** the Shopping Assistant. What problem it solves, the architecture, one hard bug you fixed (the 70% → 100% price-limit fix is a good story), and how you measured it.
- **Python experience:** FastAPI services, SQLAlchemy and Alembic, pytest (104 tests), GitHub Actions CI, Docker Compose; PyTorch and Hugging Face for the LoRA paper.
- **AI agents and LLMs beyond chat (Edge AI question):** tool calling, memory design, hybrid retrieval, guardrails, and evaluation you built yourself.
- **Linux and containers:** only what you've really done.
- **Leadership during your education:** designing and running 50 Compiler Theory lab sessions for 600+ students; publishing two papers as a student.
- **Academic results:** your real high-school results with the national scoring (Thanaweya Amma percentage) and your university grade with its scale. [FILL IN]
- **Years since graduating:** about 2 (since 06/2024).

---

## Interview prep

- **Written interview:** after the first screen, Canonical sends a long written questionnaire (education, motivation, projects). Take your time and write it yourself.
- **Python depth:** generators, decorators, context managers, typing, packaging (pyproject), testing with pytest fixtures and mocks.
- **Linux basics:** processes and signals, systemd, file permissions, package management (apt, snaps), networking basics (ports, DNS), and Docker vs LXD.
- **Edge AI:** what inference packaging means (shipping a model plus its runtime as a snap), quantisation for small devices, ONNX Runtime and OpenVINO at a high level.
- **Kubernetes basics (AI/ML role):** pods, deployments, services, and what Kubeflow or MLflow do in an MLOps stack.
- **Walk through the Shopping Assistant:** the LangGraph agent, hybrid retrieval (PostgreSQL full-text + pgvector, Reciprocal Rank Fusion, reranking), memory as typed facts in PostgreSQL plus a Postgres checkpointer, and the evaluation (12 tasks × 3 runs; 7 → 12 of 12 with 29% fewer paid rerank calls).
- **Numbers to know:** 72% / 56% / 41% top-10 recall (hybrid / keyword / vector, 127 labelled queries), 23% → 43% right-product-first with reranking, HNSW 35 ms → 3.1 ms, 104 tests.
- **Remote work:** how you work asynchronously: written updates, clear PRs, overlap hours with their time zone (Egypt is GMT+2).

---

## Original post

### Software Engineer – Edge AI (EMEA)

> Software Engineer - Edge AI — Canonical — Home based - EMEA — https://job-boards.greenhouse.io/canonical/jobs/2614095
>
> This is an exciting opportunity for a software engineer passionate about open source software, Linux, edge computing, and AI. Come build a rewarding, meaningful career working with the best and brightest people in technology at Canonical, a growing international software company.
>
> Your role will be to help us provide easy-to-deploy, secure, and customizable edge AI solutions, specifically focusing on Inference Snaps. You will work on designing and implementing silicon-optimized application packages for AI/ML inference, targeting devices from embedded systems to powerful gateways. Linux will be at the core of your everyday challenges.
>
> In our team we value collaboration, peer reviews, good integration/unit testing, and writing maintainable code. General knowledge and experience with Linux as a developer platform is required. 
>
> What you’ll do
>
> Collaborate proactively with a distributed team
>
> Develop and maintain open-source AI/ML inference application packages
>
> Debug issues and produce high-quality code to fix them
>
> Review code produced by upstream and/or other engineers at Canonical
>
> Discuss ideas and collaborate on finding good solutions
>
> Experiment with Ubuntu Core and showcase industry-grade Edge AI solutions
>
> Secure deployment of AI inference platforms on Linux
>
> Build optimized AI solutions for local inferencing on Ubuntu
>
> Work from home with global travel 2 to 4 weeks for internal and external events
>
> Who you are
>
> Proven track record of at least 3 years of professional software development using Go or C++.
>
> Experience working on and developing applications for Linux
>
> You have interest and experience with a few of the following:
>
> Containers (docker, kubernetes)
>
> Snap, debian, or RPM packaging
>
> Bash scripting
>
> CI/CD (GitHub Actions, GitLab CI, etc)
>
> Local AI/ML inference frameworks
>
> Hardware accelerators: GPU, NPU
>
> You value soft skills, communication and advocacy, and are passionate, enterprising, thoughtful, and self-motivated
>
> You have a Bachelor’s or equivalent in Computer Science, STEM or similar degree
>
> Canonical is a growing international software company that works with the open-source community to deliver Ubuntu, the world’s best free software platform. Our services help businesses worldwide reduce costs, improve efficiency and enhance security with Ubuntu.
>
> We are proud to foster a workplace free from discrimination. Diversity of experience, perspectives, and background create a better work environment and better products. Whatever your identity, we will give your application fair consideration.
>
> #LI-remote

### Python and Kubernetes Software Engineer – Data, Workflows, AI/ML & Analytics (worldwide)

> Python and Kubernetes Software Engineer - Data, Workflows, AI/ML & Analytics — Canonical — Home based - Worldwide — https://job-boards.greenhouse.io/canonical/jobs/5703396
>
> Canonical is a leading provider of open source software and operating systems to the global enterprise and technology markets. Our platform, Ubuntu, is very widely used in breakthrough enterprise initiatives such as public cloud, data science, AI, engineering innovation and IoT. Our customers include the world's leading public cloud and silicon providers, and industry leaders in many sectors. The company is a pioneer of global distributed collaboration, with 1000+ colleagues in 70+ countries and very few roles based in offices. Teams meet two to four times yearly in person, in interesting locations around the world, to align on strategy and execution.
>
> The company is founder led, profitable and growing. We are hiring Python and Kubernetes Specialist Engineers focused on Data, Workflows, AI/ML and Analytics Solutions to join our teams building open source solutions for public cloud and private infrastructure.
>
> As a software engineer on the team, you'll collaborate on end-to-end data analytics and MLOps solutions composed of popular, open-source, machine learning tools, such as Kubeflow, MLFlow, DVC, and Feast. You may also work on ETL, data governance and visualization tools like Apache SuperSet, dbt, workflow orchestration tools such as Airflow and Temporal, or data warehouse solutions such as Apache Trino, or ClickHouse. These solutions may be run on servers or on the cloud, on machines or on Kubernetes, on developer desktops, or as web services.
>
> We serve the needs of individuals and community members as much as the needs of our Global 2000 and Fortune 500 customers; we make our primary work available free of charge and our Pro subscriptions are also available to individuals for personal use at no cost. Our goal is to enable more people to enjoy the benefits of open source, regardless of their circumstances.
>
> Location: This initiative spans many teams that are home-based and in multiple time zones. We believe in distributed collaboration but we also try to ensure that colleagues have company during their work hours! Successful candidates will join a team where most members and your manager are broadly in the same time zone so that you have the benefits of constant collaboration and discussion.
>
> What your day will look like
>
> Develop your understanding of the entire Linux stack, from kernel, networking, and storage, to the application layer
>
> Design, build and maintain solutions that will be deployed on public and private clouds and local workstations
>
> Master distributed systems concepts such as observability, identity, tracing
>
> Work with both Kubernetes and machine-oriented open source applications
>
> Collaborate proactively with a distributed team of engineers, designers and product managers
>
> Debug issues and interact in public with upstream and Ubuntu communities
>
> Generate and discuss ideas, and collaborate on finding good solutions
>
> What we are looking for in you
>
> Professional or academic software delivery using Python
>
> Exceptional academic track record from both high school and university
>
> Undergraduate degree in a technical subject or a compelling narrative about your alternative chosen path
>
> Confidence to respectfully speak up, exchange feedback, and share ideas without hesitation
>
> Track record of going above-and-beyond expectations to achieve outstanding results
>
> Passion for technology evidenced by personal projects and initiatives
>
> The work ethic and confidence to shine alongside motivated colleagues
>
> Professional written and spoken English with excellent presentation skills
>
> Experience with Linux (Debian or Ubuntu preferred) 
>
> Excellent interpersonal skills, curiosity, flexibility, and accountability
>
> Appreciative of diversity, polite and effective in a multi-cultural, multi-national organisation
>
> Thoughtfulness and self-motivation 
>
> Result-oriented, with a personal drive to meet commitments 
>
> Ability to travel twice a year, for company events up to two weeks long
>
> Additional skills that would be nice to have
>
> The following skills may be helpful to you in the role, but we don't expect everyone to bring all of them.
>
> Proven track record of building highly automated machine learning solutions, data pipelines, or orchestrating workflows for the cloud.
>
> Hands-on experience with machine learning libraries, or tools.
>
> Experience with container technologies (Docker, LXD, Kubernetes, etc.)
>
> Experience with public clouds (AWS, Azure, Google Cloud)
>
> Working knowledge of cloud computing
>
> Passionate about software quality and testing
>
> Experience working on an open source project
>
> What we offer colleagues
>
> We consider geographical location, experience, and performance in shaping compensation worldwide. We revisit compensation annually (and more often for graduates and associates) to ensure we recognise outstanding performance. In addition to base pay, we offer a performance-driven annual bonus or commission. We provide all team members with additional benefits, which reflect our values and ideals. We balance our programs to meet local needs and ensure fairness globally.
>
> Distributed work environment with twice-yearly team sprints in person
>
> Personal learning and development budget of USD 2,000 per year
>
> Annual compensation review
>
> Recognition rewards
>
> Annual holiday leave
>
> Maternity and paternity leave
>
> Employee Assistance Programme
>
> Opportunity to travel to new locations to meet colleagues
>
> Priority Pass, and travel upgrades for long haul company events
>
> About Canonical
>
> Canonical is a pioneering tech firm at the forefront of the global move to open source. As the company that publishes Ubuntu, one of the most important open source projects and the platform for AI, IoT and the cloud, we are changing the world of software. We recruit on a global basis and set a very high standard for people joining the company. We expect excellence - in order to succeed, we need to be the best at what we do. Most colleagues at Canonical have worked from home since its inception in 2004.​ Working here is a step into the future, and will challenge you to think differently, work smarter, learn new skills, and raise your game.
>
> Canonical is an equal opportunity employer
>
> We are proud to foster a workplace free from discrimination. Diversity of experience, perspectives, and background create a better work environment and better products. Whatever your identity, we will give your application fair consideration.
>
> #LI-remote

### Junior Ubuntu Software Engineer (worldwide)

> Junior Ubuntu Software Engineer — Canonical — Home based - Worldwide — https://job-boards.greenhouse.io/canonical/jobs/6707669
>
> Canonical is a leading provider of open source software and operating systems to the global enterprise and technology markets. Our platform, Ubuntu, is very widely used in breakthrough enterprise initiatives such as public cloud, data science, AI, engineering innovation and IoT. Our customers include the world's leading public cloud and silicon providers, and industry leaders in many sectors. The company is a pioneer of global distributed collaboration, with 1200+ colleagues in 75+ countries and very few office based roles. Teams meet two to four times yearly in person, in interesting locations around the world, to align on strategy and execution.
>
> The company is founder led, profitable and growing.
>
> We are hiring junior engineers to work across the breadth of our Ubuntu Engineering organisation -  engineers who care deeply for quality, performance and resilience in software, engineers who are just as comfortable designing and engineering new software as they are packaging, integrating, testing and shipping the incredible catalog of open source software provided by the Ubuntu repositories.
>
> Our engineers integrate the freshest open source software, provide robust upgrade paths and engineer the future of Ubuntu. Ubuntu is not just the world’s most deployed open source operating system, it's a platform that enables innovation for millions of users across the globe. Our community represents the full breadth of the developer experience; from students, hobbyists and freelancers to high performance engineering and creative teams in corporate and academic environments.
>
> The four key teams that ship Ubuntu are 
>
> Foundations: maintaining foundational software: architectures, package managers, compilers, toolchains, bootloaders, filesystems and core utilities
>
> Server: leading the design, evolution and future of our Ubuntu Server distribution
>
> Desktop: driving Ubuntu Desktop, our future immutable desktop: Ubuntu Core Desktop, WSL, gaming technology, and a suite of modern applications for the desktop crafted with Flutter
>
> Debcrafters: a new team responsible for the forward movement, maintenance and overall health of the Ubuntu archive: one of the most abundant repositories of open source software available today
>
> Bring your existing expertise and learn new skills by working on one of the most prolific pieces of open source software. As an engineer working on Ubuntu you could work on any or all of the following categories:
>
> Development: design, build and ship new foundational systems software and applications in Rust, Go, Flutter, and Python
>
> Architecture: engineer the integration of open source from boot firmware to cloud applications deployment
>
> Packaging: a combination of Debian and Snap packaging to ship software in the distribution
>
> Automation: build and maintain the machinery responsible for building, testing and shipping Ubuntu
>
> Distro Engineering: the maintenance and evolution of a Linux distribution and its repositories
>
> If you have skills in those areas, or you have other skills you believe could contribute to Ubuntu, and you're keen to get started building your career in open source, then this is the role for you. Our junior career path caters for both new graduates and early careers engineers. 
>
> At Canonical, you will have the opportunity to engage with and contribute to the broader open source community. We're looking for individuals who can help build a thriving community and contribute with enthusiasm and precision to a broad range of technologies.
>
> Location: We have remote roles open in every time zone.
>
> The role entails
>
> Based on the first round of interviews, we identify specific teams where you might be an excellent fit and conduct second-round interviews with those teams. Our engineers are:
>
> Designing, building and shipping software in Rust, Go, Python and C/C++
>
> Packaging, integrating, testing and uploading open source software to the Ubuntu repositories
>
> Debugging issues, then designing and delivering robust solutions
>
> Authoring and improving technical and community documentation
>
> Contributing to upstream and neighboring open source projects
>
> Collaborating as part of a globally distributed team
>
> Continuously learning and progressing their technical and professional skills
>
> What we are looking for in you
>
> An exceptional academic track record from both high school and university
>
> Undergraduate degree in Computer Science or STEM, or a compelling narrative about your alternative path
>
> Drive and a track record of going above and beyond expectations
>
> A passion for open source software
>
> Experience with Rust, Go, Python, Flutter or C/C++
>
> Professional written and spoken English
>
> Excellent communication and interpersonal skills
>
> Ability to travel twice a year, for company events up to two weeks each
>
> Nice-to-have skills
>
> Familiarity with Linux distributions
>
> Familiarity with system debugging tools and techniques
>
> Familiarity with automation tooling and CI/CD systems
>
> Experience contributing to open source projects
>
> What we offer you
>
> We consider geographical location, experience, and performance in shaping compensation worldwide. We revisit compensation annually (and more often for graduates and associates) to ensure we recognize outstanding performance. In addition to base pay, we offer a performance-driven annual bonus. We provide all team members with additional benefits, which reflect our values and ideals. We balance our programs to meet local needs and ensure fairness globally.
>
> Distributed work environment with twice-yearly team sprints in person
>
> Personal learning and development budget of USD 2,000 per year
>
> Annual compensation review
>
> Recognition rewards
>
> Annual holiday leave
>
> Maternity and paternity leave
>
> Team Member Assistance Program & Wellness Platform
>
> Opportunity to travel to new locations to meet colleagues
>
> Priority Pass, and travel upgrades for long haul company events
>
> About Canonical
>
> Canonical is a pioneering tech firm at the forefront of the global move to open source. As the company that publishes Ubuntu, one of the most important open source projects and the platform for AI, IoT and the cloud, we are changing the world on a daily basis. We recruit on a global basis and set a very high standard for people joining the company. We expect excellence - in order to succeed, we need to be the best at what we do. Canonical has been a remote-first company since its inception in 2004.​ Working here is a step into the future, and will challenge you to think differently, work smarter, learn new skills, and raise your game.
>
> Canonical is an equal opportunity employer
>
> We are proud to foster a workplace free from discrimination. Diversity of experience, perspectives, and background create a better work environment and better products. Whatever your identity, we will give your application fair consideration.
