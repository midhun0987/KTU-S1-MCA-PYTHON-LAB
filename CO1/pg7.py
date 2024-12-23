 #7.Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums to
 #same value (c) whether any value occur in both

list1 = list(map(int, input("Enter the first list of Integers:").split()))
list2 = list(map(int, input("Enter the second list of Integers:").split()))
a =len(list1) == len(list2)
b=sum(list1) == sum(list2)
c=[value for value in list1 if value in list2]
print("Are the lists of the same length?",a)
print("Do the lists sum to the same value?",b)
print("Common values in both lists:", c)