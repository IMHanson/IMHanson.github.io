from flask import Flask, render_template, request, redirect, url_for
from helper import pages, social_media, contact_inbox
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
    return render_template("index.html", pages=pages, social_media=social_media)


@app.route('/adventures')
def adventures():
    return render_template('adventures.html', pages=pages, social_media=social_media)

@app.route('/music')
def music():
    return render_template('music.html', pages=pages, social_media=social_media)

@app.route('/projects')
def projects():
    return render_template('projects.html', pages=pages, social_media=social_media)

@app.route('/about')
def about():
    return render_template('about.html', pages=pages, social_media=social_media)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    sent = False
    contact_form = ContactForm(csrf_enabled=False)
    
    if contact_form.validate_on_submit():
        message_id = 'message #' + str(0000 + len(contact_inbox) + 1)
        sent = True

        contact_inbox[message_id] = {
            'name': contact_form.name.data,
            'email': contact_form.email.data,
            'subject': contact_form.subject.data,
            'message': contact_form.message.data
        }

        print(contact_inbox)

        redirect(url_for('contact', sent=sent, _external=True, _scheme='https'))
    
    return render_template('contact.html', contact_form= contact_form, pages=pages, social_media=social_media, sent=sent)
