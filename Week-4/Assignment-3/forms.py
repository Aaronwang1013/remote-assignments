from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField
from wtforms.validators import (DataRequired, ValidationError, Email)

# import db
from models import Database
# form: form self, field: argument


def email_exists(form, field):
    cursor = Database()
    query = "SELECT id FROM user WHERE email =%s"
    # will return None if nothing match
    #print({field.data})
    result = cursor.queryone(query, (field.data,))
    if result is not None:
        raise ValidationError("Email already Existed")


# combine two from in on class, use action to check rather is for sign in or sign up
class SignUnForm(FlaskForm):
    email = StringField(
        # access by field.label.text
        'Email',
        # form.validate_on_submit() will check all these stuff
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ])
    # this will be used to classify if it is a sign up or sign in request
    action = HiddenField(
        default="signup"
    )


class SignInForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    action = HiddenField(
        default="signin"
    )
