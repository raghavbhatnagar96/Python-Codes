class Rectangle():
	def __init__(self,w,h):
		self.w = w
		self.h = h
	def pri(self,p):
		return(self.w+p.w/2,self.h+p.h/2)
p1=Rectangle(100,200)
p2=Rectangle(0,0)
p3=p1.pri(p2)
print p3
