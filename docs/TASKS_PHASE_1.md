# 📝 Phase 1: Micro-Task Breakdown (The Vibe Coding Path)

This document tracks the step-by-step implementation of **Phase 1 (Core Infrastructure)** for the JobTrackr API. Every task is intentionally small, focused, and designed for deep understanding rather than rushing through implementation.

---

## Stage 1 — Project Foundation

- [✅] **Task 1.0:** Initialize advanced directory skeleton (api, core, models, repositories, schemas, services, utils, tests)
- [✅] **Task 1.1:** Create the project structure (`app/`, `docs/`, `alembic/`, etc.).
- [✅] **Task 1.2:** Initialize Git repository and create `.gitignore`.
- [✅] **Task 1.3:** Create `README.md`, `ROADMAP.md`, `PHASES.md`, and `SYSTEM_DESIGN.md`.
- [✅] **Task 1.4:** Initialize a Python 3.12 virtual environment using `uv`.
- [✅] **Task 1.5:** Install FastAPI, SQLAlchemy, Alembic, Pydantic Settings, Uvicorn and required dependencies.
- [✅] **Task 1.6:** Create a minimal FastAPI application (`app/main.py`) with a health check endpoint (`GET /`).

---

## Stage 2 — Docker Environment

- [✅] **Task 2.1:** Create a `.env` file containing PostgreSQL credentials and application settings.
- [✅] **Task 2.2:** Create `docker-compose.yml`.
- [✅] **Task 2.3:** Add a PostgreSQL service with persistent Docker volumes.
- [✅] **Task 2.4:** Configure exposed ports (`5433`).
- [✅] **Task 2.5:** Verify PostgreSQL is running correctly using `docker compose up -d`.
- [✅] **Task 2.6:** Connect to PostgreSQL using DBeaver or PgAdmin.
- [✅] **Task 2.7:** Create a `.env.example` file for repository users.

---

## Stage 3 — Configuration

- [✅] **Task 3.1:** Create `app/core/config.py` using Pydantic Settings.
- [✅] **Task 3.2:** Load all environment variables securely.
- [✅] **Task 3.3:** Create `app/core/database.py`.
- [✅] **Task 3.4:** Configure SQLAlchemy Engine.
- [✅] **Task 3.5:** Configure SessionLocal.
- [✅] **Task 3.6:** Create Declarative Base.

---

## Stage 4 — Alembic

- [✅] **Task 4.1:** Initialize Alembic.
- [✅] **Task 4.2:** Configure Alembic to use `.env`.
- [✅] **Task 4.3:** Connect Alembic to SQLAlchemy metadata.
- [✅] **Task 4.4:** Verify migrations work correctly.

---

## Stage 5 — Database Models

## Company

- [✅] **Task 5.1:** Create Company model.
- [✅] **Task 5.2:** Add fields:
  - id
  - name
  - website
  - industry
  - created_at

## Job Application

- [✅] **Task 5.3:** Create JobApplication model.
- [✅] **Task 5.4:** Add fields:
  - id
  - title
  - status
  - applied_date
  - notes
  - company_id

## Relationships

- [✅] **Task 5.5:** Configure One-to-Many relationship.
- [✅] **Task 5.6:** Create `models/__init__.py`.
- [✅] **Task 5.7:** Generate the first migration.
- [✅] **Task 5.8:** Apply migration.
- [✅] **Task 5.9:** Verify tables inside PostgreSQL.

---

## Stage 6 — Data Validation

## Company Schemas

- [✅] **Task 6.1:** CompanyCreate
- [✅] **Task 6.2:** CompanyUpdate
- [✅] **Task 6.3:** CompanyResponse

## Job Schemas

- [✅] **Task 6.4:** JobCreate
- [✅] **Task 6.5:** JobUpdate
- [✅] **Task 6.6:** JobResponse

## Validation

- [✅] **Task 6.7:** Validate URLs.
- [✅] **Task 6.8:** Validate field lengths.
- [✅] **Task 6.9:** Use Enum for application status.

---

## Stage 7 — Repository Layer

## Company Repository

- [✅] **Task 7.1:** Create Company Repository.
- [✅] **Task 7.2:** Create CRUD operations.

## Job Repository

- [✅] **Task 7.3:** Create Job Repository.
- [✅] **Task 7.4:** Create CRUD operations.

---

## Stage 8 — API Layer

- [ ] **Task 8.1:** Create database dependency (`get_db()`).
- [ ] **Task 8.2:** Create Company router.
- [ ] **Task 8.3:** Implement Company CRUD endpoints.
- [ ] **Task 8.4:** Create Job router.
- [ ] **Task 8.5:** Implement Job CRUD endpoints.
- [ ] **Task 8.6:** Register all routers.
- [ ] **Task 8.7:** Verify all endpoints in Swagger UI.

---

## Stage 9 — API Improvements

- [ ] **Task 9.1:** Add pagination.
- [ ] **Task 9.2:** Add filtering.
- [ ] **Task 9.3:** Add sorting.
- [ ] **Task 9.4:** Return proper HTTP status codes.
- [ ] **Task 9.5:** Improve Swagger documentation.
- [ ] **Task 9.6:** Add endpoint descriptions and examples.

---

## Stage 10 — Error Handling

- [ ] **Task 10.1:** Handle 404 errors.
- [ ] **Task 10.2:** Handle duplicate companies.
- [ ] **Task 10.3:** Create custom exceptions.
- [ ] **Task 10.4:** Add global exception handlers.

---

## Stage 11 — Final Cleanup

- [ ] **Task 11.1:** Add application logging.
- [ ] **Task 11.2:** Verify Docker startup from scratch.
- [ ] **Task 11.3:** Review folder structure.
- [ ] **Task 11.4:** Remove dead code.
- [ ] **Task 11.5:** Final API testing using Swagger.
- [ ] **Task 11.6:** Commit Phase 1 completion.

## Stage 12 — Project Quality

- [ ] Create service layer.
- [ ] Add health check endpoint.
- [ ] Add database constraints.
- [ ] Add timestamps to all models.
- [ ] Add common BaseModel mixin.
- [ ] Verify project works from a clean clone.
- [ ] Update README screenshots.
- [ ] Tag Release v0.1.0
- [ ] pytest
- [ ] httpx
- [ ] Test database
- [ ] Coverage

## Stage 13 — CI/CD

- [ ] GitHub Actions
- [ ] Run Ruff
- [ ] Run Tests
- [ ] Build Docker
