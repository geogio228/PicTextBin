from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "XkCI#U0|v^o1W$yt6"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['UPLOAD_FOLDER'] = 'Static'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
