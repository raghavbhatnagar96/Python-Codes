def f(g,l,initial):
	acc = initial;
	for i in l:
		acc = g(acc,i)
	return acc
def sumlist(n):
	def add(x,y):
		return x+y
	return f(add,n,0)
	

def greaterEven(l):
	r = []
	k = []
	for i in l:
		if(i%2==0):
			r.append(i)
		else:
			k.append(i)
	if(sumlist(r)>sumlist(k)):
		return True 
	else:
		return False
print greaterEven([1,2,3,4,4,4,5]) 
