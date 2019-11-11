import random
import string
from random import randint

def randomString(stringLength=5):
    #Generate a random string of fixed length
    letters = string.ascii_uppercase

    return ''.join(random.choice(letters) for i in range(stringLength))

randomletters = str(randomString(5))

print ("Random String is:", randomletters)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1

    return randint(range_start, range_end)

randomnumbers = str(random_with_N_digits(3))

print ("Random Number is:", randomnumbers)

print ("Your unique ID is:", randomnumbers + randomletters)
