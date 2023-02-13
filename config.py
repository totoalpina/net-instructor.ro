from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

class Config(object):
    SECRET_KEY = 
    MAIL_SERVER = 
    MAIL_USERNAME = 
    MAIL_PASSWORD = 
    MAIL_PORT = "587"

    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # MAIL_PORT = os.environ.get('MAIL_PORT')
    # MAIL_USE_TLS = True

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:<pass>@localhost:3306/net_instructor"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    PERMANENT_SESSION_LIFETIME = timedelta ( minutes = 20 )
    SESSION_REFRESH_EACH_REQUEST = True
    
    SQLALCHEMY_TRACK_MODIFICATIONS = True
