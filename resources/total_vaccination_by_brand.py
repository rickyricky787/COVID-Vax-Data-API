from flask_restful import Resource
from http import HTTPStatus

from models.total_vaccination_by_brand import TotalVaccinationByBrand
from models.country import Country
from models.vaccine import Vaccine

class TotalVaccinationByBrandResource(Resource):
    def get(self):
        bulk_data = TotalVaccinationByBrand.get_all()
        data = []

        for total_vax_data in bulk_data:
            data.append(total_vax_data.data())
        
        return {"data": data}

class CountryTotalVaccinationByBrandResource(Resource):
    def get(self, country_name):
        country = Country.get_by_name(country_name=country_name)

        if country is None:
            return {"message": "country name nont found"}, HTTPStatus.NOT_FOUND

        bulk_data = TotalVaccinationByBrand.get_by_country_id(country_id=country.id())
        data = []

        for total_vax_data in bulk_data:
            data.append(total_vax_data.data())
        
        return {"data": data}, HTTPStatus.OK