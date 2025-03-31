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
1. Install dependencies:
```bash
# Backend
mvn install

# Frontend
pip install -r frontend/requirements.txt
```

2. Start services:
```bash
docker-compose up
```

3. Access applications:
- Backend API: http://localhost:8080
- Frontend UI: http://localhost:8501

## Project Structure
```
user-service/
├── frontend/    # Streamlit frontend
├── src/         # Spring Boot backend
└── memory-bank/ # Project documentation
