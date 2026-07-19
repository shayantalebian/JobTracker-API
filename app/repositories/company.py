from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyRepository:

    def get(self, db: Session, company_id: int) -> Company | None:
        """Retrieve a single company by its ID."""
        return db.query(Company).filter(Company.id == company_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> list[Company]:
        """Retrieve a list of companies with pagination."""
        return db.query(Company).offset(skip).limit(limit).all()

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
