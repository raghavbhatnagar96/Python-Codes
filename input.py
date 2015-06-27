n = input("Enter the number:")
def print_digits(n):
	n = abs(n)
	while n>0:
		print n%10
		n = n/10
print_digits(n)
