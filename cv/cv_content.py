"""Single source of truth for the CV. Both the PDF and the DOCX are generated from this."""

NAME = "Ahmed Dorra"
TITLE = "AI Engineer — LLM Systems (RAG · Agents · Evaluation)"
CONTACT = [
    "Giza, Egypt · Open to relocation and remote",
    "+20 100 614 8440",
    "newahmed1672022@gmail.com",
]
LINKS = [
    ("linkedin.com/in/ahmed-mostafa-dorra", "https://www.linkedin.com/in/ahmed-mostafa-dorra"),
    ("github.com/AhmedMostafa167", "https://github.com/AhmedMostafa167"),
    ("ahmedmostafa167.github.io", "https://ahmedmostafa167.github.io/"),
]

SUMMARY = (
    "AI engineer building LLM applications end to end: hybrid-search RAG, tool-using agents with long-term "
    "memory, and the evaluation, guardrails and monitoring that show whether each change works. On a "
    "12,730-product shopping assistant, raised right-product-ranked-first from 23% to 43% and agent task "
    "success from 7 to 12 of 12 tasks. Published researcher (LoRA fine-tuning of Stable Diffusion; quantum "
    "machine learning) and Computer Science teaching assistant."
)

SKILLS = [
    ("LLM & RAG", "LangGraph, LangChain, retrieval-augmented generation (RAG), hybrid search (PostgreSQL "
     "full-text + pgvector, Reciprocal Rank Fusion), cross-encoder reranking, agents and tool calling, "
     "conversational memory, prompt engineering, structured output (Pydantic), Chroma, Groq, Cohere"),
    ("Evaluation & LLMOps", "Langfuse (tracing, prompt management, experiments), MLflow, DVC, RAGAS, "
     "LLM-as-a-judge, code-graded agent evaluation, guardrails"),
    ("Backend & Deployment", "Python, SQL, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, Docker Compose, "
     "GitHub Actions (CI), pytest, Prometheus, Grafana, Nginx, Gradio, Hugging Face Spaces"),
    ("Machine Learning", "PyTorch, Hugging Face Transformers, Diffusers, LoRA, scikit-learn, XGBoost, "
     "pandas, NumPy, spaCy, NLTK"),
]

PROJECTS = [
    {
        "name": "Shopping Assistant",
        "tagline": "Conversational product search with long-term memory",
        "links": [("GitHub", "https://github.com/AhmedMostafa167/Shopping-Assistant")],
        "stack": "Python · FastAPI · LangGraph · PostgreSQL · pgvector · Cohere · Groq · Langfuse · MLflow · "
                 "Prometheus · Grafana · Docker",
        "bullets": [
            "Built a LangGraph agent that searches a 12,730-product catalogue with hybrid retrieval (PostgreSQL "
            "full-text + pgvector HNSW, Reciprocal Rank Fusion, Cohere reranking) and remembers each customer's "
            "lasting preferences across conversations.",
            "Measured retrieval stage by stage on 127 labelled queries with 95% confidence intervals: hybrid "
            "top-10 recall 72% vs 56% keyword and 41% vector; reranking lifted right-product-first from 23% to "
            "43% (40-query subset); an HNSW index cut median vector search from 35 ms to 3.1 ms.",
            "Designed a code-graded agent evaluation (12 tasks × 3 runs, logged to Langfuse and MLflow): prompt "
            "v2 passed 12 of 12 tasks vs 7, with 29% fewer paid rerank calls; moving price limits inside search "
            "lifted on-target results from 70% to 100%.",
            "Added input and memory-write guardrails (0 of 21 legitimate facts refused), Langfuse tracing and "
            "prompt versioning, Prometheus/Grafana monitoring, 104 automated tests and GitHub Actions CI.",
        ],
    },
    {
        "name": "Research Assistant",
        "tagline": "Agentic RAG over arXiv and the web",
        "links": [
            ("Live demo", "https://huggingface.co/spaces/Ahmed167/research_assistant"),
            ("GitHub", "https://github.com/AhmedMostafa167/Projects/tree/main/01-LLM-RAG/research-assistant"),
        ],
        "stack": "Python · LangGraph · LangChain · Chroma · BM25 · FastAPI · Gradio · Docker · Hugging Face Spaces",
        "bullets": [
            "Designed a self-correcting LangGraph workflow: query rewriting, hybrid retrieval, relevance grading, "
            "cited generation and a reflection step with a bounded retry, using structured outputs for each decision.",
            "Combined dense (Chroma) and keyword (BM25) retrieval with cross-encoder reranking; a provider factory "
            "switches between Groq, Hugging Face, Anthropic and OpenAI with one setting; served through FastAPI "
            "and Gradio and deployed on Hugging Face Spaces.",
        ],
    },
    {
        "name": "VISIONEER",
        "tagline": "Text-to-floor-plan generation with AR visualisation (2024)",
        "links": [("Model", "https://huggingface.co/Ahmed167/visioneer-v2"),
                  ("Paper", "https://mgv.sggw.edu.pl/article/view/10294")],
        "stack": "Stable Diffusion v1.5 · Hugging Face Diffusers · LoRA · Android · ARCore",
        "bullets": [
            "Fine-tuned Stable Diffusion v1.5 with LoRA (Hugging Face Diffusers) on ~12k captioned floor plans to "
            "generate furnished 2D layouts from text prompts; a teammate trained the companion schematic model, "
            "and both were served to an Android AR app. Published in Machine Graphics & Vision (2025).",
        ],
    },
]

EXPERIENCE = [
    {
        "role": "Teaching Assistant, Computer Science",
        "org": "Culture and Science City · Giza",
        "dates": "03/2026 – Present",
        "bullets": [
            "Designed and led 50 Compiler Theory lab sessions over 8 weeks for 600+ students (~70 per session), "
            "covering regular expressions, finite automata and lexical analysis.",
            "Co-taught neural-network and CNN sessions on backpropagation, gradient descent and loss functions; "
            "led tutorials in Linear Algebra, Calculus and Information Retrieval.",
        ],
    },
    {
        "role": "Military Service (mandatory)",
        "org": "Egypt",
        "dates": "01/2025 – 01/2026",
        "bullets": [],
    },
    {
        "role": "Quantum Research Intern",
        "org": "QUAE (QWorld UAE chapter) · Remote",
        "dates": "12/2023 – 03/2024",
        "bullets": [
            "Built a quantum machine-learning pipeline for EEG classification: a Quantum Variational Autoencoder "
            "for self-supervised denoising, followed by LDA for cognitive-task classification in brain–computer "
            "interfaces.",
            "Evaluated generalisation and computational-complexity trade-offs on noisy neurological time series; "
            "results published at the Neurogenomics 2024 Conference.",
        ],
    },
]

PUBLICATIONS = [
    {
        "title": "Fine-tuning Stable Diffusion for Generating 2D Floor Plans Using Prompt Templates",
        "venue": "Machine Graphics & Vision, 34(3), 77–95",
        "date": "09/2025",
        "link": ("mgv.sggw.edu.pl/article/view/10294", "https://mgv.sggw.edu.pl/article/view/10294"),
    },
    {
        "title": "Quantum Denoising in the Realm of Brain-Computer Interfaces: A Preliminary Study",
        "venue": "Neurogenomics 2024 Conference",
        "date": "07/2024",
        "link": ("hal.science/hal-04501908", "https://hal.science/hal-04501908"),
    },
]
ORCID = ("orcid.org/0009-0001-4161-6026", "https://orcid.org/0009-0001-4161-6026")

EDUCATION = [
    {
        "degree": "Bachelor of Science in Computer Science",
        "org": "Culture and Science City · 6th of October, Giza",
        "dates": "10/2020 – 06/2024",
        "detail": "Relevant coursework: Machine Learning & AI, Software Engineering, Data Structures & Algorithms.",
    },
    {
        "degree": "Diploma in Quantum Computing",
        "org": "QWorld · Remote",
        "dates": "10/2023 – 07/2024",
        "detail": "Quantum algorithms, quantum machine learning and quantum information; QBronze, QSilver and "
                  "QNickel certifications.",
    },
]

TRAINING = [
    "MLOps Practitioner Course — MLOps MENA Community (2026)",
    "Mini-RAG: production RAG systems — Abu Bakr Soliman (2026)",
    "Hugging Face LLM Course (in progress)",
    "Generative AI with Large Language Models — DeepLearning.AI",
    "Natural Language Processing Specialization — DeepLearning.AI",
    "Deep Learning Specialization — DeepLearning.AI",
    "Machine Learning Specialization — DeepLearning.AI & Stanford",
    "Applied Text Mining in Python — University of Michigan",
    "Vector Databases (Pinecone) — 365 Data Science",
]

LANGUAGES = "Arabic (native) · English (professional working proficiency)"
