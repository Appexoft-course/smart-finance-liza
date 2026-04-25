# Test Plan — Smart Finance API

## Scope
- Auth (register, login, /auth/me)
- Categories
- Transactions (CRUD, filters)
- Forecast (Celery)

## Out of scope
- Frontend

## Test types
- Functional API testing
- Security (auth required)
- Negative testing

## Environments
- Local (Docker): web, db, redis, celery

## Entry criteria
- Services up (docker compose ps = all Up)
- Swagger доступний

## Exit criteria
- Critical bugs fixed
- Core flows pass

## Risks
- Token handling errors
- Data isolation bugs
- Async task delays