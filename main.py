from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL missing in .env file")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

app = FastAPI(title="Employee QR Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# DATABASE MODEL
# =========================
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    qrId = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    empId = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)


Base.metadata.create_all(bind=engine)


# =========================
# DATABASE SESSION
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# REQUEST MODELS
# =========================
class LoginData(BaseModel):
    email: str
    password: str


class EmployeeData(BaseModel):
    name: str
    empId: str
    email: str
    department: str
    designation: str
    category: str


# =========================
# LOGIN
# =========================
@app.post("/api/login")
def login(data: LoginData):
    if data.email == "debanshusekhar55@gmail.com" and data.password == "1234":
        return {"message": "Login successful"}

    raise HTTPException(status_code=401, detail="Invalid login")


# =========================
# GET ALL EMPLOYEES
# =========================
@app.get("/api/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


# =========================
# GET EMPLOYEE BY EMPLOYEE ID
# =========================
@app.get("/api/employees/id/{emp_id}")
def get_employee_by_emp_id(emp_id: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.empId == emp_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# =========================
# GET EMPLOYEE BY QR ID
# =========================
@app.get("/api/employees/qr/{qr_id}")
def get_employee_by_qr_id(qr_id: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.qrId == qr_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


# =========================
# ADD EMPLOYEE
# =========================
@app.post("/api/employees")
def add_employee(data: EmployeeData, db: Session = Depends(get_db)):
    existing = db.query(Employee).filter(Employee.empId == data.empId).first()

    if existing:
        raise HTTPException(status_code=400, detail="Employee ID already exists")

    employee = Employee(
        qrId=str(uuid.uuid4()),
        name=data.name.strip(),
        empId=data.empId.strip(),
        email=data.email.strip(),
        department=data.department.strip(),
        designation=data.designation.strip(),
        category=data.category.strip()
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


# =========================
# UPDATE EMPLOYEE
# =========================
@app.put("/api/employees/{emp_id}")
def update_employee(emp_id: str, data: EmployeeData, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.empId == emp_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    duplicate = db.query(Employee).filter(
        Employee.empId == data.empId,
        Employee.id != employee.id
    ).first()

    if duplicate:
        raise HTTPException(status_code=400, detail="Employee ID already exists")

    # IMPORTANT:
    # qrId ko touch nahi karna
    employee.name = data.name.strip()
    employee.empId = data.empId.strip()
    employee.email = data.email.strip()
    employee.department = data.department.strip()
    employee.designation = data.designation.strip()
    employee.category = data.category.strip()

    db.commit()
    db.refresh(employee)

    return employee


# =========================
# DELETE EMPLOYEE
# =========================
@app.delete("/api/employees/{emp_id}")
def delete_employee(emp_id: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.empId == emp_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted successfully"}


# =========================
# FRONTEND
# =========================
app.mount("/", StaticFiles(directory=".", html=True), name="frontend")