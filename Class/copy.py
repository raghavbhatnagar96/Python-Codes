class Rectangle():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def copy(self):
		return(self.x,self.y)
p1=Rectangle(3,4)
p2=p1.copy()
print p2
	
