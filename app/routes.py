from app import flask_app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from datetime import datetime


@flask_app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@flask_app.route("/")
@flask_app.route("/index")
def index():
    return render_template('index.html')

@flask_app.route("/login")
def login():
    return render_template('login.html')

@flask_app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))