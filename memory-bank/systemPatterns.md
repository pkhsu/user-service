# System Architecture & Design Patterns

## Overall Architecture
Standard three-layer architecture:
1. **Presentation Layer**: Spring MVC Controllers
2. **Business Logic Layer**: Service components
3. **Data Access Layer**: Spring Data MongoDB Repositories

## Core Design Patterns
- **Dependency Injection**: Implemented via Spring's @Autowired
- **Repository Pattern**: UserRepository interface provides data access abstraction
- **Service Layer Pattern**: UserService encapsulates business logic

## Data Model
- Main entity: User
- Uses MongoDB document storage model
- Entity-to-collection mapping via @Document annotation

## API Design
- RESTful style
- Uses standard HTTP methods:
  - GET: Retrieve
  - POST: Create
  - PUT: Update
  - DELETE: Delete
