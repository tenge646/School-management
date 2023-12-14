from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#Creating the SQLAlchemy engine and session
engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()

#Defining the Student data model
class Student(Base):
    tablename = 'students'

student_id = Column(Integer, primary_key=True)
name = Column(String(100), nullable=False)
grades = Column(String(100), nullable=True)
teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'), nullable=True)

teacher = relationship('Teacher', back_populates='students')

#Defining the Teacher data model
class Teacher(Base):
    tablename = 'teachers'

teacher_id = Column(Integer, primary_key=True)
name = Column(String(100), nullable=False)
class_name = Column(String(100), nullable=True)

students = relationship('Student', back_populates='teacher')

#Definin the Subject data model
class Subject(Base):
    tablename = 'subjects'

subject_id = Column(Integer, primary_key=True)
subject_name = Column(String(100), nullable=False)

#Defining the Class data model
class Class(Base):
    tablename = 'classes'

class_id = Column(Integer, primary_key=True)
class_name = Column(String(100), nullable=False)
Base.metadata.create_all(engine)