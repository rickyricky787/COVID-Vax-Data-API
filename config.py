import os
from dotenv import load_dotenv, find_dotenv

class Config:
    DEBUG = False

    # To get keys from .env files
    load_dotenv(find_dotenv())
    USERNAME = os.environ.get("USER_NAME")
    PASSWORD = os.environ.get("PASSWORD")
    ENDPOINT = os.environ.get("ENDPOINT")
    DB_INSTANCE = os.environ.get("DB_INSTANCE")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{ENDPOINT}/{DB_INSTANCE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False