# Test Plan — Smart Finance API

## Project
Smart Finance API — backend service for personal finance management, expense analytics and forecasting.

## Scope
Testing covers:
- Authentication
- Categories
- Transactions
- Filters
- Analytics
- Forecast with Celery
- Authorization and user data isolation

## Out of Scope
- UI design testing
- Performance testing
- Mobile testing

## Test Types
- Functional API testing
- Negative testing
- Security testing
- Regression testing
- Smoke testing

## Environment
- FastAPI
- PostgreSQL
- Redis
- Celery
- Docker Compose
- Swagger UI
- Pytest

## Entry Criteria
- Docker containers are running
- API is available at `http://localhost:8000/docs`
- Database connection works
- Redis and Celery worker are running

## Exit Criteria
- Critical API endpoints work correctly
- Authentication works
- Protected endpoints reject unauthorized users
- Core pytest tests pass

## Risks
- Incorrect JWT handling
- User data isolation bugs
- Celery task delay
- Database connection issues