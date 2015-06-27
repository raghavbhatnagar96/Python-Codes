n = input("Enter the number:")
a = []
count = 0
while count<n:
	num = input("Enter the number")
	count = count+1
	a.append(num)

def swap(a):
	i = input("enter 1")
	k = input("enter 2")	
	j=a[i]
	a[i]=a[k]
	a[k]=j
	return a
swap(a)
print a
