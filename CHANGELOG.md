# Changelog — ClarifySQL: Text-to-SQL with a Clarification Engine

All notable daily development milestones and changes are documented here.

## Daily Milestone Releases

### Day 03 — Synthetic Database Domain: Customers, Orders, Products, and Realistic Seed Data (2026-10-25)

- **Commit:** `14cbd0e7`
- **Summary:** Create relational schemas for customers, products, orders, and order_items with realistic sample data for text-to-sql evaluation.

### Day 04 — Database Connection Management, Session Pooling, and Schema Introspection (2026-10-25)

- **Commit:** `1f9360db`
- **Summary:** Implement robust database session management and automatic schema reflection extracting table names, columns, and data types.

### Day 05 — Backend Configuration Validation, Health Endpoints, and Baseline Test Suite (2026-10-26)

- **Commit:** `0f299c67`
- **Summary:** Add comprehensive health check endpoints, configuration sanity checks, and automated baseline pytest suite.

### Day 06 — LLM Provider Interface and Structured Response Schemas (2026-10-27)

- **Commit:** `21d7f944`
- **Summary:** Implement pluggable LLM provider abstraction supporting Gemini and OpenAI with structured JSON response schemas.

### Day 07 — Schema-Aware SQL Generation Engine (2026-10-28)

- **Commit:** `4ffe2db4`
- **Summary:** Build prompt synthesis pipeline injecting introspected database schema, foreign keys, and constraints into LLM context.

### Day 08 — SQL Parsing, Read-Only Query Validation, and Query Limits (2026-10-29)

- **Commit:** `183c4c97`
- **Summary:** Implement strict AST-based SQL validator enforcing read-only SELECT/CTE queries and blocking DDL/DML.

### Day 09 — Safe Query Execution Engine and Tabular Result Serialization (2026-10-30)

- **Commit:** `fc94e8c1`
- **Summary:** Execute validated queries under statement timeouts, serialize results to JSON tables, and compute column metadata.

### Day 10 — Test Clear Questions, Invalid Queries, and Unsupported Requests (2026-10-31)

- **Commit:** `648cb808`
- **Summary:** Build rigorous test suite covering unambiguous questions, syntactic errors, and out-of-domain requests.

### Day 11 — Ambiguity Detection and Clarification-State Models (2026-11-01)

- **Commit:** `757b863f`
- **Summary:** Implement ambiguity analyzer detecting underspecified metrics, missing time ranges, or multiple ranking criteria.

### Day 12 — Targeted Clarification Question Generator with Selectable Options (2026-11-02)

- **Commit:** `84cd5ab9`
- **Summary:** Generate one concise, targeted clarification question with 2-4 distinct selectable options when ambiguity is detected.

### Day 13 — Conversation State Manager Preserving Clarification Turns (2026-11-03)

- **Commit:** `5d3f0a87`
- **Summary:** Build stateful conversation store preserving original user question, detected ambiguities, and user answers.

### Day 14 — Clarification-Informed SQL Regeneration (2026-11-04)

- **Commit:** `9ebc1085`
- **Summary:** Incorporate user clarification choice into the SQL generator prompt to produce accurate, tailored queries.

### Day 15 — Test Suite for Ambiguous, Underspecified, and Clear Questions (2026-11-05)

- **Commit:** `92b56edc`
- **Summary:** Comprehensive automated test matrix asserting correct routing between direct execution and clarification flow.
