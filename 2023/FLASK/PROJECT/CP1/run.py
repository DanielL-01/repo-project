from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "ILOVEYOU3000"  

app.config["SQLAlchemy_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#FLASK ORM - SQLAlchemy
class User(db.model):
    id = db.Column(db.integer, primary_key=True)
    username = db.COlumn(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default="default.jpg")
    password = db.Column(db.String(100), nullable=False)

    tweets = db.relationship('Tweet', backred='author', lazy=True)

class Tweet(db.Model):
    id = db.Column(db.integer, primary_key=True)
    date_posted = de.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Tect, nullable=False)
    user_id = db.Column(db.interger, db.FOreignKey('user.id'), nullable=False)

#FLASK FORM
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=(DataRequired(), Length(min=2, max=20)))
    email = StringField('Email', validators=(DataRequired(), Email()))
    password = PasswordField('Password', validators=(DataRequired()))
    confirm_password = PasswordField('Confirm Password', validators=(DataRequired(), EqualTo()))
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=(DataRequired(), Email()))
    password = PasswordField('Password', validators=(DataRequired()))
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

tweets = [
    {
        'author': 'Budi Doremi',
        'content': 'This is my first tweet',
        'date_posted': 'May 10, 2022'
    },
    {
        'author': "Alex Chandra",
        'content': "Hello World",
        'date_posted': "May 11, 2022"
    }
]

@app.route("/") #127.0.0.1:8000
@app.route("/home")
def home():
    return render_template("home.html", tweets=tweets)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_lenght=16)
        user= User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "Success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Login Success", "info")
            return redirect(url_for("home"))
        flash("Login Failed, please check your username and password", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/about")
def about():
    return render_template("about.html", title="About us")

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    return True

if __name__ == "__main__":
    app.run(debug=True)
