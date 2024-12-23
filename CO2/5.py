''' 5. Display the given pyramid with step number accepted from user. Eg: N=4
 1
 2 4
 3 69
 4 81216
'''

n=int(input("enter a limit "))
for i in range (1,n+1):
	for j in range(1,i+1):
		print(i*j,end=" ")     
	print()