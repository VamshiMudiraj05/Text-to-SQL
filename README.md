# ClarifySQL: Text-to-SQL with an Ambiguity Clarification Engine

> **Autonomous 30-Day Project** | Built daily by [Autonomous Project Agent](https://github.com/VamshiMudiraj05/Github-Automation)

ClarifySQL is a production-minded application that converts natural-language questions into accurate SQL queries, detects conversational and schema ambiguity, prompts users with targeted clarification options, validates generated SQL for read-only safety, and executes queries against PostgreSQL.

---

## 🏗️ Architecture & Planning Deliverables

- [30-Day Master Roadmap](ROADMAP.md)
- [Daily Progress & Execution Tracker](PROGRESS.md)
- [System Architecture](docs/architecture.md)
- [Requirements & Acceptance Criteria](docs/requirements.md)
- [Synthetic Database Domain Schema](docs/domain_schema.md)

---

## 🛠️ Technology Stack
- **Backend**: Python 3.12+, FastAPI, Pydantic, SQLAlchemy/Asyncpg
- **Database**: PostgreSQL (Orders, Customers, Products, Reviews domain)
- **Frontend**: React, Tailwind CSS
- **Testing**: Pytest, Testcontainers/Mock DB
- **LLM**: Gemini / OpenAI via configurable provider abstraction

---

## 📅 Development Progress
See [PROGRESS.md](PROGRESS.md) for milestone completion history, streaks, and upcoming features.
