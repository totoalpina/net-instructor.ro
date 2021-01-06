from flask_sqlalchemy import SQLAlchemy


class Config(object):
    MAIL_SERVER = 'mail.zenic.ro'
    MAIL_USERNAME = 'cosmin@zenic.ro'
    MAIL_PASSWORD = 'Armand27Octombrie'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:783326@localhost/net_instructor'
    # SQLALCHEMY_BINDS = {
    #     'user' : 'mysql://root:783326@localhost/user',
    #     'cosmin': 'mysql://root:783326@localhost/user',
    # }
    SQLALCHEMY_TRACK_MODIFICATIONS = True