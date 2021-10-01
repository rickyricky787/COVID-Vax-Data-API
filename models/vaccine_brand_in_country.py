# vaccine_brand_in_country model
from extensions import db

class VaccineBrandInCountry(db.Model):
    # Table name
    __tablename__ = "vaccine_brand_in_country"

    # Columns
    id = db.Column(db.Integer, primary_key=True)

    # Foreign Keys
    country_id = db.Column(db.Integer, db.ForeignKey("country.country_id"))
    vaccine_id = db.Column(db.Integer, db.ForeignKey("vaccine.vaccine_id"))

    # Functions
    def data(self):
        return {
            "id": self.id,
            "country_id": self.country_id,
            "vaccine_id": self.vaccine_id
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_country_id(cls, country_id):
        return cls.query.filter_by(country_id=country_id).all()

    @classmethod
    def get_by_vaccine_id(cls, vaccine_id):
        return cls.query.filter_by(vaccine_id=vaccine_id).all()