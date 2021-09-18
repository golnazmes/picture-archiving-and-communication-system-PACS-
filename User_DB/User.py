from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///project.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'
    username = Column(String, primary_key=True)
    password = Column(String)
    email = Column(String)
    telegram_id = Column(String)

    def __init__(self, username, password, email, telegram_id):
        self.username = username
        self.password = password
        self.email = email
        self.telegram_id = telegram_id

    def insert_record(self):
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def login_authenticate(username_, password_):
        my_object = session.query(User).filter(User.username == username_, User.password == password_).first()
        print(my_object)
        if my_object:
            return True
        else:
            return False

    @staticmethod
    def signup_authenticate(username, password, email, telegram_id):
        my_object = session.query(User).filter(
            User.username == username, User.password == password, User.email == email,
            User.telegram_id == telegram_id).first()
        if my_object:
            return False
        else:
            new_user = User(username, password, email, telegram_id)
            new_user.insert_record()
            return False
