def myreduce(f,l,initial):
	acc = initial
	for i in l:
		acc = f(acc,i)
	return acc
def sum(l):
	def add(x,y):
		return x+y
	return myreduce(add,l,0)
def mul(l):
	def mult(x,y):
		return x*y
	return myreduce(mult,l,1)
def conc(l):
	def cont(x,y):
		return x+y
	return myreduce(cont,l,"")

a = [8,2,3]
b = ['s','a','r','a','y','u']
print sum(a)
print mul(a)
print conc(b)
print count(a)	
