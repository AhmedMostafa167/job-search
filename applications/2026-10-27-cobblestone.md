# Commercial Graduate Scheme, Junior Data Scientist — Cobblestone Energy (Dubai; visa sponsored)

- **Posting:** Greenhouse https://job-boards.greenhouse.io/cobblestoneenergy/jobs/7772325003 (also LinkedIn job 4472322180), **open** on 27 Oct 2026.
  - Dubai, permanent. USD 65,000 a year plus bonus, tax-free.
  - **Visa sponsorship and relocation are provided.**
- **Apply:** on the Greenhouse link. It's a long form only you can fill in:
  - your university transcript, university grade, and high-school and O-level maths grades;
  - Country: Egypt. City: Giza. Willing to relocate: Yes. Highest education: Bachelor's degree;
  - University: "Other", then type "Egypt – Culture and Science City"; status: Graduated;
  - Years of experience: "0-1 years" or "1-2 years" (your TA work);
  - CV: `Ahmed_Dorra_CV_Cobblestone.pdf`;
  - Draft answers to the essay questions are below.
- **Verdict: apply. It's a paid graduate scheme with visa sponsorship.**
  - They want Python, pandas, NumPy and SQL, plus LLMs **integrated programmatically into data pipelines** and custom agents. That's your work.
  - **Gaps (not claimed):** R, Matplotlib/Seaborn, forecasting, and trading experience.
  - The process has psychometric and logical-reasoning tests, a case study, and three remote interviews, so practise numerical-reasoning tests.
- **Company check: no red flags.** Cobblestone is a real energy-trading firm (founded in London in 2018; Cobblestone Energy FZCO, DMCC registration 179969, Jumeirah Lake Towers, Dubai). It uses Greenhouse and asks for no fee.

---

## Draft answers for the form (edit them in your own voice)

**Why Dubai (textarea):**
Dubai puts me at the centre of the region's fastest-growing tech and trading scene, a few hours from home in Egypt, and its international teams match how I want to grow: working with people from many backgrounds on measurable problems. A graduate programme with structured training is the right step after my Computer Science degree, research publications and teaching work.

**Track record of excellence:**
Two peer-reviewed publications as a student: fine-tuning Stable Diffusion with LoRA for floor-plan generation (Machine Graphics & Vision, 2025) and quantum denoising for brain-computer interfaces (Neurogenomics 2024). A Diploma in Quantum Computing from QWorld (QBronze, QSilver and QNickel). As a teaching assistant I designed and led 50 Compiler Theory lab sessions for 600+ students in 8 weeks. Outside class I built a 12,730-product AI shopping assistant with 104 automated tests. [ADD your university grade or GPA and any awards.]

**When you showed initiative:**
On my shopping assistant, about 30% of results still broke the customer's price or rating limits, even though the agent was told to respect them. Nobody asked me to fix it; I measured it on a fixed task set, traced the cause to filtering happening after search, and moved the limits inside the search call. Matching results rose from 70% to 100% (57/81 to 48/48), and paid searches fell by 15%.

**Complex data problem + AI tool + validation (max 150 words):**
I needed to know which retrieval method found the right product among 12,730 items. I built a LangGraph agent in Python that calls a hybrid search tool (PostgreSQL full-text plus pgvector), with every output validated by a Pydantic schema so malformed answers are rejected and retried. To check accuracy instead of trusting the model, I labelled 127 queries with the correct products and measured recall with 95% confidence intervals: hybrid 72%, keyword 56%, vector 41%. To catch hallucination, a code-graded check confirms that every price the agent quotes appears in the retrieved data; it passed in 25 of 25 applicable runs. Each change was kept only if the numbers improved, and I logged every result before and after.
(about 125 words)

**Extreme-weather trade (max 120 words):** this one needs your own research on a recent European event. Suggested shape: a cold snap or a heatwave → (i) e.g. long front-month Dutch TTF gas, or German power for the affected week; (ii) a back-of-envelope link: an X°C drop in temperature raises heating demand by roughly Y GW, which moves the price by about Z; (iii) the risk indicator: weather-forecast revisions, gas storage levels or wind-generation forecasts. Look up real numbers before writing.

**Why Cobblestone's data science team (max 120 words):**
Cobblestone uses data science directly in trading decisions, so models are judged by outcomes, which is how I like to work: every change I make is measured before I keep it. Your team's use of LLMs and agents to speed up data cleaning and analysis matches what I build, and I want to learn time-series forecasting for power and gas markets. Long term, I want to become a data scientist who can take an idea from data to a production tool that traders trust, and the Commercial Development Program is a structured way to get there.

**Notice period / start date:** [FILL IN]

---

## Interview prep

- **Psychometric and numerical tests:** practise SHL- or Cappfinity-style numerical and logical reasoning (free tests online), timed.
- **Statistics:** confidence intervals (how you computed yours), hypothesis tests, correlation vs causation, overfitting in back-tests.
- **Time series:** train/test split by time, lag features, seasonality, and why random shuffling leaks the future.
- **Energy basics:** what TTF and German baseload power are, why wind generation pushes prices down, and spark spreads.
- **Python and SQL live coding:** pandas groupby, merge and resample, and SQL window functions.

---

## Original post

### Greenhouse posting

> Commercial Graduate Scheme, Junior Data Scientist - Dubai, UAE — Cobblestone Energy — Dubai, UAE — updated 2026-08-17 — https://job-boards.greenhouse.io/cobblestoneenergy/jobs/7772325003
>
> Employment Type:
> Full-time &amp; Permanent.
>
> Job Location:
> Dubai, UAE (We provide visa sponsorship &amp; relocation assistance).
>
> Salary:
>
> USD 65,000&nbsp;per annum
>  + performance based bonus - 0% tax environment.
>
> &nbsp;
>
> Employee Share Scheme
> : Opportunity to join Cobblestone Employee Share Scheme.
>
> Annual Leave:
>  30 Calendar Days.
>
> Public Holidays:
>  As declared by UAE Government annually (8 to 14 days).
>
> Probation Period:
>  3 to 6 Months (as per UAE Labour Law).
>
> Health Insurance:
>  Comprehensive Private Health Insurance (IPD, OPD &amp; Dental).
>
> Residency Visa Sponsorship:
>  Provided by the Company.
>
> Relocation Support:
>  Available for candidates relocating to Dubai.
>
> End of Service Gratuity:
>  As per UAE Labour Law.
>
> About Cobblestone Energy
>
> Cobblestone Energy is an energy trading company specialising in the European Gas, Power and Emissions markets. Established in 2018, we combine deep analytics, advanced data science and agile technology to drive profitable trading decisions. Our flat organisational structure empowers every team member with autonomy and ownership. Our diverse global team of extraordinary talent is united by a relentless pursuit of excellence.
>
> Cobblestone Values
>
> Excellence in Hiring &amp; Teamwork
>
> Lifelong Learning Through Continuous Reflection
>
> Independent Thinking Through a Meritocracy of Ideas
>
> Winning
>
> What we offer in this role
>
> A full-time position on our Commercial team
>
> Committed and remarkably talented colleagues.
>
> Highly competitive compensation dependent on performance
>
> An exciting, challenging and fulfilling career.
>
> Investment in your development to ensure that you always remain the best in business.
>
> Equity participation for strong contributors, ensuring our interests are all aligned long term.
>
> Key Responsibilities:
>
> Data Preparation: Collect, clean, and structure large datasets from market, fundamental, and operational sources
>
> Forecasting &amp; Modeling: Develop and validate predictive models (e.g. wind generation, demand) to support trading strategies
>
> Strategy Research: Prototype, back-test, and refine data-driven trading ideas; collaborate with analytics and development teams to productionise solutions
>
> Infrastructure: Build and maintain data pipelines, dashboards, and automated tooling to streamline workflows
>
> AI-Accelerated Workflows: Utilise LLMs and agentic frameworks to accelerate exploratory data analysis (EDA), automate data cleaning pipelines, and generate synthetic data for model robustification.
>
> Stay current with the rapidly evolving AI landscape (e.g., RAG, Agents, Multimodal models) and proactively propose new ways to apply these to trading data.
>
> Collaboration: Partner with traders, risk managers, and software engineers to integrate insights into real-time decision-making
>
> Documentation: Maintain clear records of methodologies, data definitions, and model specifications
>
> Culture: Champion our values through proactive communication and teamwork
>
> Your background:
>
> Bachelor's or master’s degree in Computer Science, Mathematics, Statistics, or a related field
>
> Strong proficiency in programming languages such as Python and R
>
> Experience with data analysis and manipulation tools such as Pandas, NumPy, and SQL
>
> Knowledge of data visualization tools such as Matplotlib and Seaborn
>
> Experience programmatically integrating LLMs (via APIs, LangChain, or Python scripts) into data pipelines rather than just using chat interfaces.
>
> Proven ability to build custom "Agents" or automated workflows that interpret unstructured data or reason through multi-step problems.
>
> Pro-active and flexible work mentality
>
> Interest in data-driven trading
>
> Fluency in English, both written and spoken.
>
> Preferred Background:
>
> Proven track record of excellence, academic or professional, in quantitative or analytical roles
>
> Experience working with time-series data, machine learning libraries, or cloud-based data platforms
>
> Demonstrated ability to innovate and drive end-to-end solutions
>
> The Hiring Process
>
> Application Review
>
> Online Assessments:
>  Psychometric and logical reasoning tests
>
> Case Study:
>  Research-oriented project to showcase your analytical approach
>
> Remote Interviews:
>  Three rounds with members of our Analytics and Trading teams
>
> Offer &amp; Onboarding:
>  Join our Commercial Development Program, then step directly into your role as Junior Data Scientist
>
> &nbsp;
>
> &nbsp;
>
> Learn more about Cobblestone Energy careers:
>
> https://cobblestoneenergy.com/careers/
>
> Why work with us:
>
> https://cobblestoneenergy.com/why-work-with-us/
>
> Recruitment process:
>
> https://cobblestoneenergy.com/careers/vacancies/#process
>
> &nbsp;
