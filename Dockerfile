# Use an official Python runtime as a parent image
FROM python:3.8-slim

LABEL maintainer="Shukran Jabbarov <shukranjsp@gmail.com>"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Copy only the necessary files
COPY pyproject.toml poetry.lock /app/
# Install Poetry and project dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
