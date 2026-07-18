from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

app = FastAPI(
    title="JobTrackr API",
    description="A comprehensive backend API for tracking job applications and managing the job hunt process.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to JobTrackr API!"}


@app.get("/db-health")
def database_health_check(db: Session = Depends(get_db)):
    """Test the database connection."""
    try:
        # Execute a simple query to test the connection
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connection is fully operational!"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database connection failed: {str(e)}")
