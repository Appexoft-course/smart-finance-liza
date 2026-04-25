const API_URL = "http://localhost:8000";
let token = "";

async function login() {
    const data = {
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };

    const response = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();

    if (response.ok) {
        token = result.access_token;
        document.getElementById("loginResult").innerText = "Login successful";
    } else {
        document.getElementById("loginResult").innerText = JSON.stringify(result);
    }
}

async function createCategory() {
    const data = {
        name: document.getElementById("categoryName").value
    };

    await fetch(`${API_URL}/categories/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(data)
    });

    alert("Category created");
}

async function createTransaction() {
    const data = {
        title: document.getElementById("title").value,
        amount: Number(document.getElementById("amount").value),
        type: document.getElementById("type").value,
        category_id: Number(document.getElementById("categoryId").value)
    };

    await fetch(`${API_URL}/transactions/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(data)
    });

    alert("Transaction created");
}

async function getTransactions() {
    const response = await fetch(`${API_URL}/transactions/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const result = await response.json();
    document.getElementById("transactions").innerText = JSON.stringify(result, null, 2);
}

async function startForecast() {
    const response = await fetch(`${API_URL}/forecast/expenses`, {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const result = await response.json();
    document.getElementById("forecast").innerText = JSON.stringify(result, null, 2);
}