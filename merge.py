n = input("Enter the number of numbers1")
a = []
count = 0
while count<n:
	num = input("Enter the number1")
	a.append(num)
	count = count + 1
m = input("Enter the number of number2")
b=[]
count1 = 0
while count1<m:
	number=input("Enter the number")
	b.append(number)
	count1=count1 + 1
a.extend(b)
def sort(p):
	i = 0
	for i in range(len(p)):
		if(a[i]>a[i+1]):
			a[i],a[i+1]=a[i+1],a[i]
	return p

print sort(a)
