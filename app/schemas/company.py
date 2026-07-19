from pydantic import BaseModel, Field, HttpUrl, ConfigDict, field_validator


class CompanyBase(BaseModel):
    """
    Base schema for Company containing shared properties.
    Enforces Task 6.8 (Length validation) and Task 6.7 (URL validation).
    """
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Name of the company (2-100 characters)."
    )
    website: HttpUrl | None = Field(
        default=None,
        description="Must be a valid URL with a scheme (e.g., https://...)"
    )
    industry: str | None = Field(
        default=None,
        max_length=50,
        description="Industry domain (max 50 characters)."
    )

    @field_validator('website', mode='after')
    @classmethod
    def serialize_url_to_str(cls, v: HttpUrl | None) -> str | None:
        """
        Pydantic v2 parses HttpUrl into a `Url` object. 
        This validator casts it back to a standard Python string 
        to ensure seamless integration with SQLAlchemy's String columns.
        """
        return str(v) if v else None


class CompanyCreate(CompanyBase):
    """
    Schema used for creating a new Company.
    Inherits all constraints directly from CompanyBase.
    """
    pass


class CompanyUpdate(CompanyBase):
    """
    Schema used for updating an existing Company (PATCH).
    All fields are redefined as optional to allow partial updates.
    """
    name: str | None = Field(None, min_length=2, max_length=100)
    # website and industry are already optional in the base class,
    # but we inherit them to keep the schema unified.


class CompanyInDBBase(CompanyBase):
    """
    Base schema for reading Company data from the database.
    Includes the database-generated ID.
    """
    id: int

    # ConfigDict(from_attributes=True) replaces `orm_mode = True` from Pydantic v1.
    # It tells Pydantic to read data even if it is not a dict, but an ORM model.
    model_config = ConfigDict(from_attributes=True)


class Company(CompanyInDBBase):
    """
    Schema used for returning Company data to the client in API responses.
    """
    pass
