from sqlite3 import connect
from sqlite3 import Error
from Image import *
from datetime import date
from Doctor import *


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_tables():
    database = r"C:\Users\Golnaz\Desktop\system design and analysis\picture-archiving-and-communication-system-PACS-\project.db"
    create_Doctor_table = """ CREATE TABLE IF NOT EXISTS doctor (
                                          doctor_ID integer PRIMARY KEY,
                                          password text NOT NULL,
                                          name text,
                                          major text,
                                          email text
                                      ); """

    create_Patient_table = """CREATE TABLE IF NOT EXISTS patient (
                                      patient_ID integer PRIMARY KEY,
                                      name text,
                                      diagnosis text,
                                      background_illness text,
                                      gender text,
                                      age integer,
                                      height integer,
                                      weight integer,
                                      email text,
                                      registration_date text,
                                      patient_doctor integer,
                                      FOREIGN KEY (patient_doctor) REFERENCES Doctor (doctor_ID) ON DELETE CASCADE
                                  );"""

    create_Image_table = """CREATE TABLE IF NOT EXISTS image (
                                         image_ID integer PRIMARY KEY,
                                         quality integer,
                                         type text,
                                         body_part text,
                                         date_inserted text,
                                         last_date_modified text,
                                         image_patient integer,
                                         FOREIGN KEY (image_patient) REFERENCES Patient (patient_ID) ON DELETE CASCADE
                                     );"""
    conn = connect(database)
    if conn is not None:
        create_table(conn, create_Doctor_table)
        create_table(conn, create_Patient_table)
        create_table(conn, create_Image_table)
    else:
        print("Error! cannot create the database connection.")


def insert_instances():
    doctor1 = Doctor(doctor_ID=1, password="1234", name="Ali mohammadi", major="physician",
                     email="gmesbahi.gm@gmail.com")
    doctor1.add_doctor()
    patient1 = Patient(patient_ID=1, name="sara shirazi", diagnosis="bleeding", background_illness="diabetes",
                       gender="female", age=29, height=10, weight=10, email="golsames@gmai.com",
                       registration_date=date(2020, 1, 1), patient_doctor=1)
    patient1.add_patient()
    image1 = Image(image_ID=1, quality=10, type="mri", body_part="head", date_inserted=date(2020, 1, 1),
                   last_date_modified=date(2020, 1, 1), image_patient=1)
    image1.add_image()


create_tables()
insert_instances()
