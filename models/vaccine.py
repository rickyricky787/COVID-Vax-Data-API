# vaccine model
from sqlalchemy.orm import backref
from extensions import db

class Vaccine(db.Model):
    # Table name
    __tablename__ = "vaccine"

    # Columns
    vaccine_id = db.Column(db.Integer, primary_key=True)
    vaccine_name = db.Column(db.String(40), unique=True, nullable=False)

    # Functions
    def data(self):
        return {
            "vaccine_id": self.vaccine_id,
            "vaccine_name": self.vaccine_name
        }
    
    def id(self):
        return self.vaccine_id

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_name(cls, vaccine_name):
        return cls.query.filter_by(vaccine_name=vaccine_name).first()

    @classmethod
    def get_by_id(cls, vaccine_id):
        return cls.query.filter_by(vaccine_id=vaccine_id).first()

