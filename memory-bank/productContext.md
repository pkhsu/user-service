# Product Context

## Problem Statement
The system requires a centralized microservice for user data management, providing standardized CRUD operation interfaces and a simple web interface for administrators.

## Usage Scenarios
1. Other microservices querying user data via REST API
2. Admin backend managing user accounts through the `user-admin` web interface.
3. User registration/login systems requiring user data access

## User Experience Goals
- Provide stable and reliable user data access service via the REST API.
- Offer an intuitive and easy-to-use web interface for user management.
- API response time under 500ms
- 99.9% service availability

## Future Extensions
- Add user permission management
- Integrate third-party login services
- Provide user behavior analytics
