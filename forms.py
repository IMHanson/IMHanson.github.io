from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")


#####   Delete this! #####
mail_server = 'smtp.gmail.com'
mail_port = 465
my_email = 'imhanson91@gmail.com'
email_password = 'frrgqmgcbanhkbnq'