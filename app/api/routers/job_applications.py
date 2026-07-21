from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api.dependencies import get_db
from app.schemas.job_application import JobApplicationCreate, JobApplicationResponse, JobApplicationUpdate
from app.models.job_application import JobApplication
from app.models.company import Company

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

    # 2. Convert Pydantic schema to SQLAlchemy model dictionary
    job_data = job_in.model_dump()

    # 3. Create the database object, add, and commit
    new_job = JobApplication(**job_data)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


@router.get("/", response_model=List[JobApplicationResponse])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of job applications.
    """
    jobs = db.query(JobApplication).offset(skip).limit(limit).all()
    return jobs


@router.get("/{job_id}", response_model=JobApplicationResponse)
def read_job(job_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific job application by its ID.
    """
    job = db.query(JobApplication).filter(JobApplication.id == job_id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Job application not found")
    return job


@router.patch("/{job_id}", response_model=JobApplicationResponse)
def update_job(job_id: int, job_in: JobApplicationUpdate, db: Session = Depends(get_db)):
    """
    Update a job application's details. 
    Only updates fields provided in the request body.
    """
    job = db.query(JobApplication).filter(JobApplication.id == job_id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Job application not found")

    # Optional Validation: If the user is trying to change the company, ensure the new company exists!
    if job_in.company_id is not None:
        company = db.query(Company).filter(
            Company.id == job_in.company_id).first()
        if not company:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cannot update: Company with id {job_in.company_id} not found"
            )

    # Use exclude_unset=True to only extract fields the client actually sent
    update_data = job_in.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)
    return job


@router.delete("/{job_id}", response_model=JobApplicationResponse)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    """
    Delete a job application.
    """
    job = db.query(JobApplication).filter(JobApplication.id == job_id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Job application not found")

    db.delete(job)
    db.commit()
    return job
