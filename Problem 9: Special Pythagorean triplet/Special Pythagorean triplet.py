# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

start = 200
end = 400
tripletSum = 1000

for a in range(start, end + 1):
	for b in range(a, end + 1):
		if (tripletSum - a - b == math.sqrt(a*a + b*b)):
			print(a * b * (tripletSum - a - b))
			break