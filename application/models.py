from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, DateTimeField, IntegerField, SelectField, TextAreaField

from wtforms.validators import InputRequired, Email, Length
from application import db
from flask_login import LoginManager, UserMixin


class Login(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nume = db.Column(db.String(40))
    prenume = db.Column(db.String(40))
    utilizator = db.Column(db.String(30))
    email = db.Column(db.String(50))
    parola = db.Column(db.String(80))
    data_adaugare = db.Column(db.DATETIME())
    data_modificare = db.Column(db.DATETIME())
    activ = db.Column(db.Integer, default=0)


class LoginForm(FlaskForm):
    utilizator = StringField('utilizator', validators=[InputRequired(), Length(min=4, max=30)])
    parola = PasswordField('parola', validators=[InputRequired(), Length(min=6,max=25)])


class SignupForm(FlaskForm):
    utilizator = StringField('utilizator', validators=[InputRequired(), Length(min=4, max=30)])
    nume = StringField('nume', validators=[InputRequired(), Length(max=40)])
    prenume = StringField('prenume', validators=[InputRequired(), Length(max=40)])
    parola = PasswordField('parola', validators=[InputRequired(), Length(min=6,max=25)])
    confirma_parola = PasswordField('confirma_parola', validators=[InputRequired(), Length(min=6,max=25)])
    email = StringField('email', validators=[Email(), InputRequired()])

class CursantNouForm(FlaskForm):
    nume = StringField('nume', validators=[Length(max=50)])
    prenume = StringField('prenume', validators=[Length(max=50)])
    localitate = StringField('localitate', validators=[Length(max=50)])
    adresa = StringField('adresa', validators=[Length(max=250)])
    categorie_scolarizare = SelectField('categorie_scolarizare', choices=[('A','A'), ('B','B')])
    email = StringField('email', validators=[Email(), Length(max=50)])
    telefon = StringField('telefon', validators=[Length(max=13)])
    data_adaugare = DateTimeField('data_adaugare')
    data_modificare = DateTimeField('data_modificare')
    activ = IntegerField('activ', validators=[Length(max=1)])
    observatii = StringField('observatii', validators=[Length(max=350)])

class Clienti(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nume = db.Column(db.String(50))
    prenume = db.Column(db.String(50))
    localitate = db.Column(db.String(50))
    adresa = db.Column(db.String(250))
    categorie_scolarizare = db.Column(db.String(10))
    email = db.Column(db.String(50))
    telefon = db.Column(db.String(13))
    data_adaugare = db.Column(db.DATETIME())
    data_modificare = db.Column(db.DATETIME())
    activ = db.Column(db.Integer, default=0)
    observatii = db.Column(db.String(350))
    
    def __init__(self, nume, prenume, localitate, adresa, categorie_scolarizare, email, telefon, data_adaugare, data_modificare, activ, observatii):
        self.nume = nume
        self.prenume = prenume
        self.localitate = localitate
        self.adresa = adresa
        self.categorie_scolarizare = categorie_scolarizare
        self.email = email
        self.telefon = telefon
        self.data_adaugare = data_adaugare
        self.data_modificare = data_modificare
        self.activ = activ
        self.observatii = observatii

class ContactMe(FlaskForm):
    nume = StringField('nume', validators=[InputRequired(), Length(max=40)])
    email = StringField ( 'email', validators = [ Email ( ), InputRequired ( ) ] )
    telefon = StringField('telefon', validators=[InputRequired(), Length(max=25)])
    mesaj = TextAreaField('mesaj', render_kw={"rows": 6, "cols": 52}, validators=[InputRequired(), Length(max=500)])
