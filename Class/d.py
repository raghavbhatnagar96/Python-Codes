class Distance:
	def __inti__(self,x,y):
		self.x = x
		self.y = y
	def distancefromorigin(self):
		return Distance(math.sqrt(self.x*self.x+self.y*self.y)
if __name__ == "__main__":
	p1=Rectangle(1,2)
	p2=p1.distancefromorigin()
	print "("+str(p2)+")"
