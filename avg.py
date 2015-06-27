n=input("enter the number of numbers")
def avg(n):
count =0
sum = 0
while count<n:
	count = count+1
	print "number",count
	number=input("Enter the number")
	sum = sum + number
return sum	
print"the avg is",avg(5)

