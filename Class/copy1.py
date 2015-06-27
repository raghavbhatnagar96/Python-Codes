class Rect():
	def __init__(self,h,w,x,y):
		self.x = x
		self.y = y
		self.h = h
		self.w = w
	def copy(self):
		return(self.h,self.w)
p1=Rect(100,150,2,3)
p2=p1.copy()
if(p1==p2):
	print True
else:
	print False

