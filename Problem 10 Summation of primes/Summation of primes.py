# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

arr = [True for x in range(2000000)]
sum = 0

for i in range(2, len(arr)):
	if arr[i]:
		sum += i
		for j in range(i, len(arr), i):
			arr[j] = False

print(sum)
