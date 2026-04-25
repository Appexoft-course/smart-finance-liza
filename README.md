# Smart Finance API

Smart Finance API — це backend-проєкт для управління особистими фінансами з аналітикою витрат і фоновим прогнозуванням майбутніх витрат.

Проєкт створений як pet project на основі дипломної теми:  
**“Інтелектуальна система управління особистими фінансами з прогнозуванням витрат”**.

## Основна ідея

Система дозволяє користувачу:
- реєструватися та авторизуватися;
- створювати категорії витрат;
- додавати фінансові транзакції;
- переглядати тільки власні транзакції;
- фільтрувати транзакції;
- отримувати просту аналітику;
- запускати фонове прогнозування витрат через Celery.

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Docker
- Docker Compose

### Background tasks
- Celery
- Redis

### Planned QA/Automation
- Pytest API tests
- Manual test cases
- Postman collection
- Java RestAssured tests

## Project Structure

```text
smart-finance-api/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── tasks/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   └── planned simple HTML/CSS/JS client
│
├── qa/
│   └── planned manual QA documentation
│
├── automation-python/
│   └── planned pytest API tests
│
├── automation-java/
│   └── planned Java RestAssured tests
│
├── docker/
├── logs/
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```
## Features Implemented
### Authentication

- User registration
- User login
- JWT access token generation
- Protected endpoints
- Current user endpoint `/auth/me`
### Categories
- Create category
- Get categories
### Transactions
- Create transaction
- Get all user transactions
- Get one transaction
- Update transaction
- Delete transaction
- User data isolation: each user sees only their own transactions
### Filters
Transactions can be filtered by:
- type: income / expense
- category
- date range
### Analytics
Implemented basic expense aggregation by category:
```text
GET /transactions/stats/by-category
```
```json
Example response:

{
  "1": 300
}
```
### Forecasting with Celery + Redis
Implemented background task for simple expense forecasting.
Start forecast task:
```text
POST /forecast/expenses
```
Get forecast result:
```text
GET /forecast/expenses/{task_id}
```
Example result:
```json
{
  "task_id": "example-task-id",
  "status": "SUCCESS",
  "result": {
    "average_expense": 300,
    "forecast_next_month": 330,
    "method": "simple_average_plus_10_percent"
  }
}
```
## How to Run
### 1. Clone repository
```text
git clone <repository-url>
cd smart-finance-api
```
### 2. Create .env
Create a .env file inside backend/ based on .env.example.
Example:
```text
POSTGRES_DB=finance_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1234
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379

SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
### 3. Run with Docker Compose
```bash
docker compose up --build -d
```
### 4. Check containers
```bash
docker compose ps
```
Expected services:
```text
smart_finance_web
smart_finance_db
smart_finance_redis
smart_finance_celery
```
### 5. Open Swagger
```text
http://localhost:8000/docs
```
### 6.Testing

Run tests:

```bash
pytest
```
## Main API Endpoints
### Auth
```text
POST /auth/register
POST /auth/login
GET /auth/me
```
### Categories
```text
POST /categories/
GET /categories/
```
### Transactions
```text
POST /transactions/
GET /transactions/
GET /transactions/{transaction_id}
PUT /transactions/{transaction_id}
DELETE /transactions/{transaction_id}
GET /transactions/stats/by-category
```
### Forecast
```text
POST /forecast/expenses
GET /forecast/expenses/{task_id}
```
## Example Flow
### 1. Register
```json
{
  "username": "liza",
  "email": "liza@example.com",
  "password": "1234"
}
```
### 2. Login
```json
{
  "username": "liza",
  "email": "liza@example.com",
  "password": "1234"
}
```
Response:
```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```
### 3. Authorize in Swagger
Click Authorize and paste only the token value.
### 4. Create category
```json
{
  "name": "Food"
}
```
### 5. Create transaction
```json
{
  "title": "Lunch",
  "amount": 300,
  "type": "expense",
  "category_id": 1
}
```
### 6. Start forecast
```text
POST /forecast/expenses
```
### 7. Get forecast result
```text
GET /forecast/expenses/{task_id}
```
## QA Value
This project is also planned as a QA portfolio project. It will include:
- manual test plan;
- checklist;
- test cases;
- bug reports;
- Postman collection;
- API automation tests with Pytest;
- Java API automation tests with RestAssured.
## Planned Improvements
- More advanced forecasting logic
- Monthly statistics
- Budget limits
- Category-based reports
- Frontend client
- Pytest API tests
- Java RestAssured tests
- GitHub Actions CI
- Better error handling
- Alembic migrations
# Java API Automation Tests
This folder contains Java API automation tests for Smart Finance API.
## Tech Stack
- Java
- JUnit 5
- RestAssured
- Maven
## How to Run
Make sure Smart Finance API is running:

```bash
docker compose up -d
```
### Then run:
```bash
mvn test
```
