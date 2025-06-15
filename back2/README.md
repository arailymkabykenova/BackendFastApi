# AI Chatbot API with FastAPI

This project implements a FastAPI-based backend service with an AI-powered chatbot, background task processing using Celery, and Redis for task queue management.

## Features

- AI Chatbot using OpenAI's GPT-3.5
- Background task processing with Celery
- Redis for task queue management
- PostgreSQL database
- Docker containerization
- Swagger UI documentation

## Prerequisites

- Docker and Docker Compose
- OpenAI API key

## Project Structure

```
.
├── app/
│   ├── assistant/
│   │   └── assistant.py    # AI assistant implementation
│   ├── routers/
│   │   └── chat.py        # Chat API endpoints
│   ├── main.py            # FastAPI application
│   ├── worker.py          # Celery worker configuration
│   ├── tasks.py           # Background tasks
│   └── models.py          # Database models
├── docker-compose.yml     # Docker services configuration
├── Dockerfile            # Docker image configuration
└── requirements.txt      # Python dependencies
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create a `.env` file in the project root with your OpenAI API key:
```
SECRET_KEY=sk-your-openai-api-key-here
```

3. Build and start the containers:
```bash
docker-compose up -d
```

## Services

The application consists of the following services:

- **Web**: FastAPI application (port 8000)
- **Redis**: Message broker for Celery (port 6379)
- **PostgreSQL**: Database (port 5432)
- **Celery Worker**: Background task processor
- **Celery Beat**: Task scheduler

## API Documentation

Once the application is running, you can access the Swagger UI documentation at:
```
http://localhost:8000/docs
```

### Chat Endpoint

- **POST** `/api/chat`
  - Request body:
    ```json
    {
        "message": "Your message here"
    }
    ```
  - Response:
    ```json
    {
        "response": "AI assistant's response"
    }
    ```

## Background Tasks

The application includes a daily task that fetches data from a website and saves it to the database. This task runs automatically at midnight UTC.

## Development

To make changes to the code:

1. Modify the relevant files
2. Rebuild the containers:
```bash
docker-compose down
docker-compose build
docker-compose up -d
```

## Environment Variables

- `SECRET_KEY`: Your OpenAI API key
- `DATABASE_URL`: PostgreSQL connection string (default: postgresql://postgres:postgres@db:5432/tododb)
- `REDIS_URL`: Redis connection string (default: redis://redis:6379/0)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
