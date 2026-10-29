"""Raya Holding — Aman Nexus Program, Data Science round (Oracle Recruiting job 133, posted 2026-10-27). 0-2 years.
Round focus: Data Science and Agentic AI. Asks: ETL/ELT pipelines over structured and unstructured data, PySpark
feature pipelines, data lineage and ERD models, warehouse models, automated data-validation checks, predictive ML
models judged against baseline and monetary KPIs, batch scoring pipelines, executive proposals. Requirements: CS/IT/
DS degree; Python (pandas, NumPy) and SQL; statistics, probability, ML fundamentals; turning a business question into
a data problem; graduation project / Kaggle / internship / GitHub a plus; PySpark or visualisation a plus.
Data-science framing from the IBM variant; the Shopping Assistant leads with its data pipeline and validation.
Not claimed: PySpark, data warehousing, ERD/lineage work, BI dashboards, business KPIs.
"""
import copy

from variants.ibm import *  # noqa: F401,F403
from variants.ibm import PROJECTS as _IBM_PROJECTS

FILE_STEM = "Ahmed_Dorra_CV_Raya_DataScience"

TITLE = "Data Scientist — Python, SQL, Machine Learning & Agentic AI"

SUMMARY = (
    "Computer Science graduate (2024) who turns questions into measured answers with Python and SQL. Built an "
    "ingestion pipeline for 12,730 products (pandas loaders for five file formats, row-level validation with "
    "Pydantic, PostgreSQL), then measured every model change against a baseline on labelled data with 95% "
    "confidence intervals: hybrid retrieval reached 72% top-10 recall vs 56% keyword and 41% vector, and reranking "
    "lifted right-product-first from 23% to 43%. Builds agentic AI with LangGraph, trains models with PyTorch, "
    "scikit-learn and XGBoost, and publishes the work on GitHub. Teaching assistant (Linear Algebra, Calculus) who "
    "explains results clearly to non-technical audiences."
)

PROJECTS = copy.deepcopy(_IBM_PROJECTS)
PROJECTS[0]["tagline"] = "Data pipeline, measured retrieval models and an agentic assistant"
PROJECTS[0]["bullets"][0] = (
    "Built the data pipeline for a 12,730-product catalogue: pandas loaders for five file formats, row-level "
    "validation with Pydantic, PostgreSQL storage with embeddings in pgvector, then hybrid retrieval with reranking "
    "and a LangGraph agent with long-term customer memory."
)
