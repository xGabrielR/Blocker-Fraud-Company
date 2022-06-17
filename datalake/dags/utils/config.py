import os
#from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv()) # Dotenv do not work on Docker Compose Airflow!!

class getInfos():
    def __init__(self):
        self.H_DB = os.getenv('H_DB')
        self.H_DB_HOST = os.getenv('H_DB_HOST')
        self.H_DB_PORT = os.getenv('H_DB_PORT')
        self.H_DB_USER = os.getenv('H_DB_USER')
        self.H_DB_PASS = os.getenv('H_DB_PASS')

        self.MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT')
        self.MINIO_HOST = os.getenv('MINIO_HOST')
        self.ACCESS_KEY = os.getenv('ACCESS_KEY')
        self.SECRET_KEY = os.getenv('SECRET_KEY')