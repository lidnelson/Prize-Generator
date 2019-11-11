from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError




class Name(FlaskForm):
	firstname = StringField('First Name: ',
		validators = [
			DataRequired(),
			Length(min=2, max=100)
		])
	lastname = StringField('Last Name: ',
		validators = [
			DataRequired(),
			Length(min=2, max=100)
		])
	prizegen = SubmitField("What's My Prize!")