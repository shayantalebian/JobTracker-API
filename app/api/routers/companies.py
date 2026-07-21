from fastapi import APIRouter, Depends, HTTPException, status, Query  # noqa
from app.core.exceptions import DuplicateResourceException
from sqlalchemy.orm import Session
from typing import List

from app.api.dependencies import get_db
from app.schemas.company import CompanyCreate, CompanyInDBBase, CompanyUpdate
from app.repositories.company import company_repo
from app.models.company import Company  # noqa
from app.core.exceptions import NotFoundException


# Initialize the router with a prefix and tags for Swagger UI
router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


@router.post("/", response_model=CompanyInDBBase, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    # 1. Use the repository to check for duplicates
    existing_company = company_repo.get_by_name(db, name=company.name)

    if existing_company:
        raise DuplicateResourceException(
            resource_name="Company",
            field_name="name",
            field_value=company.name
        )

    # 2. Delegate creation to the repository
    return company_repo.create(db, obj_in=company)


@router.get("/", response_model=List[CompanyInDBBase])
def read_companies(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(
        10, ge=1, le=100, description="Max records to return (max 100)"),
    search: str | None = Query(None, description="Filter by company name"),
    sort_by: str = Query(
        "id", description="Field to sort by (e.g., 'id', 'name', 'industry')"),
    sort_desc: bool = Query(False, description="Sort in descending order")
):
    """
    Retrieve a list of companies with optional search, sorting, and pagination.
    """
    return company_repo.get_all(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
        sort_by=sort_by,
        sort_desc=sort_desc
    )


@router.get("/{company_id}", response_model=CompanyInDBBase)
def read_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific company by its ID.
    """
    company = company_repo.get(db, company_id)
    if not company:
        raise NotFoundException(resource_name="Company",
                                resource_id=company_id)

    return company


@router.patch("/{company_id}", response_model=CompanyInDBBase)
def update_company(
    company_id: int,
    company_in: CompanyUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a company's details.
    """
    company = company_repo.get(db, company_id)
    if not company:
        raise NotFoundException(resource_name="Company",
                                resource_id=company_id)

    return company_repo.update(db, company, company_in)


@router.delete("/{company_id}", response_model=CompanyInDBBase)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    # 1. Fetch the object from the database first
    company = company_repo.get(db, company_id)

    # 2. Guard clause for 404
    if not company:
        raise NotFoundException(resource_name="Company",
                                resource_id=company_id)

    # 3. Pass the actual object (not the integer ID!) to the repository
    # Note: Passed positionally to avoid keyword errors
    return company_repo.delete(db, company)
