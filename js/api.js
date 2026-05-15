/* Get all employees */
async function getEmployees() {
    let res = await fetch(`${API_BASE}/api/employees`);

    if (!res.ok) {
        throw new Error("Failed to load employees");
    }

    return await res.json();
}


/* Get employee by Employee ID */
async function getEmployeeByEmpId(empId) {
    let res = await fetch(`${API_BASE}/api/employees/id/${empId}`);

    if (!res.ok) {
        return null;
    }

    return await res.json();
}


/* Get employee by permanent QR ID */
async function getEmployeeByQrId(qrId) {
    let res = await fetch(`${API_BASE}/api/employees/qr/${qrId}`);

    if (!res.ok) {
        return null;
    }

    return await res.json();
}


/* Add employee */
async function addEmployeeAPI(emp) {
    let res = await fetch(`${API_BASE}/api/employees`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(emp)
    });

    if (!res.ok) {
        let err = await res.json();
        throw new Error(err.detail || "Employee add failed");
    }

    return await res.json();
}


/* Update employee */
async function updateEmployeeAPI(oldEmpId, emp) {
    let res = await fetch(`${API_BASE}/api/employees/${oldEmpId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(emp)
    });

    if (!res.ok) {
        let err = await res.json();
        throw new Error(err.detail || "Update failed");
    }

    return await res.json();
}


/* Delete employee */
async function deleteEmployeeAPI(empId) {
    let res = await fetch(`${API_BASE}/api/employees/${empId}`, {
        method: "DELETE"
    });

    if (!res.ok) {
        let err = await res.json();
        throw new Error(err.detail || "Delete failed");
    }

    return await res.json();
}