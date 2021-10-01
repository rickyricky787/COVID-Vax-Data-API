from flask_restful import Resource
from http import HTTPStatus

from models.vaccine import Vaccine

class VaccineResource(Resource):
    def get(self):
        bulk_data = Vaccine.get_all()
        data = []

        for vaccine_data in bulk_data:
            data.append(vaccine_data.data())
        
        return {"data": data}, HTTPStatus.OK

class VaccineIdResource(Resource):
    def get(self, vaccine_id):
        vaccine = Vaccine.get_by_id(vaccine_id=vaccine_id)

        if vaccine is None:
            return {"message": "vaccine id nont found"}, HTTPStatus.NOT_FOUND
        
        return {"data": [vaccine.data()]}, HTTPStatus.OK