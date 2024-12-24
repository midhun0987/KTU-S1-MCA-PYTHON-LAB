import csv
with open("student.csv",mode="r")as file:
	csvr=csv.reader(file)
	for row in csvr:
		
		print(row)
		
