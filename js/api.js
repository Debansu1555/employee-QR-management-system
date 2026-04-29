/* Get all employees */
async function getEmployees() {
    let res = await fetch(`${API_BASE}/api/employees`);
    return await res.json();
}


/* Get one employee by Employee ID */
async function getEmployeeById(empId) {
    let res = await fetch(`${API_BASE}/api/employees/${empId}`);

    if (!res.ok) {
        return null;
    }

    return await res.json();
}


/* Add employee */
async function addEmployeeAPI(emp) {
    return await fetch(`${API_BASE}/api/employees`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(emp)
    });
}


/* Update employee */
async function updateEmployeeAPI(oldEmpId, emp) {
    return await fetch(`${API_BASE}/api/employees/${oldEmpId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(emp)
    });
}


/* Delete employee */
async function deleteEmployeeAPI(empId) {
    return await fetch(`${API_BASE}/api/employees/${empId}`, {
        method: "DELETE"
    });
}