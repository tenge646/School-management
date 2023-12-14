from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Teacher, Subject, Class

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

# Seed initial data
# Students
students_data = [
    {'name': 'Alice', 'grades': 'A', 'teacher_id': 1},
    {'name': 'Bob', 'grades': 'B', 'teacher_id': 2},
    {'name': 'Charlie', 'grades': 'C', 'teacher_id': 1},
    # Add more students here
]

for data in students_data:
    student = Student(**data)
    session.add(student)

# Teachers
teachers_data = [
    {'name': 'Mr. Smith', 'class_name': 'Math'},
    {'name': 'Ms. Johnson', 'class_name': 'English'},
    # Add more teachers here
]

for data in teachers_data:
    teacher = Teacher(**data)
    session.add(teacher)

# Subjects
subjects_data = [
    {'subject_name': 'Math'},
    {'subject_name': 'English'},
    # Add more subjects here
]

for data in subjects_data:
    subject = Subject(**data)
    session.add(subject)

# Classes
classes_data = [
    {'class_name': 'Math Class'},
    {'class_name': 'English Class'},
    # Add more classes here
]

for data in classes_data:
    class_ = Class(**data)
    session.add(class_)

# Commit the changes to the database
session.commit()