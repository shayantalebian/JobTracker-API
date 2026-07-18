# Use official Python 3.12 slim image for a smaller footprint
FROM python:3.12-slim

# Copy the uv package manager binary directly from the official source
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set the working directory inside the container
WORKDIR /app

# Copy dependency files first (optimizes Docker caching)
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen

# Copy the rest of the application code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application with hot-reload enabled
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
