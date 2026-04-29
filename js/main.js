/* Check admin login */
function checkLogin() {

    /* If not logged in */
    if (sessionStorage.getItem("loggedIn") !== "true") {
        window.location.href = "index.html";
    }
}


/* Show toast message */
function showToast(msg) {

    /* Get toast box */
    let toast = document.getElementById("toast");

    /* If toast box not found */
    if (!toast) {
        alert(msg);
        return;
    }

    /* Show message */
    toast.innerText = msg;
    toast.style.opacity = "1";

    /* Hide after 2 seconds */
    setTimeout(() => {
        toast.style.opacity = "0";
    }, 2000);
}