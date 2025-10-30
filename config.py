import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mi_clave_secreta')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '1234')
    DB_NAME = os.getenv('DB_NAME', 'portfolio_db')
    DB_PORT = int(os.getenv('DB_PORT', 3306))
