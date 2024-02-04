from flask import Flask
import os
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import request
from flask_bcrypt import check_password_hash
import forms
import models
from configparser import ConfigParser



app = Flask(__name__)
# for csrf configuration
config_object = ConfigParser()
config_object.read("config.ini")
SECRET_KEY = config_object["SECRET_KEY"]
app.secret_key = SECRET_KEY["secret_key"]


# home page, for both sign and sign up
@app.route('/', methods=('GET', 'POST'))
def index():
    # this will run all the validation we define in forms.py
    signupform = forms.SignUnForm()
    signinform = forms.SignInForm()
    # if the form has been sent
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'signup':
            if signupform.validate_on_submit() == True :   
                # if the email is valid, mean there is no match email in db
                # add the email and password in db and redirect to mamber page  
                flash("Sign Up successful", "success")
                cursor = models.Database()
                cursor.create_user(email=signupform.email.data,
                                password=signupform.password.data)
                return redirect(url_for('member_page', user_email=signupform.email.data))
            else:
                flash("Email already existed", "error")
        if action == "signin" and signinform.validate_on_submit():
            # if the request is for signing in
            cursor = models.Database()
            userinfo = cursor.queryone(
                "SELECT email, password FROM user WHERE email = (%s)",
                (signinform.email.data,)
            )
            # if userinfo is not None mean there is a match in db
            if userinfo is not None:
                # db_password is the password store in db
                db_password = userinfo['password']
                password = signinform.password.data
                # check if password match
                # remember to use generate_password_hash when insert
                if check_password_hash(db_password, password): 
                    return redirect(url_for('member_page', user_email=signinform.email.data))
            else:
                flash("Invalid email or password", "error")
    return render_template('index.html', signupform=signupform, signinform=signinform)


@app.route('/member_page')
def member_page():
    user_email = request.args.get("user_email", "")
    return render_template('member_page.html', user_email=user_email)


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')
