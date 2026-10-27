"""Foodics — AI Engineer (agentic AI infrastructure). Riyadh, hybrid; open to all levels ("early career: prior agentic
experience is not required; mentorship provided"). Workable 9BDF0B39E6, posted 2026-09-29 (Workable rate-limited
our check on 2026-10-27, so open status unconfirmed). Saudi restaurant-management and payments platform.
Asks: deep software engineering in one language; CS foundations; backend infrastructure (REST/gRPC, databases,
caching, queues); Git, automated tests, CI/CD; LLM mechanics (context windows, tokenization, function calling,
non-determinism, hallucinations); full-lifecycle projects (side projects count); methodical debugging; writing.
Work: agent orchestration, session and state management, tool integrations and MCP servers, OpenTelemetry tracing,
eval suites and regression tests, root-cause analysis, guardrails, output-validation schemas, human-in-the-loop.
Eval-driven development. No gRPC, queues, caching, MCP, OpenTelemetry, AWS or Kubernetes claimed.
"""
from variants.deeplight import *  # noqa: F401,F403

FILE_STEM = "Ahmed_Dorra_CV_Foodics"

TITLE = "AI Engineer — Agent Infrastructure, Tool Calling & Eval-Driven Development"

SUMMARY = (
    "Software engineer building LLM agents as tested backend services in Python: LangGraph orchestration with tool "
    "calling, conversation state in a Postgres checkpointer, Pydantic output schemas, bounded retries, guardrails, "
    "FastAPI on PostgreSQL, 104 automated tests and GitHub Actions CI. Works eval-first: each prompt or retrieval "
    "change was measured on a task suite before it was kept. On a 12,730-product assistant, a revised prompt took the agent from 7 to 12 of 12 "
    "tasks with 29% fewer paid rerank calls, root-causing off-target results led to moving price limits into search "
    "(70% to 100% on target), and an HNSW index cut median search latency from 35 ms to 3.1 ms."
)

COVER_LETTER = None
