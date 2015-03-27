# Find the sum of the digits in the number 100!

def factorial(x):
	if (x==1):
		return 1
	return x * factorial(x-1)

f = factorial(100)
print(sum(map(int,str(f))))
