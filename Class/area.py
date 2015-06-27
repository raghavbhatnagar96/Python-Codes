class Rectangle:
	def __inti__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		return point(self.x*self.y)
	def perimeter(self):
		return point(2*(self.x+self.y))
if __name__ == "__main__"
	p1 = point(1,3)
	p3 = p1.area()
	p4 = p1.perimeter()
	print "("+str(p3)+")"
	print "("+str(p4)+")"
