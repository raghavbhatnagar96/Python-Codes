n = input("Enter number1")
m = input("Enter number2")
count = 0
count1 = 0
a = []
b = []
while count<n:
	num = input("Enter the number")
	a.append(num)
	count = count + 1
while count1<n:
	num1 = input("Enter the num")
	b.append(num1)
	count1 = count1 + 1
def common(a,b):
	r = []	
	for i in a:
		if  i in b:
			r.append(i)

	return r
print "ans is",common(a,b)
