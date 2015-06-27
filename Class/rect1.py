class Rectangle():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def moverectangle(self,p):
		return(self.x+p.x,self.y+p.y)
p1=Rectangle(1,3)
p2=Rectangle(2,4)
p3=p1.moverectangle(p2)
print p3
