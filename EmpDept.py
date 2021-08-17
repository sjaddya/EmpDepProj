from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
engine = create_engine('sqlite:///EmpDept.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship

class Department(Base):
   __tablename__ = 'departments'
   Id = Column(Integer, primary_key = True)
   DepName = Column(String)
   employees = relationship('Employee', secondary = 'link')
   
class Employee(Base):
   __tablename__ = 'employees'
   Id = Column(Integer, primary_key = True)
   EmpName = Column(String)
   Age = Column(Integer)
   departments = relationship(Department,secondary='link')

class Link(Base):
        __tablename__ = 'link'
        department_id = Column(
                        Integer, 
                        ForeignKey('departments.Id'), 
                        primary_key = True)

        employee_id = Column(
                        Integer, 
                        ForeignKey('employees.Id'), 
                        primary_key = True)


Base.metadata.create_all(engine)

'''e1 = Employee(EmpName = "John", Age = 20)
d1 = Department(DepName = "Accounts")


e1.departments.append(d1)'''

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
'''session.add(e1)
session.add(d1)
session.commit()'''


def AddEmp(name, age):
    e = Employee(name, age)
    session.add(e)
    session.commit()

def AddDept(name):
    d = Department(name)
    session.add(d)
    session.commit()