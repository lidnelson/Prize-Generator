import random
def lambda_handler(event, context):
	random_number = ''
	for n in
        range(3):
		random_number += str(random.randint(0, 9))
	return random_number
