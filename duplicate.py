n = input("Enter the number of numbers")
count = 0
a = []

while count<n:
	num = input("Enter the number")
	a.append(num)
	count = count + 1
def duplicate(a):
	r = []
	for i in a:
		if i is not in  r:
			r.append(i)
		return r
print"ans is",duplicate(a)
