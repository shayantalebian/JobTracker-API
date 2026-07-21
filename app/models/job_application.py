import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

# 1. Define the Enum (Must inherit from str and enum.Enum)


class ApplicationStatus(str, enum.Enum):
    APPLIED = "APPLIED"
    INTERVIEWING = "INTERVIEWING"
    OFFER = "OFFER"
    REJECTED = "REJECTED"

# 2. Define the Database Table


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)

    # Use the Enum we defined above
    status = Column(SQLEnum(ApplicationStatus),
                    default=ApplicationStatus.APPLIED, nullable=False)

    location = Column(String(100), nullable=True)
    job_url = Column(String, nullable=True)
    notes = Column(String(500), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship back to the Company table
    company = relationship("Company", back_populates="job_applications")
