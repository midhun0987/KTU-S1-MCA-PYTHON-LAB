# 15.Print out all colors from color-list1 not contained in color-list2.

l1=[i for i in input("enter the colos in list 1:").split()]
l2=[i for i in input("enter the colos in list 2:").split()]
print(l1)
print(l2)
result=set(l1)-set(l2)
print("colors in list1 not in list2",result)