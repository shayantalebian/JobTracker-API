from app.models.company import Company
from app.models.job_application import JobApplication

# This allows easy importing elsewhere and ensures Alembic registers the tables.
__all__ = ["Company", "JobApplication"]
