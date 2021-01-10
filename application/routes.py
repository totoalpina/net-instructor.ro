from flask import render_template, redirect, url_for, flash
from application import app, db, login_manager, mail
from application.models import LoginForm, SignupForm, Login, Clienti, CursantNouForm
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

s = URLSafeTimedSerializer('SECRET_KEY')

@login_manager.user_loader
def load_user(login_id):
    return Login.query.get(int(login_id))

@app.route('/', methods=['GET','POST'])
def index():
    an_curent = datetime.now()
    return render_template('index.html', an_curent=an_curent)


@app.route('/logare', methods=['GET','POST'])
def logare():
    form = LoginForm()
    an_curent = datetime.now()
    if form.validate_on_submit() :
        utilizator = Login.query.filter_by(utilizator=form.utilizator.data).first()
        print( [utilizator])

        if utilizator:
            if check_password_hash(utilizator.parola, form.parola.data) and utilizator.activ == 1:
                login_user(utilizator)
                flash("V-ati logat cu succes")

                return redirect(url_for('clienti'))

            elif not check_password_hash(utilizator.parola, form.parola.data):

                flash ( "Parola introdusa nu este corecta. Incercati din nou" )
                return redirect(url_for('logare'))

            else :

                flash("Contul dumneavoastra nu este activ !!! Contactati-ne pentru a verifica situatia contului.")
            return redirect(url_for('index'))

        flash("Nu aveti dreptul de a folosi aceasta sectiune. Creati-va in cont pentru a pute intra !")
    return render_template("logare.html", form=form, an_curent=an_curent)

@app.route('/cont_nou', methods=['GET','POST'])
def cont_nou():
    form = SignupForm()
    an_curent = datetime.now()
    if form.validate_on_submit():
        hased_parola = generate_password_hash(form.parola.data, method='sha256' )
        utilizator_nou = Login(nume=form.nume.data, prenume=form.prenume.data, utilizator=form.utilizator.data, email=form.email.data,
                              data_adaugare=datetime.now(), data_modificare=datetime.now(), parola=hased_parola)
        if form.parola.data == form.confirma_parola.data:
            db.session.add(utilizator_nou)
            db.session.commit()
            email=utilizator_nou.email
            token = s.dumps(email, salt='confirmare_email')

            msg = Message('Confirmare Email', sender='totoalpina@gmail.com', recipients=[email])
            link = url_for('confirmare_email', token=token, _external=True)
            msg.body = """\n    Va multumim pentru inregistrare ! Pentru a va activa contul creat pe site-ul nostru accesati linkul de mai jos. \n
        \n
    Accesati acest link pentru activare cont: \n    {}""".format(link)

            mail.send(msg)
            flash("Contul a fost creat ! Accesati adresa de mail cu care v-ati inregistrat pentru a activa contul")
            return redirect(url_for('index'))
        else:
            flash("Parola nu este identica, incercati din nou !")
        return redirect(url_for('cont_nou'))
    return render_template('cont_nou.html', form=form, an_curent=an_curent)

@app.route('/confirmare_email/<token>')
def confirmare_email(token):
    try:
        email = s.loads(token, salt='confirmare_email', max_age=3600)
        print('verificare' + email)
        user = db.session.query(Login).filter(Login.email == email).one()
        user.activ = 1
        db.session.commit()

        flash("Contul a fost activat ! Folositi credentialele salvate in cont pentru a va loga in aplicatie !")
        return redirect(url_for('logare'))
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'
    return redirect(url_for('logare'))

@app.route('/clienti', methods=['GET','POST'])
@login_required
def clienti():
    an_curent = datetime.now()
    form = Clienti.query.order_by('id')
    return render_template("clienti.html", an_curent=an_curent, form = form)

@app.route('/adauga_cursant', methods=['GET','POST'])
@login_required
def adauga_cursant():
    an_curent=datetime.now()
    form = CursantNouForm()
    return render_template("adauga_cursant.html", form=form, an_curent=an_curent)

@app.route('/cursant', methods=['GET','POST'])
@login_required
def cursant():
    form = CursantNouForm()
    an_curent = datetime.now()
    if form.validate_on_submit:
        cursant_nou = Clienti(nume=form.nume.data, prenume=form.prenume.data, categorie_scolarizare=form.categorie_scolarizare.data,
                                     localitate=form.localitate.data, adresa=form.adresa.data, email=form.email.data,
                                     telefon=form.telefon.data, data_adaugare=datetime.now(), data_modificare=datetime.now(),
                                     observatii=form.observatii.data, activ=1)
        db.session.add(cursant_nou)
        db.session.commit()
        return redirect(url_for('clienti'))
    return render_template("adauga_cursant.html", form=form, an_curent=an_curent)



@app.route('/contact')
def contact():
    an_curent = datetime.now()
    return render_template("contact.html", an_curent=an_curent)

@app.route('/sterge_cursant/<int:id>')
@login_required
def sterge_cursant(id):
    to_delete = Clienti.query.filter_by(id=id).first()
    db.session.delete(to_delete)
    db.session.commit()
    flash("Cursant sters cu succes")
    return redirect(url_for('clienti'))

@app.route('/delogare')
@login_required
def delogare():
    logout_user()
    flash("Sesiune inchisa cu succes")
    return redirect(url_for('index'))