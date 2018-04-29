def last_fibonaci(last_fib, b=1, a=0):
	if b >= last_fib:
		print(a, b - a)
		return

	last_fibonaci(last_fib, b=a + b, a=b)


print("/////////////////////")
last_fibonaci(6765)
print("/////////////////////")
last_fibonaci(6768)
print("/////////////////////")
last_fibonaci(100000)
