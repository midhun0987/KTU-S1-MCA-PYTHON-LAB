'''9.Construct following pattern using nested loop
 *
 * *
 * **
 * ***
 * ****
 * ***
 * **
 * *
 *
 '''
n = int(input("Enter the limit: "))
for i in range(n):
	for j in range(i + 1):
		print("*", end=" ")
	print()
for i in range(n):
	for j in range(n - i - 1):
		print("*", end=" ")
	print()