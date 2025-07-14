# User Service Management System

A user management system built with Spring Boot and Streamlit.

## Features
- User CRUD operations
- User status toggle
- Frontend-backend separation architecture

## Tech Stack
- Backend: Java Spring Boot
- Frontend: Python Streamlit
- Database: MongoDB

## Quick Start

To start the application, run the following command:

```bash
docker compose up -d --build
```

This command will build the Docker images for the backend and frontend services, and then start all the required containers in detached mode.

Once the services are running, you can access them at:
- Backend API: `http://localhost:8080/api/users`
- Frontend UI: `http://localhost:8501`

## Project Structure
```
user-service/
├── frontend/    # Streamlit frontend
├── src/         # Spring Boot backend
└── memory-bank/ # Project documentation
