from app import db

class Prizes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(30), nullable=False)
	lastname = db.Column(db.String(30), nullable=False)
	uniqueid = db.Column(db.String(150), nullable=False, unique=True)
	prize = db.Column(db.String(150), nullable=False)
