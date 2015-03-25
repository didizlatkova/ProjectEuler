# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

maxChain = 0
maxNumber = 0
limit = 1000000
knownChains = {}

for i in range(2, limit):
	number = i
	count = 1
	while (number != 1):
		if (number in knownChains):			
			count += knownChains[number] - 1
			break

		count += 1
		if (number % 2 == 0):
			number = number / 2
		else:
			number = 3*number + 1		

	if (i not in knownChains):
		knownChains[i] = count

	if (count > maxChain):
		maxChain = count
		maxNumber = i

print(maxNumber)