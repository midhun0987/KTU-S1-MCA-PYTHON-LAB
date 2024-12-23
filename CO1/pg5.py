 #5.Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.


numbers = input("Enter a list of integers separated by spaces: ").split()
list = ['over' if int(num) > 100 else num for num in numbers]
print("NEW list:", list)