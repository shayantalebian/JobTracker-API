from pydantic import BaseModel, Field, HttpUrl, ConfigDict, field_validator
from app.models.job_application import ApplicationStatus


class JobApplicationBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=150,
                       description="Job title (2-150 characters).")
    company_id: int = Field(...,
                            description="Foreign key linking to the Company ID.")
    status: ApplicationStatus = Field(
        default=ApplicationStatus.APPLIED, description="Current status of the application.")
    location: str | None = Field(
        default=None, max_length=100, description="Job location.")
    job_url: HttpUrl | None = Field(
        default=None, description="Valid URL linking to the original job posting.")
    notes: str | None = Field(default=None, max_length=500,
                              description="Personal notes about the application.")

    @field_validator('job_url', mode='after')
    @classmethod
    def serialize_url_to_str(cls, v: HttpUrl | None) -> str | None:
        """Safely casts the parsed Pydantic Url object to a string for SQLAlchemy."""
        return str(v) if v else None


class JobApplicationCreate(JobApplicationBase):
    pass


class JobApplicationUpdate(JobApplicationBase):
    title: str | None = Field(None, min_length=2, max_length=150)
    company_id: int | None = None
    status: ApplicationStatus | None = None

# Renamed to Response so it doesn't clash with the SQLAlchemy Model name!


class JobApplicationResponse(JobApplicationBase):
    id: int

    # Allows Pydantic to read data directly from the SQLAlchemy model
    model_config = ConfigDict(from_attributes=True)
