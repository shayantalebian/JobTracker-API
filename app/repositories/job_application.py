from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.models.job_application import JobApplication
from app.schemas.job_application import JobApplicationCreate, JobApplicationUpdate


class JobApplicationRepository:
    """
    Repository handling database interaction logic for Job Applications.
    Fulfills Tasks 7.3 & 7.4 of TASKS_PHASE_1.md.
    """

    def get(self, db: Session, job_id: int) -> JobApplication | None:
        """Retrieve a single job application by its primary key ID."""
        return db.query(JobApplication).filter(JobApplication.id == job_id).first()

    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 100,
        status: str | None = None,
        sort_by: str = "id",
        sort_desc: bool = False
    ) -> list[JobApplication]:
        """Retrieve job applications with pagination, filtering, and sorting."""
        query = db.query(JobApplication)

        # 1. Filtering - Exact match for status (e.g., 'APPLIED', 'REJECTED')
        if status:
            query = query.filter(JobApplication.status == status)

        # 2. Sorting - Dynamic column sorting
        sort_column = getattr(JobApplication, sort_by,
                              JobApplication.id)  # Fallback to ID
        if sort_desc:
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        # 3. Pagination
        return query.offset(skip).limit(limit).all()

    def get_by_company_id(self, db: Session, company_id: int, skip: int = 0, limit: int = 100) -> list[JobApplication]:
        """Retrieve all job applications associated with a specific company ID."""
        return (
            db.query(JobApplication)
            .filter(JobApplication.company_id == company_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, db: Session, job_in: JobApplicationCreate) -> JobApplication:
        """Create and persist a new job application record."""
        # Convert Pydantic schema to dict and unpack into the SQLAlchemy model
        db_job = JobApplication(**job_in.model_dump())
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job

    def update(
        self, db: Session, db_job: JobApplication, job_in: JobApplicationUpdate
    ) -> JobApplication:
        """Update an existing job application record with partial data (PATCH)."""
        # Exclude unset fields to prevent overwriting existing values with None
        update_data = job_in.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_job, field, value)

        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job

    def delete(self, db: Session, db_job: JobApplication) -> JobApplication:
        """Delete a job application record from the database."""
        db.delete(db_job)
        db.commit()
        return db_job


# Singleton instance for clean import across API dependencies
job_application_repo = JobApplicationRepository()
