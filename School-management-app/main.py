from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Teacher, Subject, Class

# sql engine and session
engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

# Define functions for interacting with the system
def display_students():
    students = session.query(Student).all()
    for student in students:
        print("Student Name:", student.name)
        print("Student ID:", student.student_id)
        print("Grades:", student.grades)
        print("Teacher ID:", student.teacher_id)
        print()

def display_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print("Teacher Name:", teacher.name)
        print("Subject they teach:", teacher.class_name)
        print()

def display_subjects_and_teachers():
    subjects = session.query(Subject).all()
    for subject in subjects:
        print("Subject:", subject.subject_name)
        teachers = session.query(Teacher).filter_by(class_name=subject.subject_name).all()
        print("Teachers:")
        for teacher in teachers:
            print("- ", teacher.name)
        print()

def display_classes_and_teachers():
    classes = session.query(Class).all()
    for class_ in classes:
        print("Class:", class_.class_name)
        teachers = session.query(Teacher).filter_by(class_name=class_.class_name).all()
        print("Teacher:")
        for teacher in teachers:
            print("- ", teacher.name)
        print()