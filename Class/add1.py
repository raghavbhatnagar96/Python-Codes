def getx(P):
	return p[1]
def gety(p):
	return p[2]
def makepoint(x,y):
	return (x,y)
def add(p1,p2):
	return makepoint(getx(p1)+getx(p2),gety(p1)+gety(p2))
p1=(1,2)
p2=(3,4)
print add(p1,p2)
