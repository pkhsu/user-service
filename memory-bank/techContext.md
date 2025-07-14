# Technical Context

## Technology Stack
- **Backend Framework**: Spring Boot 3.x
- **Frontend Framework**: Streamlit (Python)
- **Database**: MongoDB 6.0
- **ORM**: Spring Data MongoDB
- **API Style**: RESTful
- **Build Tool**: Maven (for backend), pip (for frontend)

## Development Environment
- **JDK Version**: 17+
- **Python Version**: 3.9+
- **IDE**: VSCode or IntelliJ IDEA
- **Containerization**: Docker + docker-compose

## Dependency Management
- **Backend**: Managed through pom.xml
  - Main dependencies:
    - spring-boot-starter-web
    - spring-boot-starter-data-mongodb
    - spring-boot-starter-test
- **Frontend**: Managed through frontend/requirements.txt
  - Main dependencies:
    - streamlit
    - pymongo

## Deployment
- Containerized deployment (Docker)
- Starts MongoDB, backend, and frontend services via docker-compose
