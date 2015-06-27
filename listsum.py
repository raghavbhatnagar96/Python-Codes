n = input("Enter the number of numbers")
a = []
count = 0
sum = 0
sum1 = 0
while count<n:
	num = input("Enter the number")
	a.append(num)
	count = count + 1
for i in a:
	for j in i:
		sum = sum + j
		j = j + 1
	

