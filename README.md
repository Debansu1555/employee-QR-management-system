# Employee QR Management System

A professional Employee QR Management System built using **FastAPI + HTML + CSS + JavaScript + SQLite**.

This project allows Admin to:

* Login securely
* Add new employees
* Generate QR Codes for employees
* Edit employee details
* Delete employee records
* View employee profile with QR
* Deploy the system live so any mobile QR scanner can open employee details directly

The QR Code stores a **live URL** like:

```text
https://your-domain.com/view.html?id=18300
```

This ensures:

* Same QR remains active forever
* Employee details can be updated anytime
* Any mobile QR scanner can open the latest employee details

---

# Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* QRCode.js Library

## Backend

* FastAPI
* Python

## Database

* SQLite (Local Development)
* PostgreSQL (Recommended for Production)

## Deployment

* GitHub
* Render

---

# Features

## Admin Panel

### Secure Login

Default Login:

```text
Email: debanshusekhar55@gmail.com
Password: 1234
```

---

## Employee Management

### Add Employee

Admin can add:

* Full Name
* Employee ID
* Mail ID
* Department
* Designation
* Category

---

## QR Code Generation

Each employee gets a unique QR Code.

Example QR Content:

```text
https://your-domain.com/view.html?id=18300
```

---

## Edit Employee

Admin can update:

* Name
* Email
* Department
* Designation
* Category

Same QR remains valid.

---

## Delete Employee

Admin can permanently remove employee records.

---

## Public Employee View Page

When anyone scans QR:

* Employee profile opens automatically
* Latest updated details are shown

No login required.

---

# Project Structure

```text
EMPLOYEE_QR_NO_SERVER/
│
├── main.py
├── requirements.txt
│
├── index.html
├── dashboard.html
├── add.html
├── edit.html
├── view.html
│
├── css/
│   └── style.css
│
├── js/
│   ├── config.js
│   ├── auth.js
│   ├── main.js
│   ├── api.js
│   └── qr.js
│
└── employees.db
```

---



# Final Live URL

Example:

```text
https://employee-qr-management-system.onrender.com
```

Now QR codes work from:

* Mobile Camera
* Google Lens
* Any QR Scanner App

---

# Important Notes

## Do NOT Upload

Add `.gitignore`

```text
venv/
__pycache__/
*.pyc
employees.db
.vscode/
```

---

## Production Recommendation

Use:

```text
PostgreSQL
```

instead of SQLite for production deployment.

SQLite may reset on free hosting redeploys.

---

# Future Upgrades

Recommended advanced features:

* Employee Photo Upload
* ID Card PDF Download
* Excel Export
* Department Filter
* Search Employee
* Admin Password Change
* Backup & Restore
* QR Scan History
* Multi Admin Panel
* Role-Based Access Control

---

# Author

Developed by:

**Debanshu Sekhar Bal**

Junior Python Full Stack Developer

CR Cyber Crime Foundation

---

# License

This project is developed for professional employee management and QR-based identification systems.

All rights reserved.
