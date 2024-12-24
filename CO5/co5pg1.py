#25-11-2024
#Write a Python program to read a file line by line and store it into a list.

#program code:

f= open("midhun.txt", "r")
l=[i.split() for i in open("midhun.txt")]
f.close()
print(l)






