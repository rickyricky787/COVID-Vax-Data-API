# covid_data model
from extensions import db
from sqlalchemy import text

class CovidData(db.Model):
    # Table name
    __tablename__ = "covid_data"

    # Columns
    date_id = db.Column(db.Integer, primary_key=True)
    date_recorded = db.Column(db.DateTime)
    new_cases = db.Column(db.Integer)
    new_deaths = db.Column(db.Integer)
    total_cases = db.Column(db.Integer)
    total_deaths = db.Column(db.Integer)

    # Foreign Key
    country_id = db.Column(db.Integer, db.ForeignKey("country.country_id"))

    def data(self):
        return {
            "country_id": self.country_id,
            "date_id:": self.date_id,
            "date_recorded": self.date_recorded.isoformat(),
            "new_cases": self.new_cases,
            "new_deaths": self.new_deaths,
            "total_cases": self.total_cases,
            "total_deaths": self.total_deaths
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
        
    @classmethod
    def get_by_country_id(cls, country_id):
        return cls.query.filter_by(country_id=country_id).all()

    @classmethod
    def get_lastest_all(cls):
        sql_query = "WITH T AS (SELECT country_id, MAX(date_recorded) AS latest_date FROM covid_data GROUP BY country_id)\
            SELECT U.country_id, U.date_id, U.date_recorded, U.new_cases, U.new_deaths, U.total_cases, U.total_deaths\
            FROM covid_data AS U, T \
            WHERE U.date_recorded = T.latest_date and U.country_id = T.country_id"
        return cls.query.from_statement(text(sql_query)).all()
    

    @classmethod
    def get_lastest_by_country(cls, country_id):
        sql_query = "WITH T AS (SELECT country_id, MAX(date_recorded) AS latest_date FROM covid_data WHERE country_id = " + str(country_id) + ")\
            SELECT U.country_id, U.date_id, U.date_recorded, U.new_cases, U.new_deaths, U.total_cases, U.total_deaths\
            FROM covid_data AS U, T \
            WHERE U.date_recorded = T.latest_date and U.country_id = T.country_id"
        return cls.query.from_statement(text(sql_query)).all()