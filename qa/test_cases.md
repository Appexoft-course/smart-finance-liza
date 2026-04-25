# Test Cases

## TC-01 Register user
Steps:
1. POST /auth/register
2. Valid body

Expected:
201 Created

## TC-02 Login
Steps:
1. POST /auth/login
2. Valid credentials

Expected:
200 + access_token

## TC-03 Unauthorized access
Steps:
1. GET /transactions/

Expected:
401 Unauthorized

## TC-04 Create transaction
Steps:
1. Authorize
2. POST /transactions/

Expected:
201 Created

## TC-05 Data isolation
Steps:
1. User A creates transaction
2. User B requests list

Expected:
User B does NOT see A data

## TC-06 Forecast
Steps:
1. POST /forecast/expenses
2. GET result

Expected:
SUCCESS + result