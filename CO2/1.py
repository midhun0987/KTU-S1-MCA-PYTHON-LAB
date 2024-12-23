# 1.Program to find the factorial of a number

num=int(input("Enter a number:\n"))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")