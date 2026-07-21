from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.api.dependencies import get_db
from app.schemas.job_application import JobApplicationCreate, JobApplicationResponse, JobApplicationUpdate
from app.models.company import Company
from app.repositories.job_application import job_application_repo

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
    # 1. Verify that the company exists first
    company = db.query(Company).filter(Company.id == job_in.company_id).first()
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with ID {job_in.company_id} not found."
        )

    # 2. Delegate creation to the repository pattern
    return job_application_repo.create(db=db, obj_in=job_in)


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
    job = job_application_repo.get(db=db, id=job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found."
        )
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
    job = job_application_repo.get(db=db, id=job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found."
        )

    # Optional Validation: If the user is trying to change the company, ensure the new company exists!
    if job_in.company_id is not None:
        company = db.query(Company).filter(
            Company.id == job_in.company_id).first()
        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cannot update: Company with ID {job_in.company_id} not found."
            )

    # Delegate the update operation to the repository
    return job_application_repo.update(db=db, db_obj=job, obj_in=job_in)


@router.delete("/{job_id}", response_model=JobApplicationResponse)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    """
    Delete a job application.
    """
    job = job_application_repo.get(db=db, id=job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job application not found."
        )

    # Delete the record using the repository but return the deleted instance
    # so it correctly fulfills the response_model requirements
    job_application_repo.delete(db=db, id=job_id)
    return job
