def myreduce(f,l,initial):
	acc = initial
	for i in l:
		acc = f(acc,i)
	return acc
def sum(l):
	return myreduce(lambda x,y:x+y,l,0)
def mul(l):
	return myreduce(lambda x,y:x*y,l,1)
def conc(l):
	return myreduce(lambda x,y:x+y,l,"")
a = [1,2,3]
b = ['a','r','m','i','t','h','a']
print sum(a)
print mul(a)
print conc(b)
