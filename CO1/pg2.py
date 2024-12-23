a = int(input("Enter the Current year:\n"))
b = int(input("Enter the final Year:\n"))

print("Future leap years from", a, "to", b, "are:")
for i in range(a, b + 1):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        print(i)