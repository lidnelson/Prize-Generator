from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY']='f9bf78bavdwvwefveavecd2b0b86df9da'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sqldatabase:sqldatabase@sqldatabase.calytdhddf4j.eu-west-1.rds.amazonaws.com/Prizes'

db = SQLAlchemy(app)



from app import routes
