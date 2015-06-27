class Rectangle:
	def __inti__(self,x,y):
		self.x = x
		self.y = y
	def area(self):
		return Rectangle(self.x*self.y)
	def perimeter(self):
		return Rectangle(2*(self.x+self.y))
if __name__ == "__main__":
	p1 = Rectangle(1,3)
	p2 = p1.area()
	p3 = p1.perimeter()
	print "("+str(p2)+")"
	print "("+str(p3)+")"
