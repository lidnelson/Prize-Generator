from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY']='f9bf78bavdwvwefveavecd2b0b86df9da'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.189.82.67/Prizes'

db = SQLAlchemy(app)



from app import routes
