#12.Accept a file name from user and print extension of that.

file = input("Enter File Name : ")
temp = file.split(".")
ext = temp[-1]
if len(temp) > 1:
	print("Extension : ", ext)
else:
	print("No extension found")