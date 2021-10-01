from flask_restful import Resource
from http import HTTPStatus

from models.daily_vaccination import DailyVaccination
from models.country import Country

class DailyVaccinationResource(Resource):
    def get(self):
        bulk_data = DailyVaccination.get_all()
        data = []

        for daily_vaccine_data in bulk_data:
            data.append(daily_vaccine_data.data())
        
        return {"data": data}, HTTPStatus.OK

class CountryDailyVaccinationResource(Resource):
    def get(self, country_name):
        country = Country.get_by_name(country_name=country_name)

        if country is None:
            return {"message": "country name not found"}, HTTPStatus.NOT_FOUND

        vax_bulk_data = DailyVaccination.get_by_country_id(country_id=country.id())
        data = []

        for vax_data in vax_bulk_data:
            data.append(vax_data.data())
        
        return {"data": data}, HTTPStatus.OK

class LatestDailyVaccinationResource(Resource):
    def get(self):
        bulk_data = DailyVaccination.get_lastest_all()
        data = []

        for daily_vaccine_data in bulk_data:
            data.append(daily_vaccine_data.data())
        
        return {"data": data}, HTTPStatus.OK

class LatestCountryDailyVaccinationResource(Resource):
    def get(self, country_name):
        country = Country.get_by_name(country_name=country_name)

        if country is None:
            return {"message": "country name not found"}, HTTPStatus.NOT_FOUND

        bulk_data = DailyVaccination.get_lastest_by_country(country_id=country.id())
        data = []

        for daily_vaccine_data in bulk_data:
            data.append(daily_vaccine_data.data())
        
        return {"data": data}, HTTPStatus.OK