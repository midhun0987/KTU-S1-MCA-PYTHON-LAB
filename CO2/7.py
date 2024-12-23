# 7. Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’.

a=input("Enter a string :")
b=a[-3:]
if b=='ing':
    print(a+'ly')
else:
    print(a+'ing')