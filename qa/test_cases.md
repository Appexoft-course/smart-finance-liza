# Test Cases — Smart Finance API

## TC-01 Register User
**Precondition:** API is running.  
**Steps:**
1. Send POST `/auth/register`
2. Provide username, email, password

**Expected Result:**  
User is created successfully.

---

## TC-02 Login User
**Precondition:** User exists.  
**Steps:**
1. Send POST `/auth/login`
2. Provide valid credentials

**Expected Result:**  
API returns `access_token`.

---

## TC-03 Get Current User
**Precondition:** User is logged in.  
**Steps:**
1. Authorize with JWT token
2. Send GET `/auth/me`

**Expected Result:**  
Current user data is returned.

---

## TC-04 Unauthorized Transactions Request
**Steps:**
1. Send GET `/transactions/` without token

**Expected Result:**  
API returns `401 Unauthorized`.

---

## TC-05 Create Category
**Precondition:** User is authorized.  
**Steps:**
1. Send POST `/categories/`
2. Provide category name

**Expected Result:**  
Category is created.

---

## TC-06 Create Transaction
**Precondition:** User is authorized and category exists.  
**Steps:**
1. Send POST `/transactions/`
2. Provide title, amount, type, category_id

**Expected Result:**  
Transaction is created.

---

## TC-07 Update Transaction
**Precondition:** Transaction exists.  
**Steps:**
1. Send PUT `/transactions/{id}`
2. Provide updated data

**Expected Result:**  
Transaction is updated.

---

## TC-08 Delete Transaction
**Precondition:** Transaction exists.  
**Steps:**
1. Send DELETE `/transactions/{id}`

**Expected Result:**  
Transaction is deleted.

---

## TC-09 Forecast Task
**Precondition:** User has expense transactions.  
**Steps:**
1. Send POST `/forecast/expenses`
2. Copy task_id
3. Send GET `/forecast/expenses/{task_id}`

**Expected Result:**  
Forecast result is returned.