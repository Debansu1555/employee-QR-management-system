function makeEmployeeQRText(emp) {
    return `${API_BASE}/view.html?qr=${emp.qrId}`;
}

function generateQRCode(containerId, emp) {
    let qrContainer = document.getElementById(containerId);
    qrContainer.innerHTML = "";

    new QRCode(qrContainer, {
        text: makeEmployeeQRText(emp),
        width: 220,
        height: 220
    });
}

function downloadQR(fileName = "employee_qr.png") {
    let img = document.querySelector("#qrcode img");

    if (!img) {
        alert("QR not ready");
        return;
    }

    let link = document.createElement("a");
    link.href = img.src;
    link.download = fileName;
    link.click();
}