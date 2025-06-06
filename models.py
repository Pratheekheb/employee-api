from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class EmployeeDB(Base):
    __tablename__="employee"
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String(100))
    email=Column(String(100))
    department=Column(String(100))
    salary=Column(Float)

from pydantic import BaseModel
from typing import Optional
class Employee(BaseModel):
    id:Optional[int]=None
    name:str
    email:str
    department:str
    salary:float
    class Config:
        from_attributes=True