# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def isPrime(number):
	factor = 2
	while (factor <= int(math.sqrt(number)) and number % factor != 0):
		factor += 1

	if (factor == int(math.sqrt(number)) + 1):		
		return True
	return False

counter = 1
number = 3

while(counter < 10001):
	if isPrime(number):
		counter += 1
	number += 2

print(number - 2)