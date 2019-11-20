import random
def lambda_handler(event, context):
	letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
	random_letter=''
	for i in range(6):
        	random_letter += letter[random.SystemRandom().randint(0,25)].upper()
    	return random_letter
