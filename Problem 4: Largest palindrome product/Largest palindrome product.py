# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def isPalindrome(number):
	stringNumber = number.__str__()
	for i in range(int(math.floor(len(stringNumber)/2))):
		if stringNumber[i] != stringNumber[len(stringNumber) - i - 1]:
			return Falses
	return True

maxes = []
for i in range(999, 99, -1):	
	for j in range(i, 9, -1):
		if isPalindrome(i*j):
			maxes.append(i*j)
			break

print(max(maxes))

