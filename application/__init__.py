from flask import Flask
from config import Config
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta


app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = b"\x8a{\x9e\x02\xbfo\\\xc0\x1a\xff'\x86\xe5\x8e\xf4\xbf"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)
app.config['SESSION_REFRESH_EACH_REQUEST'] = True
bootstrap = Bootstrap(app)
mail = Mail(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'


from application import routes