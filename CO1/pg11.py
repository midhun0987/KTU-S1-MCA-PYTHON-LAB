# 11. Find biggest of 3 numbers entered.

a = int(input("Enter first number: \n"))
b = int(input("Enter second number: \n"))
c = int(input("Enter third number: \n"))

if a > b and a > c:
	print(a, "is greater than", b, c)
elif b > a and b > c:
	print(b, "is greater than", a, c)
elif c > a and c > b:
	print(c, "is greater than", a, b)
elif a == b and b == c:
	print("All are equal")
else:
	print("There is a tie between the numbers")