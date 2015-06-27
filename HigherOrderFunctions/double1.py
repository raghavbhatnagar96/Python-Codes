def dbl(d,l):
	r = []
	for i in l:
		r.append(d(i))
	return r
def double(l):
	def dl(x):
		return 2*x
	return dbl(dl,l)
def sums(l):
	def sum(x):
		return 2+x
	return dbl(sum,l)
def length(l):
	def leng(x):
		return len(x)
	return dbl(leng,l)
a = [1,2,3]
c = ['aa','ddddddd','llllllllll']
print double(a)
print sums(a)
print length(c)
