'''List comprehensions:
 (a) Generate positive list of numbers from a given list of integers
 (b) Square of N numbers
 (c) Form a list of vowels selected from a given word
 (d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
 '''
 #PROGRAM (a)
l=[int(i) for i in input("Enter list of integers : ").split()]
p=[i for i in l if i>=0]
print("Positive Integers : ",p)
 
 #PROGRAM(b)
l=[int(i) for i in input("Enter List to be squared : ").split()]
l1=[i*i for i in l]
print(l1)
 
 #PROGRAM(c)
word=input("Enter word : ")
vowels = "aeiouAEIOU"
vowel_list = [i for i in word if i in vowels]
print("Vowels in ",word," : ",vowel_list)
 
 #PROGRAM(d)
word=input("Enter a word to get its ordinal: ")
ordinal_values = [ord(char) for char in word]
print(f"The ordinal values of the characters are : {ordinal_values}")
 