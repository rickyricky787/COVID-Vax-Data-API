from flask_restful import Resource
from http import HTTPStatus

from models.covid_data import CovidData
from models.country import Country

class CovidDataResource(Resource):
    def get(self):
        covid_bulk_data = CovidData.get_all()
        data = []

        for covid_data in covid_bulk_data:
            data.append(covid_data.data())
        
        return {"data": data}, HTTPStatus.OK

class CountryCovidDataResource(Resource):
    def get(self, country_name):
        country = Country.get_by_name(country_name=country_name)

        if country is None:
            return {"message": "country name not found"}, HTTPStatus.NOT_FOUND

        covid_bulk_data = CovidData.get_by_country_id(country_id=country.id())
        data = []

        for covid_data in covid_bulk_data:
            data.append(covid_data.data())
        
        return {"data": data}, HTTPStatus.OK

class LatestCovidDataResource(Resource):
    def get(self):
        covid_bulk_data = CovidData.get_lastest_all()
        data = []

        for covid_data in covid_bulk_data:
            data.append(covid_data.data())
        
        return {"data": data}, HTTPStatus.OK

class LatestCountryCovidDataResource(Resource):
    def get(self, country_name):
        country = Country.get_by_name(country_name=country_name)

        if country is None:
            return {"message": "country name not found"}, HTTPStatus.NOT_FOUND

        covid_bulk_data = CovidData.get_lastest_by_country(country_id=country.id())
        data = []

        for covid_data in covid_bulk_data:
            data.append(covid_data.data())
        
        return {"data": data}, HTTPStatus.OK
        

