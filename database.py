from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "mysql+pymysql://root:Lambu%40pulvo01@localhost:3306/rest_apis_employee_db"
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
