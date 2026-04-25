# QA Checklist — Smart Finance API

## Auth
- [ ] User can register
- [ ] User can login
- [ ] Login returns JWT token
- [ ] `/auth/me` works with token
- [ ] Protected endpoints reject requests without token

## Categories
- [ ] User can create category
- [ ] User can get category list
- [ ] Duplicate category is handled correctly

## Transactions
- [ ] User can create transaction
- [ ] User can get own transactions
- [ ] User can get one transaction
- [ ] User can update transaction
- [ ] User can delete transaction
- [ ] User cannot access another user's transactions

## Filters
- [ ] Filter by type works
- [ ] Filter by category works
- [ ] Filter by date range works

## Analytics
- [ ] Statistics by category works
- [ ] Balance endpoint works if implemented

## Forecast
- [ ] Forecast task starts
- [ ] Task ID is returned
- [ ] Forecast result can be received
- [ ] Celery worker processes task