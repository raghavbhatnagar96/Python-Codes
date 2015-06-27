n=input("Enter the number of numbers")
r = []
count = 0
while count<n:
	number = input("Enter number")
	count = count + 1
	r.append(number)
def max(r):
	max = r[0]
	for elm in r[1: ]:
		if elm>max:
			max = elm
			return max
print "the max is",max(r)
	


	
