# Bug Reports

## BUG-001 — Unauthorized request without token

**Status:** Expected behavior  
**Severity:** Low  
**Steps to reproduce:**
1. Send GET `/transactions/` without Authorization header

**Actual result:**  
API returns 401.

**Expected result:**  
API should return 401.

---

## BUG-002 — Duplicate category

**Status:** To verify  
**Severity:** Medium  
**Steps to reproduce:**
1. Create category `Food`
2. Create category `Food` again

**Expected result:**  
API should return clear validation error.