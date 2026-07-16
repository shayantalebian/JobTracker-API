# 🏗️ System Design & Architecture (Phase 1)

## High-Level Architecture

JobTrackr API follows a standard 3-tier architecture containerized for local development:

1.  **Presentation/Routing Layer:** FastAPI endpoints routing HTTP requests and handling OpenAPI (Swagger) documentation.
2.  **Business Logic Layer:** Python services validating data (Pydantic) and interacting with the ORM.
3.  **Data Access Layer:** SQLAlchemy ORM communicating with the PostgreSQL database.

## Database Schema (ERD Overview)

### Entity: `Company`

- `id` (PK, UUID)
- `name` (String, Unique)
- `website` (String, Optional)
- `industry` (String)
- `created_at` (Timestamp)

### Entity: `Application`

- `id` (PK, UUID)
- `company_id` (FK -> Company.id)
- `job_title` (String)
- `status` (Enum: APPLIED, INTERVIEWING, REJECTED, OFFER)
- `applied_date` (Date)
- `notes` (Text)

**Relationship:** One `Company` can have Many `Applications`.

## Containerization

- **App Service:** FastAPI running on Uvicorn.
- **DB Service:** PostgreSQL 15+ persistent volume.
