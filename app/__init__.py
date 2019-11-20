from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config

app = Flask(__name__)

app.config['SECRET_KEY'] = config.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri

db = SQLAlchemy(app)



from app import routes
