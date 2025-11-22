import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mi_clave_secreta')

    DB_HOST = os.getenv('MYSQL_ADDON_HOST')
    DB_USER = os.getenv('MYSQL_ADDON_USER')
    DB_PASSWORD = os.getenv('MYSQL_ADDON_PASSWORD')
    DB_NAME = os.getenv('MYSQL_ADDON_DB')
    DB_PORT = int(os.getenv('MYSQL_ADDON_PORT', 3306))
