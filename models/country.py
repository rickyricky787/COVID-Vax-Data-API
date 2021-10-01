# country model
from sqlalchemy.orm import backref
from extensions import db

class Country(db.Model):
    # Table Name
    __tablename__ = "country"

    # Columns
    country_id = db.Column(db.Integer, primary_key=True) # auto increments
    country_name = db.Column(db.String(40), nullable=False, unique=True)
    pop_size = db.Column(db.Integer)

    # Foreign Key
    continent_id = db.Column(db.Integer, db.ForeignKey("continent.continent_id"))

    # Relationships
    daily_vaccinations = db.relationship("DailyVaccination", backref="country") # A country their vaccination numbers daily (one-to-many)
    daily_covid_data = db.relationship("CovidData", backref="country") # A country enters covid data daily (one-to-many)
    total_vaccinations_by_brand = db.relationship("Vaccine", secondary="total_vaccination_by_brand", backref=db.backref("total_vax_by_brand", lazy="dynamic")) # many-to-many
    vaccine_brands_in_country = db.relationship("Vaccine", secondary="vaccine_brand_in_country", backref=db.backref("vax_brand_in_country", lazy="dynamic")) # many-to-many

    # Functions
    def data(self):
        return {
            "continent_id": self.continent_id,
            "country_id": self.country_id,
            "country_name": self.country_name,
            "pop_size": self.pop_size

        }
    
    def id(self):
        return self.country_id
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_name(cls, country_name):
        return cls.query.filter_by(country_name=country_name).first()

    @classmethod
    def get_by_id(cls, country_id):
        return cls.query.filter_by(country_id=country_id).first()