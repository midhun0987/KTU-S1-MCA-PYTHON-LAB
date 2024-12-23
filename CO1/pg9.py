# 9.Create a string from given string where first and last characters exchanged.

a= input("Enter a string: ")
if len(a) > 1:
    new_string = ''.join([a[-1]] + list(a)[1:-1] + [a[0]])
else:
    new_string = a
print("Updated string:", new_string)