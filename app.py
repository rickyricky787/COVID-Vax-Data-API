from flask import Flask
from flask_restful import Api

from config import Config
from extensions import db

from resources.continent import ContinentResource, ContinentIdResource
from resources.country import CountryResource, CountryIdResource
from resources.covid_data import CovidDataResource, CountryCovidDataResource, LatestCovidDataResource, LatestCountryCovidDataResource
from resources.daily_vaccination import DailyVaccinationResource, CountryDailyVaccinationResource, LatestDailyVaccinationResource, LatestCountryDailyVaccinationResource
from resources.total_vaccination_by_brand import TotalVaccinationByBrandResource, CountryTotalVaccinationByBrandResource
from resources.vaccine_brand_in_country import VaccineBrandInCountryResource, CountryVaccineBrandInCountryResource, VaccineVaccineBrandInCountryResource
from resources.vaccine import VaccineResource, VaccineIdResource

def register_extensions(app):
    db.init_app(app)

def register_resources(app):
    api = Api(app)

    api.add_resource(ContinentResource, "/continent")
    api.add_resource(ContinentIdResource, "/continent/id/<int:continent_id>")

    api.add_resource(CountryResource, "/country")
    api.add_resource(CountryIdResource, "/country/id//<int:country_id>")

    api.add_resource(CovidDataResource, "/covid-data")
    api.add_resource(CountryCovidDataResource, "/covid-data/country/<string:country_name>")
    api.add_resource(LatestCovidDataResource, "/covid-data/latest")
    api.add_resource(LatestCountryCovidDataResource, "/covid-data/latest/<string:country_name>")

    api.add_resource(DailyVaccinationResource, "/daily-vax")
    api.add_resource(CountryDailyVaccinationResource, "/daily-vax/country/<string:country_name>")
    api.add_resource(LatestDailyVaccinationResource, "/daily-vax/latest")
    api.add_resource(LatestCountryDailyVaccinationResource, "/daily-vax/latest/<string:country_name>")

    api.add_resource(TotalVaccinationByBrandResource, "/total-vax-brand")
    api.add_resource(CountryTotalVaccinationByBrandResource, "/total-vax-brand/country/<string:country_name>")

    api.add_resource(VaccineBrandInCountryResource, "/vax-in-country")
    api.add_resource(CountryVaccineBrandInCountryResource, "/vax-in-country/country/<string:country_name>")
    api.add_resource(VaccineVaccineBrandInCountryResource, "/vax-in-country/vaccine/<string:vaccine_name>")

    api.add_resource(VaccineResource, "/vaccine")
    api.add_resource(VaccineIdResource, "/vaccine/id/<int:vaccine_id>")

app = Flask(__name__)
app.config.from_object(Config)

register_extensions(app)
register_resources(app)

if __name__ == "__main__":
    app.run()