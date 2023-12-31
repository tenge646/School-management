from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define the Student data model
class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    grades = Column(String(100), nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'), nullable=True)

    teacher = relationship('Teacher', back_populates='students')

# Define the Teacher data model
class Teacher(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    class_name = Column(String(100), nullable=True)

    students = relationship('Student', back_populates='teacher')

# Define the Subject data model
class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String(100), nullable=False)

# Define the Class data model
class Class(Base):
    __tablename__ = 'classes'

    class_id = Column(Integer, primary_key=True)
    class_name = Column(String(100), nullable=False)

Base.metadata.create_all(engine)
