# 🗺️ 30-Day Engineering Roadmap: ClarifySQL: Text-to-SQL with a Clarification Engine

> **Project Objective:** A production-minded, portfolio-quality application that converts natural-language questions into accurate SQL queries, detects ambiguity, asks users targeted clarification questions, validates generated SQL, executes safe read-only queries, and presents results in an interactive interface.
> **Start Date:** 2026-10-24 | **Schedule:** Daily at 18:00 (Asia/Kolkata)
> **Overall Progress:** 1/30 Days Completed (3.3%)

## 📊 Progress Overview

| Phase | Days | Focus Area | Status |
| :--- | :--- | :--- | :--- |
| **Phase 1: Foundation** | Days 1–5 | Architecture, Models, Persistence, CI Setup | In Progress |
| **Phase 2: Core Functionality** | Days 6–12 | End-to-End Ingestion, Aggregation, Processing | Planned |
| **Phase 3: Advanced Features** | Days 13–19 | Alerts, Query Engine, Anomaly Detection, Exporters | Planned |
| **Phase 4: Reliability & Polish** | Days 20–25 | Benchmarks, Concurrency, Hardening, 90%+ Test Coverage | Planned |
| **Phase 5: Release & Deployment** | Days 26–30 | Packaging, Docker, Production Verification, Final Docs | Planned |

---

## 🗓️ Detailed 30-Day Milestone Breakdown

### Phase 1: Foundation

#### Day 01: Requirements, Acceptance Criteria, Architecture, and Synthetic Database Domain — ✅ Completed
- **Description:** Define ClarifySQL system requirements, architecture specifications, and synthetic e-commerce database schema contracts.
- **Complexity:** `Low` | **Dependencies:** `None`
- **Acceptance Criteria:**
  - [x] Specify schema entity-relationship model (customers, orders, products, order_items)
  - [x] Document clarification engine state machine and ambiguity trigger thresholds
  - [x] Define read-only safety guardrails, timeouts, and AST validation specifications
- **Key Deliverables:**
  - `docs/architecture.md`
  - `docs/requirements.md`
  - `docs/domain_schema.md`

#### Day 02: Project Scaffolding, Python/FastAPI Environment, PostgreSQL Config, and React Layout — ⚪ Planned
- **Description:** Initialize backend project layout with FastAPI and Pydantic v2, PostgreSQL connection driver, and React frontend scaffolding.
- **Complexity:** `Low` | **Dependencies:** `task-day-01`
- **Acceptance Criteria:**
  - [ ] FastAPI application skeleton with structured config management
  - [ ] Pydantic v2 settings loading database credentials from environment
  - [ ] React frontend scaffolding initialized with Tailwind CSS configuration
- **Key Deliverables:**
  - `src/core/config.py`
  - `src/main.py`
  - `frontend/package.json`
  - `frontend/src/App.tsx`

#### Day 03: Synthetic Database Domain: Customers, Orders, Products, and Realistic Seed Data — ⚪ Planned
- **Description:** Create relational schemas for customers, products, orders, and order_items with realistic sample data for text-to-sql evaluation.
- **Complexity:** `Medium` | **Dependencies:** `task-day-02`
- **Acceptance Criteria:**
  - [ ] SQLAlchemy models defined with primary keys, foreign keys, and indexes
  - [ ] Synthetic seed generator populates realistic customers, products, orders, and line items
  - [ ] Unit test verifies relational integrity and seed data consistency
- **Key Deliverables:**
  - `src/db/models.py`
  - `src/db/seed_data.py`
  - `tests/test_seed_data.py`

#### Day 04: Database Connection Management, Session Pooling, and Schema Introspection — ⚪ Planned
- **Description:** Implement robust database session management and automatic schema reflection extracting table names, columns, and data types.
- **Complexity:** `Medium` | **Dependencies:** `task-day-03`
- **Acceptance Criteria:**
  - [ ] Thread-safe engine pool with read-only execution session factory
  - [ ] Schema introspector extracts tables, columns, foreign keys, and sample distinct values
  - [ ] Tests verify schema reflection accurately matches database catalog
- **Key Deliverables:**
  - `src/db/connection.py`
  - `src/db/introspector.py`
  - `tests/test_introspector.py`

#### Day 05: Backend Configuration Validation, Health Endpoints, and Baseline Test Suite — ⚪ Planned
- **Description:** Add comprehensive health check endpoints, configuration sanity checks, and automated baseline pytest suite.
- **Complexity:** `Low` | **Dependencies:** `task-day-04`
- **Acceptance Criteria:**
  - [ ] GET /health endpoint reporting database ping latency and schema readiness
  - [ ] Configuration validator checking model API keys and connection parameters
  - [ ] Pytest suite executes and passes 100% on Phase 1 modules
- **Key Deliverables:**
  - `src/api/health.py`
  - `tests/test_health.py`
  - `tests/test_config.py`

### Phase 2: Core Functionality

#### Day 06: LLM Provider Interface and Structured Response Schemas — ⚪ Planned
- **Description:** Implement pluggable LLM provider abstraction supporting Gemini and OpenAI with structured JSON response schemas.
- **Complexity:** `Medium` | **Dependencies:** `task-day-05`
- **Acceptance Criteria:**
  - [ ] Pydantic models for SQLGenerationResponse, AmbiguityCheck, and ClarificationPrompt
  - [ ] Gemini and OpenAI provider implementations with exponential backoff
  - [ ] Unit tests verifying JSON response parsing and schema conformance
- **Key Deliverables:**
  - `src/llm/provider.py`
  - `src/llm/schemas.py`
  - `tests/test_llm_provider.py`

#### Day 07: Schema-Aware SQL Generation Engine — ⚪ Planned
- **Description:** Build prompt synthesis pipeline injecting introspected database schema, foreign keys, and constraints into LLM context.
- **Complexity:** `Medium` | **Dependencies:** `task-day-06`
- **Acceptance Criteria:**
  - [ ] Dynamic prompt builder formatting schema catalog into compact model context
  - [ ] Generates standard SQL queries adhering to database dialect without hallucinations
  - [ ] Unit tests verifying correct table joins on multi-table queries
- **Key Deliverables:**
  - `src/engine/sql_generator.py`
  - `tests/test_sql_generator.py`

#### Day 08: SQL Parsing, Read-Only Query Validation, and Query Limits — ⚪ Planned
- **Description:** Implement strict AST-based SQL validator enforcing read-only SELECT/CTE queries and blocking DDL/DML.
- **Complexity:** `High` | **Dependencies:** `task-day-07`
- **Acceptance Criteria:**
  - [ ] SQL AST parser rejects INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE
  - [ ] Blocks stacked queries, dangerous functions, and unauthorized system tables
  - [ ] Enforces statement limit (LIMIT 100) and query complexity checks
- **Key Deliverables:**
  - `src/security/sql_guard.py`
  - `tests/test_sql_guard.py`

#### Day 09: Safe Query Execution Engine and Tabular Result Serialization — ⚪ Planned
- **Description:** Execute validated queries under statement timeouts, serialize results to JSON tables, and compute column metadata.
- **Complexity:** `Medium` | **Dependencies:** `task-day-08`
- **Acceptance Criteria:**
  - [ ] Read-only database transaction execution with strict timeout (5 seconds)
  - [ ] Serializes rows and columns into JSON table structure with row count and duration
  - [ ] Error interceptor converting database exceptions into readable user messages
- **Key Deliverables:**
  - `src/engine/query_executor.py`
  - `tests/test_query_executor.py`

#### Day 10: Test Clear Questions, Invalid Queries, and Unsupported Requests — ⚪ Planned
- **Description:** Build rigorous test suite covering unambiguous questions, syntactic errors, and out-of-domain requests.
- **Complexity:** `Medium` | **Dependencies:** `task-day-09`
- **Acceptance Criteria:**
  - [ ] End-to-end tests for simple and aggregated clear questions (e.g. 'total sales in 2024')
  - [ ] Tests verifying rejection of malicious queries like 'DROP TABLE customers'
  - [ ] Negative tests handling unsupported queries with graceful error responses
- **Key Deliverables:**
  - `tests/test_clear_questions.py`
  - `tests/test_security_rejection.py`

#### Day 11: Ambiguity Detection and Clarification-State Models — ⚪ Planned
- **Description:** Implement ambiguity analyzer detecting underspecified metrics, missing time ranges, or multiple ranking criteria.
- **Complexity:** `High` | **Dependencies:** `task-day-10`
- **Acceptance Criteria:**
  - [ ] Ambiguity classifier determining if question requires user clarification
  - [ ] Identifies specific ambiguity type: ranking criteria, date range, entity filter
  - [ ] Tests verify clear questions are not unnecessarily flagged as ambiguous
- **Key Deliverables:**
  - `src/engine/ambiguity_detector.py`
  - `tests/test_ambiguity_detector.py`

#### Day 12: Targeted Clarification Question Generator with Selectable Options — ⚪ Planned
- **Description:** Generate one concise, targeted clarification question with 2-4 distinct selectable options when ambiguity is detected.
- **Complexity:** `Medium` | **Dependencies:** `task-day-11`
- **Acceptance Criteria:**
  - [ ] Clarification generator outputs clear question and structured choice options
  - [ ] Example: 'Show top customers' -> choices: Total Spending, Order Count, Recent Activity
  - [ ] Tests confirm concise wording and mutually exclusive options
- **Key Deliverables:**
  - `src/engine/clarification_generator.py`
  - `tests/test_clarification_generator.py`

### Phase 3: Clarification & State

#### Day 13: Conversation State Manager Preserving Clarification Turns — ⚪ Planned
- **Description:** Build stateful conversation store preserving original user question, detected ambiguities, and user answers.
- **Complexity:** `Medium` | **Dependencies:** `task-day-12`
- **Acceptance Criteria:**
  - [ ] Session state store caching multi-turn dialogue history with TTL cleanup
  - [ ] ConversationTurn model linking question, clarification options, and selection
  - [ ] Integration tests verifying conversation state persistence across turns
- **Key Deliverables:**
  - `src/engine/conversation.py`
  - `tests/test_conversation.py`

#### Day 14: Clarification-Informed SQL Regeneration — ⚪ Planned
- **Description:** Incorporate user clarification choice into the SQL generator prompt to produce accurate, tailored queries.
- **Complexity:** `Medium` | **Dependencies:** `task-day-13`
- **Acceptance Criteria:**
  - [ ] Prompt pipeline augments schema and original question with selected clarification
  - [ ] Generates refined SQL directly matching the clarified user intent
  - [ ] Tests verify generated SQL reflects the clarified metric (e.g. SUM(total_amount))
- **Key Deliverables:**
  - `src/engine/sql_regenerator.py`
  - `tests/test_sql_regenerator.py`

#### Day 15: Test Suite for Ambiguous, Underspecified, and Clear Questions — ⚪ Planned
- **Description:** Comprehensive automated test matrix asserting correct routing between direct execution and clarification flow.
- **Complexity:** `Medium` | **Dependencies:** `task-day-14`
- **Acceptance Criteria:**
  - [ ] Tests asserting clarification triggers on underspecified ranking requests
  - [ ] Tests asserting direct execution on fully specified date-filtered queries
  - [ ] Verification that default assumptions are explicitly documented when no clarification is needed
- **Key Deliverables:**
  - `tests/test_clarification_workflow.py`

#### Day 16: React Chat Interface and Question Submission Workflow — ⚪ Planned
- **Description:** Build modern, responsive React chat interface with Tailwind CSS for natural language question input.
- **Complexity:** `Medium` | **Dependencies:** `task-day-15`
- **Acceptance Criteria:**
  - [ ] Clean chat message timeline supporting user questions and assistant responses
  - [ ] Input box with auto-focus, send button, and keyboard shortcut (Enter)
  - [ ] Component tests asserting input handling and loading state transitions
- **Key Deliverables:**
  - `frontend/src/components/ChatTimeline.tsx`
  - `frontend/src/components/QuestionInput.tsx`

#### Day 17: Interactive Clarification Option Controls and Turn History — ⚪ Planned
- **Description:** Render clickable clarification option buttons within the chat stream allowing 1-click option selection.
- **Complexity:** `Medium` | **Dependencies:** `task-day-16`
- **Acceptance Criteria:**
  - [ ] ClarificationCard component rendering option pills/buttons for user selection
  - [ ] Disables choices once answered and updates conversation timeline seamlessly
  - [ ] Frontend interaction tests verifying choice submission callback
- **Key Deliverables:**
  - `frontend/src/components/ClarificationCard.tsx`
  - `frontend/src/components/HistorySidebar.tsx`

#### Day 18: SQL Preview Modal, Plain-English Explanations, and Tabular Results — ⚪ Planned
- **Description:** Display formatted SQL preview with syntax highlighting, plain-English explanation, and interactive data table.
- **Complexity:** `Medium` | **Dependencies:** `task-day-17`
- **Acceptance Criteria:**
  - [ ] SqlPreview component with copy-to-clipboard and syntax highlighting
  - [ ] QueryExplanation card detailing why the query was constructed that way
  - [ ] ResultTable component with pagination, sortable columns, and row counts
- **Key Deliverables:**
  - `frontend/src/components/SqlPreview.tsx`
  - `frontend/src/components/ResultTable.tsx`

#### Day 19: Responsive UI Polish, Skeleton Loading States, and Error Banners — ⚪ Planned
- **Description:** Implement polished dark-mode styling, loading skeletons during SQL execution, and actionable error toasts.
- **Complexity:** `Low` | **Dependencies:** `task-day-18`
- **Acceptance Criteria:**
  - [ ] Skeleton placeholders for SQL generation and data table loading states
  - [ ] Error banner explaining syntax or security policy rejections clearly
  - [ ] Responsive mobile-friendly drawer and desktop side-by-side view
- **Key Deliverables:**
  - `frontend/src/components/ErrorBanner.tsx`
  - `frontend/src/components/LoadingSkeleton.tsx`

### Phase 4: Evaluation, Hardening & Integration

#### Day 20: Full Frontend-Backend API Integration and User Journey Test — ⚪ Planned
- **Description:** Connect React frontend with FastAPI backend endpoints over HTTP and test complete clarification journey.
- **Complexity:** `High` | **Dependencies:** `task-day-19`
- **Acceptance Criteria:**
  - [ ] POST /api/v1/query endpoint handling initial question, ambiguity, and clarification
  - [ ] End-to-end integration test asserting full question -> clarify -> execute flow
  - [ ] CORS and API client error handling verified
- **Key Deliverables:**
  - `src/api/routes.py`
  - `tests/test_api_integration.py`

#### Day 21: Representative Text-to-SQL Benchmark Dataset — ⚪ Planned
- **Description:** Curate benchmark suite of 50 diverse e-commerce questions across simple, multi-join, ambiguous, and edge cases.
- **Complexity:** `Medium` | **Dependencies:** `task-day-20`
- **Acceptance Criteria:**
  - [ ] Benchmark dataset JSON containing questions, expected tables, and golden SQL
  - [ ] Categories covering simple lookups, aggregations, multi-table joins, and ambiguous prompts
  - [ ] Automated dataset loader and test runner
- **Key Deliverables:**
  - `benchmarks/dataset.json`
  - `benchmarks/evaluator.py`

#### Day 22: Execution Accuracy and Clarification Effectiveness Measurement — ⚪ Planned
- **Description:** Run automated evaluation computing exact-match accuracy, execution accuracy, and ambiguity recall.
- **Complexity:** `High` | **Dependencies:** `task-day-21`
- **Acceptance Criteria:**
  - [ ] Evaluation script calculates execution accuracy (% of queries producing identical results)
  - [ ] Measures clarification precision: does the engine ask questions only when needed?
  - [ ] Generates benchmark evaluation report in Markdown
- **Key Deliverables:**
  - `benchmarks/run_eval.py`
  - `reports/evaluation_results.md`

#### Day 23: Prompt Engineering Improvements and Failure Analysis — ⚪ Planned
- **Description:** Analyze failed benchmark questions to refine schema prompts, few-shot examples, and ambiguity triggers.
- **Complexity:** `Medium` | **Dependencies:** `task-day-22`
- **Acceptance Criteria:**
  - [ ] Incorporate few-shot representative join examples into generator prompt
  - [ ] Fine-tune ambiguity detection thresholds to minimize false positive clarifications
  - [ ] Re-run benchmarks demonstrating measurable accuracy improvement
- **Key Deliverables:**
  - `src/engine/prompts.py`
  - `tests/test_prompt_improvements.py`

#### Day 24: Database Security Audit, Parameterization, and Vulnerability Scan — ⚪ Planned
- **Description:** Audit SQL security rules, enforce parameterized execution for literals, and run dependency audit.
- **Complexity:** `Medium` | **Dependencies:** `task-day-23`
- **Acceptance Criteria:**
  - [ ] Verify parameterization of user-supplied filter constants to prevent SQL injection
  - [ ] Audit query timeout enforcement preventing Denial-of-Service on heavy scans
  - [ ] Run security audit verifying zero high/critical vulnerabilities
- **Key Deliverables:**
  - `src/security/sanitizer.py`
  - `tests/test_security_audit.py`

#### Day 25: Full Regression Testing and Defect Resolution — ⚪ Planned
- **Description:** Execute full regression test suite across backend API, database engine, guardrails, and frontend mocks.
- **Complexity:** `Medium` | **Dependencies:** `task-day-24`
- **Acceptance Criteria:**
  - [ ] 100% test pass rate across all backend unit and integration test suites
  - [ ] Resolve all outstanding edge-case defects identified during evaluation
  - [ ] Produce quality and reliability sign-off checklist
- **Key Deliverables:**
  - `tests/test_full_regression.py`
  - `reports/quality_audit.md`

### Phase 5: Release

#### Day 26: Production Deployment Configuration and Environment Setup — ⚪ Planned
- **Description:** Configure production environment profiles, database connection pooling, and Gunicorn/Uvicorn workers.
- **Complexity:** `Low` | **Dependencies:** `task-day-25`
- **Acceptance Criteria:**
  - [ ] Production settings profile with strict environment variable validation
  - [ ] Production ASGI server configuration with optimized worker processes
  - [ ] Configuration tests validating production parameters
- **Key Deliverables:**
  - `src/core/prod_config.py`
  - `tests/test_prod_config.py`

#### Day 27: Containerization: Multi-Stage Dockerfile & Docker Compose Pipeline — ⚪ Planned
- **Description:** Create multi-stage Dockerfile packaging FastAPI backend, React build, and PostgreSQL database service.
- **Complexity:** `Medium` | **Dependencies:** `task-day-26`
- **Acceptance Criteria:**
  - [ ] Multi-stage Dockerfile producing minimal, hardened production container
  - [ ] docker-compose.yml orchestrating ClarifySQL API, PostgreSQL, and React frontend
  - [ ] Automated container startup smoke test verifying all services healthy
- **Key Deliverables:**
  - `Dockerfile`
  - `docker-compose.yml`
  - `.dockerignore`

#### Day 28: End-to-End Production Smoke Testing in Sandbox — ⚪ Planned
- **Description:** Deploy containerized ClarifySQL stack in isolated sandbox and execute comprehensive smoke test suite.
- **Complexity:** `Medium` | **Dependencies:** `task-day-27`
- **Acceptance Criteria:**
  - [ ] Automated smoke test exercises natural language question, clarification, SQL execution, and table output
  - [ ] Verifies read-only permission isolation on production database account
  - [ ] Sandbox health verification passes without warnings
- **Key Deliverables:**
  - `scripts/smoke_test.py`
  - `tests/test_smoke.py`

#### Day 29: Comprehensive Developer Guide, Architecture Specs, and Interactive Demo Guide — ⚪ Planned
- **Description:** Author complete technical documentation, architecture diagrams, API reference, and demo walk-throughs.
- **Complexity:** `Low` | **Dependencies:** `task-day-28`
- **Acceptance Criteria:**
  - [ ] Comprehensive README.md with system architecture diagram and feature highlights
  - [ ] API documentation covering all REST endpoints with curl examples
  - [ ] Interactive demo guide with sample ambiguous and clear questions to try
- **Key Deliverables:**
  - `README.md`
  - `docs/api_reference.md`
  - `docs/demo_guide.md`

#### Day 30: Final Acceptance Audit, Release v1.0.0 Tagging, and 30-Day Retrospective — ⚪ Planned
- **Description:** Conduct final acceptance audit against all requirements, tag v1.0.0 release, and document project achievements.
- **Complexity:** `Low` | **Dependencies:** `task-day-29`
- **Acceptance Criteria:**
  - [ ] All 30 daily acceptance criteria verified 100% complete
  - [ ] Changelog and release notes published for v1.0.0
  - [ ] Publish 30-day retrospective report documenting architecture, evaluation, and future roadmap
- **Key Deliverables:**
  - `CHANGELOG.md`
  - `reports/30_day_retrospective.md`
