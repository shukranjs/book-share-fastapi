# FastAPI Book Sharing Project

Welcome to the FastAPI Book Sharing Project! This project is designed for sharing books among users, including features such as user registration, authentication, and book-related functionalities.

## Project Structure

- `app/`: Main application directory.
  - `main.py`: FastAPI main application.
  - `auth/`: Authentication-related functionality.
    - `jwt.py`: JWT authentication functions.
  - `crud/`: CRUD operations for different entities.
    - `user.py`: CRUD operations for users.
  - `models/`: Pydantic models for data validation.
    - `user.py`: User models.
  - `routers/`: FastAPI routers for different endpoints.
    - `user.py`: User-related routes.
  - `tests/`: Directory for testing modules.
  - `example_file.txt`: Example file used in file I/O operations.

## Requirements

- Python 3.7 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- [Docker](https://www.docker.com/) for containerization
- [PostgreSQL](https://www.postgresql.org/) as the database

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/fastapi-book-sharing.git
   cd fastapi-book-sharing
