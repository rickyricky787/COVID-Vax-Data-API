from flask_restful import Resource
from http import HTTPStatus

from models.continent import Continent

class ContinentResource(Resource):
    def get(self):
        continents = Continent.get_all()
        data = []
        
        for continent in continents:
            data.append(continent.data())
        
        return {"data": data}, HTTPStatus.OK

class ContinentIdResource(Resource):
    def get(self, continent_id):
        continent = Continent.get_by_id(continent_id=continent_id)

        if continent is None:
            return {"message": "continent id nont found"}, HTTPStatus.NOT_FOUND
        
        return {"data": [continent.data()]}, HTTPStatus.OK
