import bcrypt
from flask import url_for, render_template, request, flash, redirect
from flask_login import login_user, current_user, login_required, logout_user

from app import app, login_manager, app_funcs
from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = True if request.form.get('remember-me') else False
        app_funcs.login(email, password, remember_me)
    
    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully signed out ", "success")
    return redirect(url_for('login'))


@app.route("/profile", methods=['GET'])
@login_required
def profile():
    return render_template("profile.html")
