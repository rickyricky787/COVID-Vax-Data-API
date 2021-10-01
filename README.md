# COVID-Vax-Data-API
This API contains COVID-19 vaccination data from accross the globe, collected from [Our World In Data](https://github.com/owid/covid-19-data).
The data was cleaned, normalized, and added to a database in order to create this API.
This API project is a small extension to a [previous project](https://github.com/rickyricky787/Vaccination-Impact), done solely for the purpose to practice writing API's.
The data in this API is automatically updated daily with the use of AWS Lambda. The code used for cleaning, normalizing, and auto-updating the database can be found [here](https://github.com/rickyricky787/Vaccination-Impact/tree/main/lambda_files).

API routes are available at the API homepage.

API homepage: https://covid-vax-data-api.herokuapp.com/

# Tech Stack
- Frontend: HTML, CSS (Used stackedit.io to create home page)
- Backend: Python (Flask), AWS RDS (MySQL)
- Data Analysis Tools: Pandas, Numpy (Used for cleaning and normalizing data)
- AWS Lambda used to auto scrape data from source, normalize data, and update the database daily.
- Deployed on Heroku
