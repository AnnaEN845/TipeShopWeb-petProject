from flask import url_for, render_template, request, flash, redirect
from flask_login import login_required, current_user

from app import app, login_manager, app_funcs
from app.models import User
from loguru import logger

logger.add("logger.log")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        if not app_funcs.user_login():
            flash('Email or password is not correct', 'error')
        else:
            return redirect(request.args.get("next") or url_for("profile"))
    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    app_funcs.user_logout()
    return redirect(url_for('login'))


@app.route("/profile", methods=['GET'])
@login_required
def profile():
    logger.info(f'User {current_user.email} has looked at his profile')
    return render_template("profile.html")
