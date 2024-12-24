#25-11-2024

#Python program to copy odd lines of one file to other

#programcode:


with open("midhun.txt", "r") as x, open("demo.txt","w") as y:
    line_number = 0
    for line in x:
        if line_number % 2 == 0:  
            y.write(line)
        line_number += 1
