# 🏗️ System Design & Architecture (Phase 1)

## High-Level Architecture

### Directory Structure & Architecture Mapping

Our folder structure strictly adheres to the 3-Tier Architecture for maximum modularity and scalability:

- **Presentation Layer (`app/api/`)**: Contains FastAPI routers, endpoints, and dependency injections (`dependencies.py`). It strictly handles HTTP requests and responses.
- **Business Logic Layer (`app/services/` & `app/schemas/`)**: Contains the core logic of the application. `services/` process the rules, while `schemas/` (Pydantic) validate the input/output data.
- **Data Access Layer (`app/repositories/` & `app/models/`)**: `repositories/` abstract all SQLAlchemy database queries, ensuring the services never interact with the database directly. `models/` define the database tables.
- **Core Configuration (`app/core/`)**: Houses environmental settings, logging, and database engine initialization (`database.py`).
- **Utilities (`app/utils/`)**: Standalone helper functions independent of domain logic.

JobTrackr API follows a standard 3-tier architecture containerized for local development:

1. **Presentation/Routing Layer:** FastAPI endpoints routing HTTP requests and handling OpenAPI (Swagger) documentation.
2. **Business Logic Layer:** Python services validating data (Pydantic) and interacting with the ORM.
3. **Data Access Layer:** SQLAlchemy ORM communicating with the PostgreSQL database.

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
