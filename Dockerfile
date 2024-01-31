# Use an official Python runtime as a parent image
FROM python:3.8-slim

LABEL maintainer="Shukran Jabbarov <shukranjsp@gmail.com>"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["echo", "DATABASE_URL: ${DATABASE_URL}"]

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /project

COPY . /project

# Install Poetry and project dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi



# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
