/* Admin login */
async function login() {

    /* Get login values */
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();

    /* Send login request */
    let res = await fetch(`${API_BASE}/api/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    });

    /* If login success */
    if (res.ok) {
        sessionStorage.setItem("loggedIn", "true");
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid login");
    }
}


/* Admin logout */
function logout() {
    sessionStorage.removeItem("loggedIn");
    window.location.href = "index.html";
}