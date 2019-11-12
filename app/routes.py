from app import app, db
import random
from random import randint
import string
from flask import render_template, Flask, url_for, redirect
from app.forms import Name
from app.models import Prizes

def random_with_N_digits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)


def randomString(stringLength=5):
	letters = string.ascii_uppercase
	return ''.join(random.choice(letters) for i in range(stringLength))


@app.route("/",  methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
	form = Name()
	prizes = ['£1,000,000', '£500,000', '£500,000', '£250,000', '£250,000', '£250,000',
        '£75,000', '£75,000', '£75,000', '£10,000', '£10,000', '£10,000', '£10,000',
        '£5,000', '£5,000', '£5,000', '£5,000', '£5,000', '£1,000', '£1,000', '£1,000',
        '£1,000', '£1,000', '£1,000', '£500', '£500', '£500', '£500', '£500', '£500',
        '£500', '£500', '£200', '£200', '£200', '£200', '£200', '£200', '£200', '£200',
        '£200', '£200', '£200', '£200', '£200', '£200', '£200', '£100', '£100', '£100',
        '£100', '£100', '£100', '£100', '£100', '£100', '£100', '£100', '£100','£100',
        '£100', '£100', '£100', '£100', '£100', '£100', '£100', '£100', '£100', '£50',
        '£50', '£50', '£50', '£50','£50','£50', '£50','£50','£50','£50', '£50', '£50',
        '£50', '£50', '£50', '£50', '£50','£50', '£50', '£50','£50','£50','£50','£50',
        '£50', '£50','£50','£50','£50','£50', '£20', '£20', '£20', '£20', '£20', '£20',
        '£20', '£20', '£20', '£20','£20','£20','£20','£20', '£20', '£20', '£20','£20',
        '£20', '£20', '£20','£20','£20', '£10', '£10', '£10','£10','£10','£10','£10',
        '£10', '£10', '£10','£10', '£10','£10','£10', '£10','£10','£10', '£10', '£10',
        '£10', '£10', '£10', '£10','£10','£10','£10', '£5', '£5', '£5','£5', '£5','£5',
        '£5','£5','£5', '£5', '£5', '£5', '£5','£5','£5', '£5', '£5', '£5','£5', '£5',
        '£5', '£5', '£5', '£5', '£5', '£5','£5', '£5', '£5','£5','£5','Haribos', 'Haribos',
        'Haribos', 'Haribos','Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos',
        'Haribos', 'Haribos',  'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos',
         'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos',
          'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos', 'Haribos']

	prize_name = (random.choice(prizes))
	
	randomnumbers = str(random_with_N_digits(3))
	randomletters = str(randomString(5))
	unique_id = randomnumbers + randomletters
	if form.validate_on_submit():
		User = Prizes(firstname=form.firstname.data.capitalize(), lastname=form.lastname.data.capitalize(), uniqueid=unique_id, prize=prize_name)
		db.session.add(User)
		db.session.commit()
		temp = Prizes.query.filter_by(uniqueid=unique_id).first()
		return redirect(url_for('spin', id=temp.id))
	return render_template('home.html', title='Home', form=form)


@app.route('/spin/<int(min=1):id>')
def spin(id):
	temp = Prizes.query.filter_by(id=id).first()
	return render_template('spin.html', title="Spin", spin=temp)