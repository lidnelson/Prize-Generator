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
	prize_id =  randint(1,1000)
	if 990<prize_id<=1000:
		prize_name="You've won £1,000,000"
	elif 975<prize_id<=990:
		prize_name="you've won £250,000"
	elif 955<prize_id<=975:
		prize_name="you've won £50,000"
	elif 930<prize_id<=955:
		prize_name="you've won £25,000"
	elif 900<prize_id<=930:
		prize_name="you've won £20,000"
	elif 865<prize_id<=900:
		prize_name="you've won £10,000"
	elif 825<prize_id<=865:
		prize_name="you've won £5,000"
	elif 780<prize_id<=825:
		prize_name="you've won £1,000"
	elif 700<prize_id<=780:
		prize_name="you've won £500"
	elif 615<prize_id<=700:
		prize_name="you've won £200"
	elif 525<prize_id<=615:
		prize_name="you've won £100"
	elif 430<prize_id<=525:
		prize_name="you've won £50"
	elif 330<prize_id<=430:
		prize_name="you've won £20"
	elif 225<prize_id<=330:
		prize_name="you've won £10"
	elif 115<prize_id<=225:
		prize_name="you've won £5"
	else:
		prize_name="you've won a pack of Haribos"
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