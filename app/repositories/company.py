from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyRepository:

    def get(self, db: Session, company_id: int) -> Company | None:
        """Retrieve a single company by its ID."""
        return db.query(Company).filter(Company.id == company_id).first()

    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 100,
        search: str | None = None,
        sort_by: str = "id",
        sort_desc: bool = False
    ) -> list[Company]:
        """Retrieve companies with pagination, filtering, and sorting."""
        query = db.query(Company)

        # 1. Filtering (Task 9.2) - Search by company name (case-insensitive)
        if search:
            query = query.filter(Company.name.ilike(f"%{search}%"))

        # 2. Sorting (Task 9.3) - Dynamic column sorting
        # Fallback to ID if invalid
        sort_column = getattr(Company, sort_by, Company.id)
        if sort_desc:
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        # 3. Pagination (Task 9.1)
        return query.offset(skip).limit(limit).all()

    def create(self, db: Session, company_in: CompanyCreate) -> Company:
        """Create a new company record."""
        # Convert Pydantic schema to dictionary and unpack into the SQLAlchemy model
        db_company = Company(**company_in.model_dump())
        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company

    def update(self, db: Session, db_company: Company, company_in: CompanyUpdate) -> Company:
        """Update an existing company record."""
        # Extract fields that were explicitly set in the request
        update_data = company_in.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(db_company, field, value)

        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company

    def delete(self, db: Session, db_company: Company) -> Company:
        """Delete a company record."""
        db.delete(db_company)
        db.commit()
        return db_company


# Instantiate the repository so it can be easily imported and used across the app
company_repo = CompanyRepository()
