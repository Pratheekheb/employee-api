from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from typing import List
from models import Employee
import crud
from database import SessionLocal
router = APIRouter()
def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()
@router.get("/employees",response_model=List[Employee])
def get_employees(db:Session=Depends(get_db)):
    return crud.get_all_employees(db)
@router.post("/employees",response_model=Employee)
def create_employee(emp:Employee,db:Session=Depends(get_db)):
    return crud.add_employees(emp,db)
@router.put("/employees/{emp_id}",response_model=Employee)
def update_employee(emp_id:int,emp:Employee,db:Session=Depends(get_db)):
    updated=crud.update_employee(emp_id,emp,db)
    if updated:
        return updated
    raise HTTPException(status_code=404,detail="Employee not found")
@router.delete("/employees/{emp_id}",response_model=Employee)
def delete_employee(emp_id:int,db:Session=Depends(get_db)):
    deleted=crud.delete_employee(emp_id,db)
    if deleted:
        return deleted
    raise HTTPException(status_code=404,detail="employee_not_found")