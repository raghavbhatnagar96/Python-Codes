n = input("Enter the number of numbers")
count = 0
a = []

while count<n:
	num = input("Enter the number")
	a.append(num)
	count = count + 1
l = input("Enter the number1:")
def search(a,l):
	
	for i in len(a):
		if (l==a[i]):
			return True			
	return False
			
	
print"ans is", search(a,l)		


