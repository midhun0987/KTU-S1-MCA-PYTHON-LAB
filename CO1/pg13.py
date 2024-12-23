 #13. Create a list of colors from comma-separated color names entered by user. Display first and last colors.

list=[i for i in input("enter the colors:")].split(",")
print("First colour entered is:",list[0])
print("Last colour entered is:",list[-1])