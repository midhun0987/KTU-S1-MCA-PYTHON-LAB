 #10. Generate all factors of a number.
 
def factors(m):
	for i in range(1, m + 1):
		if m % i == 0:
			print(i)
 
 
a=int(input("Enter a number :"))
factors(a)