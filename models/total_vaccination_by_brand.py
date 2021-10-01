# total_vaccination_by_brand model
from extensions import db

class TotalVaccinationByBrand(db.Model):
    # Table name
    __tablename__ = "total_vaccination_by_brand"

    # Columns
    date_id = db.Column(db.Integer, primary_key=True)
    date_recorded = db.Column(db.DateTime)
    vaccination_total = db.Column(db.Integer)

    # Foreign Key
    country_id = db.Column(db.Integer, db.ForeignKey("country.country_id"))
    vaccine_id = db.Column(db.Integer, db.ForeignKey("vaccine.vaccine_id"))

    # Functions
    def data(self):
        return {
            "date_id": self.date_id,
            "date_recorded:": self.date_recorded.isoformat(),
            "vaccination_total": self.vaccination_total,
            "country_id": self.country_id,
            "vaccine_id": self.vaccine_id
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_country_id(cls, country_id):
        return cls.query.filter_by(country_id=country_id).all()