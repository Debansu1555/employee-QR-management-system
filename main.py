from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os


# Database URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./employees.db")


# Database connection
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)


# Database session
SessionLocal = sessionmaker(bind=engine)


# Base class for database model
Base = declarative_base()


# FastAPI app
app = FastAPI()


# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Employee table
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    empId = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)
    department = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    category = Column(String, nullable=False)


# Create table automatically
Base.metadata.create_all(bind=engine)


# Login request model
class LoginData(BaseModel):
    email: str
    password: str


# Employee request model
class EmployeeData(BaseModel):
    name: str
    empId: str
    email: str
    department: str
    designation: str
    category: str


# Admin login API
@app.post("/api/login")
def login(data: LoginData):
    if data.email == "debanshusekhar55@gmail.com" and data.password == "1234":
        return {"message": "Login successful"}

    raise HTTPException(status_code=401, detail="Invalid login")


# Get all employees API
@app.get("/api/employees")
def get_employees():
    db = SessionLocal()

    try:
        employees = db.query(Employee).all()
        return employees

    finally:
        db.close()


# Get single employee by Employee ID API
@app.get("/api/employees/{emp_id}")
def get_employee(emp_id: str):
    db = SessionLocal()

    try:
        employee = db.query(Employee).filter(Employee.empId == emp_id).first()

        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        return employee

    finally:
        db.close()


# Add employee API
@app.post("/api/employees")
def add_employee(data: EmployeeData):
    db = SessionLocal()

    try:
        existing = db.query(Employee).filter(Employee.empId == data.empId).first()

        if existing:
            raise HTTPException(status_code=400, detail="Employee ID already exists")

        employee = Employee(
            name=data.name,
            empId=data.empId,
            email=data.email,
            department=data.department,
            designation=data.designation,
            category=data.category
        )

        db.add(employee)
        db.commit()
        db.refresh(employee)

        return {
            "message": "Employee added successfully",
            "employee": employee
        }

    finally:
        db.close()


# Update employee API
@app.put("/api/employees/{emp_id}")
def update_employee(emp_id: str, data: EmployeeData):
    db = SessionLocal()

    try:
        employee = db.query(Employee).filter(Employee.empId == emp_id).first()

        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        employee.name = data.name
        employee.empId = data.empId
        employee.email = data.email
        employee.department = data.department
        employee.designation = data.designation
        employee.category = data.category

        db.commit()
        db.refresh(employee)

        return {
            "message": "Employee updated successfully",
            "employee": employee
        }

    finally:
        db.close()


# Delete employee API
@app.delete("/api/employees/{emp_id}")
def delete_employee(emp_id: str):
    db = SessionLocal()

    try:
        employee = db.query(Employee).filter(Employee.empId == emp_id).first()

        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        db.delete(employee)
        db.commit()

        return {"message": "Employee deleted successfully"}

    finally:
        db.close()


# Serve frontend files from current project folder
app.mount("/", StaticFiles(directory=".", html=True), name="frontend")