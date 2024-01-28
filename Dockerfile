# app/Dockerfile
# Stage 1: Build the application
FROM python:3.8-slim AS builder

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry install --no-dev

COPY . /app

# Stage 2: Create a lightweight image
FROM python:3.8-slim

WORKDIR /app

# Copy only necessary files from the builder stage
COPY --from=builder /app .

# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
