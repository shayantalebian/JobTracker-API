from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # API Configurations
    PROJECT_NAME: str = "JobTracker API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Databse Configurations
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432

    # Pydantic Config to read from .env file
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True)

    @property
    def DATABASE_URL(self) -> str:
        """
        Constructs the PostgreSQL database URL from the provided settings.
        """
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()
