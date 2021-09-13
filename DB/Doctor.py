from sqlalchemy import Column, Integer, String
from sqlalchemy_utils.types import EmailType, PasswordType
#TODO:change datatype to emailType and passwordType
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///project.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Doctor(Base):
    __tablename__ = "doctor"
    doctor_ID = Column(Integer, primary_key=True)
    password = Column(String)
    name = Column(String)
    major = Column(String)
    email = Column(String)

    def __init__(self, doctor_ID=0, password=0, name="emtpy", major="physician", email="empty"):
        self.doctor_ID = doctor_ID
        self.password = password
        self.name = name
        self.major = major
        self.email = email

    def add_doctor(self):
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def delete_doctor(doctor_ID):
        doctor = session.query(Doctor).filter(Doctor.doctor_ID == doctor_ID)
        session.delete(doctor)
        # session.commit()
        # session.close()

    @staticmethod
    def show_doctor(doctor_ID):
        row = session.query(Doctor).filter(Doctor.doctor_ID == doctor_ID).all()
        return row

    @staticmethod
    def edit_doctor(doctor_ID, password, name, major, email):
        session.query(Doctor).filter(Doctor.doctor_ID == doctor_ID).update(
            {Doctor.password: password,
             Doctor.name: name,
             Doctor.major: major,
             Doctor.email: email
             }
        )
        Doctor.show_doctor(doctor_ID)
