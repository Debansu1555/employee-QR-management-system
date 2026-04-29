/* Create live QR URL */
function makeEmployeeQRText(emp) {
    return `${API_BASE}/view.html?id=${emp.empId}`;
}


/* Generate QR code */
function generateQRCode(containerId, emp) {

    /* Get QR container */
    let qrContainer = document.getElementById(containerId);

    /* Clear old QR */
    qrContainer.innerHTML = "";

    /* Create new QR */
    new QRCode(qrContainer, {
        text: makeEmployeeQRText(emp),
        width: 220,
        height: 220
    });
}


/* Download QR image */
function downloadQR(fileName = "employee_qr.png") {

    /* Get QR image */
    let img = document.querySelector("#qrcode img");

    /* If QR not generated */
    if (!img) {
        alert("QR not ready");
        return;
    }

    /* Download QR */
    let link = document.createElement("a");
    link.href = img.src;
    link.download = fileName;
    link.click();
}