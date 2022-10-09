import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world-server-hc.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello-world-db-hc'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@ssword1234'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'hcfirststorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'rk4xCuUyjKjgGZJJe5vfJ7/Rp+eK6CNbiOB3+P9iIIQC1+ItAlM2mKf28BN/JuvLwjz/JSVTVD+6+AStjU+dNQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
