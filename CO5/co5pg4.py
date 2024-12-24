#4.Write a Python program to read specific columns of a given CSV file and print the content of the columns.

import csv

CI=int(input("Enter coloumn"))

with open("student.csv",mode="r") as file:
	csvr=csv.reader(file)

	rows=list(csvr)	
	
	for row in rows:
		print(row)
		
	for row in rows:
		if len(row)>CI:
			print(row[CI]) 
