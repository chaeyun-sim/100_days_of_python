from email_validator import validate_email
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask import request
from flask_bootstrap import Bootstrap


# def password_length_check(form, field):
#     if len(field.data) >= 8:
#         raise ValidationError('Field must be more than 8 characters')


def check_email(form, field):
    return validate_email(field.data)


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), check_email])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "secret cat"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
