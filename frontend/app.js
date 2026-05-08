const API_URL = "http://localhost:8000";
let token = localStorage.getItem("token") || "";

updateAuthStatus();

function show(elementId, data) {
    document.getElementById(elementId).innerText =
        typeof data === "string" ? data : JSON.stringify(data, null, 2);
}

function updateAuthStatus() {
    document.getElementById("authStatus").innerText =
        token ? "Авторизовано" : "Не авторизовано";
}

function getAuthHeaders() {
    return {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
    };
}

async function request(url, options = {}) {
    try {
        const response = await fetch(url, options);
        const text = await response.text();

        let data;
        try {
            data = text ? JSON.parse(text) : {};
        } catch {
            data = text;
        }

        if (!response.ok) {
            return {
                error: true,
                status: response.status,
                data
            };
        }

        return {
            error: false,
            status: response.status,
            data
        };
    } catch (error) {
        return {
            error: true,
            status: "NETWORK_ERROR",
            data: error.message
        };
    }
}

async function registerUser() {
    const data = {
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };

    const result = await request(`${API_URL}/auth/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    show("authResult", result.error ? result : "Registration successful. Now click Login.");
}

async function loginUser() {
    const data = {
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };

    const result = await request(`${API_URL}/auth/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    if (!result.error) {
        token = result.data.access_token;
        localStorage.setItem("token", token);
        updateAuthStatus();
        show("authResult", "Login successful.");
    } else {
        show("authResult", result);
    }
}

function logoutUser() {
    token = "";
    localStorage.removeItem("token");
    updateAuthStatus();
    show("authResult", "Logged out.");
}

async function createCategory() {
    const data = {
        name: document.getElementById("categoryName").value
    };

    const result = await request(`${API_URL}/categories/`, {
        method: "POST",
        headers: getAuthHeaders(),
        body: JSON.stringify(data)
    });

    show("categoryResult", result.data || result);
}

async function createTransaction() {
    const data = {
        title: document.getElementById("title").value,
        amount: Number(document.getElementById("amount").value),
        type: document.getElementById("type").value,
        category_id: Number(document.getElementById("categoryId").value)
    };

    const result = await request(`${API_URL}/transactions/`, {
        method: "POST",
        headers: getAuthHeaders(),
        body: JSON.stringify(data)
    });

    show("transactionResult", result.data || result);
}

async function getTransactions() {
    const result = await request(`${API_URL}/transactions/`, {
        headers: getAuthHeaders()
    });

    show("transactionsResult", result.data || result);
}

async function getExpenseTransactions() {
    const result = await request(`${API_URL}/transactions/?type=expense`, {
        headers: getAuthHeaders()
    });

    show("transactionsResult", result.data || result);
}

async function getStats() {
    const result = await request(`${API_URL}/transactions/stats/by-category`, {
        headers: getAuthHeaders()
    });

    show("analyticsResult", result.data || result);
}

async function getBalance() {
    const result = await request(`${API_URL}/analytics/balance`, {
        headers: getAuthHeaders()
    });

    show("analyticsResult", result.data || result);
}

async function startForecast() {
    const start = await request(`${API_URL}/forecast/expenses`, {
        method: "POST",
        headers: getAuthHeaders()
    });

    if (start.error) {
        show("forecastResult", start);
        return;
    }

    show("forecastResult", {
        message: "Forecast task started",
        task_id: start.data.task_id
    });

    setTimeout(async () => {
        const result = await request(`${API_URL}/forecast/expenses/${start.data.task_id}`, {
            headers: getAuthHeaders()
        });

        show("forecastResult", result.data || result);
    }, 1500);
}

function showPage(pageId) {
    document.querySelectorAll(".page").forEach(page => {
        page.classList.remove("active");
    });

    document.getElementById(pageId).classList.add("active");

    const titles = {
        dashboard: "Dashboard",
        auth: "Authorization",
        categories: "Categories",
        transactions: "Transactions",
        analytics: "Analytics",
        forecast: "Forecast"
    };

    document.getElementById("pageTitle").innerText = titles[pageId] || "Dashboard";

    const sidebar = document.getElementById("sidebar");
    sidebar.classList.remove("open");
}

function toggleSidebar() {
    document.getElementById("sidebar").classList.toggle("open");
}