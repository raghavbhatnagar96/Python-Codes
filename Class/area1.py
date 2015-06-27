class Point:
	def __inti__(self,x,y):
		self.x = x
		self.y = y
	def add(self,p):
		return Point(self.x+p.x,self.y+p.y)
	def __str__(self):
		return "Point("+str(self.x)+","+str(self.y)+")"
if __name__ == " __main__ ":
	p1=Point(1,2)
	p2=Point(3,4)
	p3=p1.add(p2)
	p4=p2.add(p3)
	print "(" + str(p3.x) + "," + str(p3.y) + ")"
	print "(" + str(p4.x) + "," + str(p4.y) + ")"
	
