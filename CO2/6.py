 #6.Count the number of characters (character frequency) in a string.
def character_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

a = input("Enter a String:")
result = character_frequency(a)
print(result)
 