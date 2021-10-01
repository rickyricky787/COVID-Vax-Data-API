# continent model
from extensions import db

class Continent(db.Model):
    # Table name
    __tablename__ = "continent"

    # Columns
    continent_id = db.Column(db.Integer, primary_key=True) # auto increments
    continent_name = db.Column(db.String(40), nullable=False, unique=True)

    # Relationship
    country = db.relationship("Country", backref="continent") # A continent has many countries

    # Functions
    def data(self):
        return {
            "continent_id": self.continent_id,
            "continent_name:": self.continent_name
        }
    
    def id(self):
        return self.continent_id
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, continent_id):
        return cls.query.filter_by(continent_id=continent_id).first()