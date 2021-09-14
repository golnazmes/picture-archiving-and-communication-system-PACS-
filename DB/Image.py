from DB.Patient import *


class Image(Base):
    __tablename__ = "image"
    image_ID = Column(Integer, primary_key=True)
    quality = Column(Integer)
    type = Column(String)
    body_part = Column(String)
    date_inserted = Column(Date)
    last_date_modified = Column(Date)
    image_patient = Column(Integer, ForeignKey("patient.patient_ID", ondelete="CASCADE"))
    patient = relationship("Patient", backref=backref("image"), cascade="all,delete")

    def __init__(self, image_ID, quality, type, body_part, date_inserted, last_date_modified, image_patient):
        self.image_ID = image_ID
        self.quality = quality
        self.type = type
        self.body_part = body_part
        self.date_inserted = date_inserted
        self.last_date_modified = last_date_modified
        self.image_patient = image_patient

    def add_image(self):
        session.add(self)
        session.commit()
        session.close()
