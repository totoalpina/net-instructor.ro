from flask import Flask
from datetime import timedelta
from flask_mail import Mail


app = Flask(__name__)
app.secret_key = b"\x8a{\x9e\x02\xbfo\\\xc0\x1a\xff'\x86\xe5\x8e\xf4\xbf"
mail = Mail(app)


from application import routes