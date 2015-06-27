def dbl(d,l):
	l1=[]
	for v in l:
		l1.append(d(v))
	return l1
def double(l):
	return dbl(lambda x: 2*x,l)
def add(l):
	return dbl(lambda x: 2+x,l)
def leng(l):
	return dbl(lambda x: len(x),l)
a=[1,2,3]
b = ['ss','dddddd','wwwwwwwwwww']
print double(a)
print add(a)
print leng(b)
	
