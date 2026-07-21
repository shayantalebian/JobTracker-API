from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api.dependencies import get_db
from app.schemas.company import CompanyCreate, CompanyInDBBase, CompanyUpdate
from app.repositories.company import company_repo
from app.models.company import Company

# Initialize the router with a prefix and tags for Swagger UI
router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


@router.post("/", response_model=CompanyInDBBase, status_code=status.HTTP_201_CREATED)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    # 1. FIX: Query the 'Company' model directly
    existing_company = db.query(Company).filter(
        Company.name == company.name).first()

    if existing_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company with this name already exists"
        )

    # 2. Create and save the new record
    new_company = Company(**company.model_dump())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company


@router.get("/", response_model=List[CompanyInDBBase])
def read_companies(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve a list of companies.
    """
    return company_repo.get_all(db=db, skip=skip, limit=limit)


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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )

    return company_repo.update(db, company, company_in)


@router.delete("/{company_id}", response_model=CompanyInDBBase)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    # 1. Fetch the object from the database first
    company = company_repo.get(db, company_id)

    # 2. Guard clause for 404
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    # 3. Pass the actual object (not the integer ID!) to the repository
    # Note: Passed positionally to avoid keyword errors
    return company_repo.delete(db, company)
