# 📋 Development Phases

## Phase 1: The Core (Active)

- [ ] Initialize repository and documentation (README, SDLC, System Design).
- [ ] Set up Docker & `docker-compose.yml` for PostgreSQL.
- [ ] Design database schemas (Models) using SQLAlchemy.
- [ ] Configure Alembic for database migrations.
- [ ] Create Pydantic schemas for data validation.
- [ ] Implement CRUD REST API endpoints for `Companies`.
- [ ] Implement CRUD REST API endpoints for `Applications` (One-to-Many).

## Phase 2: Security & Testing (Next)

- [ ] Implement User model and database relationships.
- [ ] Add JWT (JSON Web Token) authentication.
- [ ] Secure endpoints with role-based access control.
- [ ] Write unit and integration tests using `pytest`.
- [ ] Develop a minimal HTML/CSS/JS frontend for testing outside Swagger UI.

## Phase 3: Advanced Backend & Scaling (Future)

- [ ] Implement Redis for caching frequent queries.
- [ ] Set up Celery & RabbitMQ/Redis for asynchronous background tasks.
- [ ] Establish GitHub Actions for CI/CD (Linting, Testing, Docker build).
- [ ] Refactor UI to React (Optional/Extension).
