from flask_restful import Resource
from http import HTTPStatus

from models.country import Country

class CountryResource(Resource):
    def get(self):
        countries = Country.get_all()
        data = []
        
        for country in countries:
            data.append(country.data())
        
        return {"data": data}, HTTPStatus.OK

class CountryIdResource(Resource):
    def get(self, country_id):
        country = Country.get_by_id(country_id=country_id)

        if country is None:
            return {"message": "country id nont found"}, HTTPStatus.NOT_FOUND
        
        return {"data": [country.data()]}, HTTPStatus.OK
