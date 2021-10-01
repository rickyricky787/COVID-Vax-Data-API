# daily_vaccination model
from extensions import db
from sqlalchemy import text

class DailyVaccination(db.Model):
    # Table name
    __tablename__ = "daily_vaccination"

    # Columns
    date_id = db.Column(db.Integer, primary_key=True)
    date_recorded = db.Column(db.DateTime())
    vaccination_total = db.Column(db.Integer)

    # Foreign Keys
    country_id = db.Column(db.Integer, db.ForeignKey("country.country_id"))

    # Functions
    def data(self):
        return {
            "date_id": self.date_id,
            "date_recorded": self.date_recorded.isoformat(),
            "vaccination_total": self.vaccination_total,
            "country_id": self.country_id
        }
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_country_id(cls, country_id):
        return cls.query.filter_by(country_id=country_id).all()
    
    @classmethod
    def get_lastest_all(cls):
        sql_query = "WITH T AS (SELECT country_id, MAX(date_recorded) AS latest_date FROM daily_vaccination GROUP BY country_id)\
            SELECT U.country_id, U.date_id, U.date_recorded, U.vaccination_total\
            FROM daily_vaccination AS U, T \
            WHERE U.date_recorded = T.latest_date and U.country_id = T.country_id"
        return cls.query.from_statement(text(sql_query)).all()

    @classmethod
    def get_lastest_by_country(cls, country_id):
        sql_query = "WITH T AS (SELECT country_id, MAX(date_recorded) AS latest_date FROM daily_vaccination WHERE country_id = " + str(country_id) + ")\
            SELECT U.date_id, U.country_id, U.date_recorded, U.vaccination_total\
            FROM daily_vaccination AS U, T \
            WHERE U.date_recorded = T.latest_date and U.country_id = T.country_id"
        return cls.query.from_statement(text(sql_query)).first()