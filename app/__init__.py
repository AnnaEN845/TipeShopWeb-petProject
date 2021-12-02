from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdjhfghjsdgfjhgjdshgfjh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_20:123@159.69.151.133:5056/user_20_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Log in to access"
login_manager.login_message_category = "success"

from app import models, views
