from fastapi import FastAPI
from app.api.routers import companies, job_applications

# Initialize the main FastAPI application
app = FastAPI(
    title="JobTrackr API",
    description="A robust API for tracking job applications and managing company data.",
    version="1.0.0",
)

# ---------------------------------------------------------
# Router Registration
# ---------------------------------------------------------
# We use a prefix (e.g., /api/v1) for API versioning.
# This is a REST best practice so we can upgrade the API in
# the future without breaking older clients.
app.include_router(companies.router)
app.include_router(job_applications.router)

# A simple health-check/root endpoint


@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to JobTrackr API!",
        "status": "Healthy",
        "version": "1.0.0"
    }
