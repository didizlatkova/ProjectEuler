# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(n1, n2):
	while(n1 != 0):
		if (n1 > n2):
			n1 -= n2
		else:
			saveN1 = n1
			n1 = n2 - n1
			n2 = saveN1
	return n2

def lcm(n1, n2):
	return abs(n1 * n2) / gcd(n1, n2)

print(reduce(lcm, range(2, 20)))