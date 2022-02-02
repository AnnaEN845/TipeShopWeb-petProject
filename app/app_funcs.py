import bcrypt
from flask import flash, request
from flask_login import login_user, current_user, logout_user
from loguru import logger

from app.models import User


def user_login():
	email = request.form.get('email')
	password = request.form.get('password')
	remember_me = True if request.form.get('remember-me') else False
	user = User.query.filter_by(email=email).first()
	if user and str.encode(user.password) == bcrypt.hashpw(str.encode(password), str.encode(user.salt)):
		login_user(user, remember=remember_me)
		logger.info(f'User {email} and psw {password} logged in')
		return True
	else:
		logger.warning(f'User {email} and psw {password} can not be logged in')
		return False


def user_logout():
	user = current_user.email
	logout_user()
	flash("You have successfully signed out ", "success")
	logger.info(f'User {user} has been logged out')