import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_mail import Mail, Message
from forms import ContactForm
from helper import pages, social_media

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = os.getenv('MAIL_PORT')
MY_EMAIL = os.getenv('MY_EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

app = Flask(__name__)
app.secret_key = SECRET_KEY

mail = Mail()
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = MY_EMAIL
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
mail.init_app(app)


#   Main Page
@app.route('/')
def index():
    return render_template("index.html", pages=pages, social_media=social_media)

#   Adventures Landing Page
@app.route('/adventures')
def adventures():
    return render_template('adventures.html', pages=pages, social_media=social_media)

#   Music Landing Page
@app.route('/music')
def music():
    return render_template('music.html', pages=pages, social_media=social_media)

#   Projects Landing Page
@app.route('/projects')
def projects():
    return render_template('projects.html', pages=pages, social_media=social_media)

#   About Landing Page
@app.route('/about')
def about():
    return render_template('about.html', pages=pages, social_media=social_media)

#   Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    sent = False
    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        sent = True

        subject = contact_form.subject.data
        name = contact_form.name.data
        user_email = contact_form.email.data
        message = contact_form.message.data

        #   Email from user to be sent to my account
        user_message = Message(subject, sender=MY_EMAIL, recipients=[MY_EMAIL])

        user_message.body = """
        From: {0} - ({1}):

        {2}

        """.format(name, user_email, message)

        #   Email to the user confirming that their message was sent
        confirmation_email = Message('Confirmation - Thank you for getting in touch', sender=MY_EMAIL, recipients=[user_email])

        confirmation_email.body = """
        Thank you for getting in touch!

        You should hopefully receive a reply within the next few days. I will try to address any questions or comments that you may have.  Feel free to explore the site in the meantime.

        Have a great day!
        -Ian

        -----------YOUR MESSAGE-----------

        {0}

        """.format(message)

        mail.send(user_message)
        mail.send(confirmation_email)

        redirect(url_for('contact', sent=sent, _external=True, _scheme='https'))

    return render_template('contact.html', contact_form=contact_form, pages=pages, social_media=social_media, sent=sent)
