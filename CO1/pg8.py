# 8 Get a string from an input string where all occurrences of first character replaced with ‘$’,
 #except first character.

a=input("Enter a string: ")
if a:
    first_char = a[0]
    newstring = first_char + a[1:].replace(first_char, '$')
else:
    newstring = ""
    print("Modified string:", newstring)