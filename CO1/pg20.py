 #20 From a list of integers, create a list removing even numbers.

ol=[int(i) for i in input("Enter the numbers: \n").split()]
nl=[i for i in ol if i%2!=0]
print("New list =",nl)