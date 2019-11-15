from app import app, db
import random
from random import randint
import string
from flask import render_template, Flask, url_for, redirect
from app.forms import Name
from app.models import Prizes
import json
import boto3

sol = boto3.client('lambda', region_name='eu-west-1')

@app.route("/", methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
	form = Name()
	prize_name = sol.invoke(FunctionName='randomprize', InvocationType='RequestResponse')
	ref = json.loads(prize_name['Payload'].read().decode('utf-8'))

	randomnumbers = sol.invoke(FunctionName='randomnumber', InvocationType='RequestResponse') 
	ref2 = json.loads(randomnumbers['Payload'].read().decode('utf-8'))

	randomletters = sol.invoke(FunctionName='randomletter', InvocationType='RequestResponse')
	ref3 = json.loads(randomletters['Payload'].read().decode('utf-8'))
	unique_id = str(ref2) + str(ref3)

	if form.validate_on_submit():
		User = Prizes(
			firstname = form.firstname.data.capitalize(),
			lastname = form.lastname.data.capitalize(),
			uniqueid = unique_id,
			prize = ref)

		db.session.add(User)
		db.session.commit()
		temp = Prizes.query.filter_by(uniqueid=unique_id).first()
		return redirect(url_for('spin', id=temp.id))
	return render_template('home.html', title='Home', form=form)

@app.route('/spin/<int(min=1):id>')
def spin(id):
	temp = Prizes.query.filter_by(id=id).first()
	return render_template('spin.html', title='Spin', spin=temp)
