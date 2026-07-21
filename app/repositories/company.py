from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyRepository:

    def get(self, db: Session, company_id: int) -> Company | None:
        """Retrieve a single company by its ID."""
        return db.query(Company).filter(Company.id == company_id).first()

    def get_by_name(self, db: Session, name: str) -> Company | None:
        """Retrieve a single company by its name (to prevent duplicates)."""
        return db.query(Company).filter(Company.name == name).first()

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

        if search:
            query = query.filter(Company.name.ilike(f"%{search}%"))

        sort_column = getattr(Company, sort_by, Company.id)
        if sort_desc:
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        return query.offset(skip).limit(limit).all()

    def create(self, db: Session, company_in: CompanyCreate) -> Company:
        db_company = Company(**company_in.model_dump())
        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company

    def update(self, db: Session, db_company: Company, company_in: CompanyUpdate) -> Company:
        update_data = company_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_company, field, value)

        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company

    def delete(self, db: Session, db_company: Company) -> Company:
        db.delete(db_company)
        db.commit()
        return db_company


company_repo = CompanyRepository()
