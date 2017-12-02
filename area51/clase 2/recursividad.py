def factorial(n):
	print("*"*n)
	res = n * factorial(n - 1) if n > 0 else 1
	print("*"*n)
	return res

print(factorial(5))

