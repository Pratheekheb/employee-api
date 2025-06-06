from sqlalchemy.orm import Session
from models import Employee,EmployeeDB
def get_all_employees(db:Session):
    return db.query(EmployeeDB).all()
def add_employees(emp:Employee,db:Session):
    try:
        db_emp=EmployeeDB(**emp.dict())
        db.add(db_emp)
        db.commit()
        db.refresh(db_emp)
        return db_emp
    
    except Exception as e:
        print("❌ DB ERROR:", e)   # ADD THIS
        raise
def update_employee(emp_id:int,updated:Employee,db:Session):
    emp=db.query(EmployeeDB).filter(EmployeeDB.id==emp_id).first()
    if emp:
        emp.name=updated.name
        emp.email=updated.email
        emp.department=updated.department
        emp.salary=updated.salary
        db.commit()
        db.refresh(emp)
        return emp
    return None
def delete_employee(emp_id:int,db:Session):
    emp=db.query(EmployeeDB).filter(EmployeeDB.id==emp_id).first()
    if emp:
        db.delete(emp)
        db.commit()
        return emp
    return None
 