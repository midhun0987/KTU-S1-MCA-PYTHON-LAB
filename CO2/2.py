# 2.Generate Fibonacci series of N terms

n =int(input("Enter the limit: "))
a =0
b =1
for i in range(n):
    print(a)
    c =a+b
    a =b
    b =c
