# 6.Store a list of first names. Count the occurrences of ‘a’ within the list

names = input("Enter the names:")
count= sum(name.lower().count('a') for name in names)
print("Total occurrences of 'a':", count)