# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def isPrime(number):
	factor = int(math.sqrt(number))
	while (factor > 0 and number % factor is not 0):
		factor -= 1

	if (factor is 1):
		return True
	return False

number = 600851475143
factor = int(math.sqrt(number))

while number % factor is not 0 or not isPrime(factor):
	factor -= 1

print(factor)
