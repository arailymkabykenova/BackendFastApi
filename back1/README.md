# Todo List API with FastAPI and PostgreSQL

This is a secure Todo List API built with FastAPI, PostgreSQL, and JWT authentication.

## Features

- User authentication with JWT
- CRUD operations for tasks
- PostgreSQL database with Alembic migrations
- Docker & Docker Compose support
- GitHub Actions CI/CD pipeline

## Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)

## Getting Started with Docker (Recommended)

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  Create a `.env` file in the root directory and fill it with your secrets:
    ```
    DATABASE_URL=postgresql://postgres:postgres@db:5432/tododb
    SECRET_KEY=your-super-secret-key-that-is-long-and-random
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

3.  Build and run the application with Docker Compose:
    ```bash
    docker-compose up --build
    ```
    The first time you run this, it will start the database and the web server. The web server might crash initially because the database tables are not created yet. This is expected.

4.  **Create the database tables using Alembic.**
    In a **new terminal window**, while the containers are running, execute the following command to run Alembic migrations inside the `web` container:
    ```bash
    docker-compose exec web alembic upgrade head
    ```
    This command will create the `users` and `tasks` tables in the database.

5.  The application should now be running correctly. The API will be available at `http://localhost:8000`, and the interactive documentation at `http://localhost:8000/docs`.

## API Endpoints
### Authentication
- POST `/token` - Login and get access token
- POST `/users/` - Create new user

### Tasks
- GET `/me` - Get current user info
- POST `/tasks/` - Create new task
- GET `/tasks/` - Get all tasks for current user
- GET `/tasks/{task_id}` - Get specific task
- PUT `/tasks/{task_id}` - Update task
- DELETE `/tasks/{task_id}` - Delete task
