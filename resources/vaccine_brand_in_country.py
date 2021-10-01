from flask_restful import Resource
from http import HTTPStatus

from models.vaccine_brand_in_country import VaccineBrandInCountry
from models.country import Country
from models.vaccine import Vaccine

class VaccineBrandInCountryResource(Resource):
    def get(self):
        bulk_data = VaccineBrandInCountry.get_all()
        data = []

        for vaccine_brand_data in bulk_data:
            data.append(vaccine_brand_data.data())
        
        return {"data": data}, HTTPStatus.OK

class CountryVaccineBrandInCountryResource(Resource):
    def get(self, country_name):
        country = Country.get_by_name(country_name=country_name)

        if country is None:
            return {"message": "country name nont found"}, HTTPStatus.NOT_FOUND

        bulk_data = VaccineBrandInCountry.get_by_country_id(country_id=country.id())
        data = []

        for vaccine_brand_data in bulk_data:
            data.append(vaccine_brand_data.data())
        
        return {"data": data}, HTTPStatus.OK

class VaccineVaccineBrandInCountryResource(Resource):
    def get(self, vaccine_name):
        vaccine = Vaccine.get_by_name(vaccine_name=vaccine_name)

        if vaccine is None:
            return {"message": "vaccine name nont found"}, HTTPStatus.NOT_FOUND

        bulk_data = VaccineBrandInCountry.get_by_vaccine_id(vaccine_id=vaccine.id())
        data = []

        for vaccine_brand_data in bulk_data:
            data.append(vaccine_brand_data.data())
        
        return {"data": data}, HTTPStatus.OK
