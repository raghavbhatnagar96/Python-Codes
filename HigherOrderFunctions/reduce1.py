def myreduce(g,l,initial):
	acc = initial
	for i in l:
		if(i!=0):
			acc = g(acc,1)
	return acc
def sum(l):
	def add(x,y):
		return x+y
	return myreduce(add,l,0)
a = [1,2,3,4]
print sum(a)
