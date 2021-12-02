import bcrypt
from flask_login import login_user
from flask import redirect, url_for, request, flash

from app.models import User


def login(email, password, remember_me):
	user = User.query.filter_by(email=email).first()
	if user and str.encode(user.password) == bcrypt.hashpw(str.encode(password), str.encode(user.salt)):
		login_user(user, remember=remember_me)
		return redirect(request.args.get("next") or url_for("profile"))
	else:
		flash('Email or password is not correct', 'error')