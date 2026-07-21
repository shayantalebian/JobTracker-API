from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.api.dependencies import get_db
from app.schemas.job_application import JobApplicationCreate, JobApplicationResponse, JobApplicationUpdate
from app.repositories.job_application import job_application_repo
from app.repositories.company import company_repo
from app.core.exceptions import NotFoundException

# Define the router with a clean prefix and tag for Swagger UI
router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post("/", response_model=JobApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_job_application(
    job_in: JobApplicationCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new Job Application.
    Validates that the provided company_id actually exists before creation.
    """
    # 1. Verify that the company exists using the repository
    company = company_repo.get(db, company_id=job_in.company_id)
    if not company:
        raise NotFoundException(
            resource_name="Company",
            resource_id=job_in.company_id
        )

    # 2. Delegate creation to the repository pattern
    return job_application_repo.create(db=db, job_in=job_in)


@router.get("/", response_model=List[JobApplicationResponse])
def read_jobs(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=100,
                       description="Max records to return (max 100)"),
    status_filter: str | None = Query(
        None, alias="status", description="Filter by application status (e.g., 'APPLIED', 'REJECTED')"),
    sort_by: str = Query(
        "id", description="Field to sort by (e.g., 'id', 'applied_date', 'status')"),
    sort_desc: bool = Query(False, description="Sort in descending order")
):
    """
    Retrieve a list of job applications with optional status filter, sorting, and pagination.
    """
    return job_application_repo.get_all(
        db=db,
        skip=skip,
        limit=limit,
        status=status_filter,
        sort_by=sort_by,
        sort_desc=sort_desc
    )


@router.get("/{job_id}", response_model=JobApplicationResponse)
def read_job(job_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific job application by its ID.
    """
    # Note: Passed job_id positionally or mapped correctly to avoid kwarg errors
    job = job_application_repo.get(db, job_id)
    if not job:
        raise NotFoundException(
            resource_name="Job Application", resource_id=job_id)
    return job


@router.patch("/{job_id}", response_model=JobApplicationResponse)
def update_job(
    job_id: int,
    job_in: JobApplicationUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a job application's details. 
    Only updates fields provided in the request body.
    """
    job = job_application_repo.get(db, job_id)
    if not job:
        raise NotFoundException(
            resource_name="Job Application", resource_id=job_id)

    # Optional Validation: If the user is trying to change the company, ensure the new company exists!
    if job_in.company_id is not None:
        company = company_repo.get(db, company_id=job_in.company_id)
        if not company:
            raise NotFoundException(
                resource_name="Company", resource_id=job_in.company_id)

    # Delegate the update operation to the repository
    return job_application_repo.update(db=db, db_job=job, job_in=job_in)


@router.delete("/{job_id}", response_model=JobApplicationResponse)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    """
    Delete a job application.
    """
    job = job_application_repo.get(db, job_id)
    if not job:
        raise NotFoundException(
            resource_name="Job Application", resource_id=job_id)

    # Delegate the deletion of the fetched object to the repository
    return job_application_repo.delete(db=db, db_job=job)
