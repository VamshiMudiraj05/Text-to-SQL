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
