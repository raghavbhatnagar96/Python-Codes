def myfilter(f,l):
	return filter(f,l)
def is_odd(l):
	def odd(x):
		if(x%2==1):
			return x
	return myfilter(odd,l)
def is_even(l):
	def even(x):
		if(x%2==0):
			return x
	return myfilter(even,l)
def is_end(l):
	def end(x):
		if(x[-1:-3]=='ing'):
			return x
	return myfilter(end,l)
a = [1,2,3]
b = ['eeeing','adadadd','sdsding']
print is_odd(a)
print is_even(a)
print is_end(b)
