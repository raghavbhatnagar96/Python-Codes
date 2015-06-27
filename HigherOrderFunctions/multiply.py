def f(x):
	def g(y):
		return x*y
	return g
multiply = f(2)
print multiply(3)


