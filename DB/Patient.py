from DB.Doctor import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Date, ForeignKey

class Patient(Base):
    __tablename__ = "patient"
    patient_ID = Column(Integer, primary_key=True)
    name = Column(String)
    diagnosis = Column(String)
    background_illness = Column(String)
    gender = Column(String)
    age = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)
    email = Column(String)
    registration_date = Column(Date)
    patient_doctor = Column(Integer, ForeignKey("doctor.doctor_ID", ondelete="CASCADE"))
    doctor = relationship("Doctor", backref=backref("patient"), cascade="all,delete")

    def __init__(self, patient_ID, name, diagnosis, background_illness, gender, age, height, weight, email,
                 registration_date, patient_doctor):
        self.patient_ID = patient_ID
        self.name = name
        self.diagnosis = diagnosis
        self.background_illness = background_illness
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.email = email
        self.registration_date = registration_date
        self.patient_doctor = patient_doctor

    def add_patient(self):
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def delete_patient(patient_ID):
        patient = session.query(Patient).filter(Patient.patient_ID == patient_ID)
        session.delete(patient)
        # session.commit()
        # session.close()

    @staticmethod
    def show_patient(patient_ID):
        row = session.query(Patient).filter(Patient.patient_ID == patient_ID).all()
        return row

    @staticmethod
    def edit_patient(patient_ID, name, diagnosis, background_illness, gender, age, height, weight, email,
                     registration_date, patient_doctor):
        session.query(Patient).filter(Patient.patient_ID == patient_ID).update(
            {
                Patient.name: name,
                Patient.diagnosis: diagnosis,
                Patient.background_illness: background_illness,
                Patient.gender: gender,
                Patient.age: age,
                Patient.height: height,
                Patient.weight: weight,
                Patient.email: email,
                Patient.registration_date: registration_date,
                Patient.patient_doctor: patient_doctor
            }
        )
        Patient.show_patient(patient_ID)
