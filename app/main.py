from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="JobTrackr API",
    description="A comprehensive backend API for tracking job applications and managing the job hunt process.",
    version="1.0.0",
)


@app.get("/", tags=["Health"])
async def root():
    """
    Health check endpoint to verify the API is running.
    """
    return JSONResponse(
        content={
            "status": "healthy",
            "message": "Welcome to JobTrackr API!",
            "version": app.version
        }
    )
