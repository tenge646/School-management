from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Teacher, Subject, Class

# sql engine and session
engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker(bind=engine)
session = Session()