from email_validator import validate_email, EmailNotValidError
from flask import flash

def validare_mail(args):
    try :
        valid = validate_email ( args )
        args = valid.email
    except EmailNotValidError as e :
        flash ( "Email-ul introdus nu este valid. Introduceti un email valid de forma : email@email.com !" )