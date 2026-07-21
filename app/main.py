from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.routers import companies, job_applications
from app.core.exceptions import BaseAPIException
from app.core.logger import logger
from contextlib import asynccontextmanager


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # This block executes on startup
    logger.info("JobTrackr API is starting up...")
    yield
    # This block executes on shutdown
    logger.info("JobTrackr API is shutting down gracefully...")
# Initialize the main FastAPI application
app = FastAPI(
    title="JobTrackr API",
    description="A robust API for tracking job applications and managing company data.",
    version="1.0.0",
    lifespan=app_lifespan,  # Attach the lifespan context manager here
)


# ---------------------------------------------------------
# Router Registration
# ---------------------------------------------------------
# We use a prefix (e.g., /api/v1) for API versioning.
# This is a REST best practice so we can upgrade the API in
# the future without breaking older clients.
app.include_router(companies.router)
app.include_router(job_applications.router)


@app.exception_handler(BaseAPIException)
async def custom_api_exception_handler(request: Request, exc: BaseAPIException):
    """
    Catches all custom BaseAPIExceptions and returns a unified JSON structure.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "status_code": exc.status_code,
            "message": exc.message,
            "path": request.url.path
        }
    )

# A simple health-check/root endpoint


@app.get("/", tags=["Root"])
def read_root():
    logger.info("Root endpoint accessed.")
    return {
        "message": "Welcome to JobTrackr API!",
        "status": "Healthy",
        "version": "1.0.0"
    }
