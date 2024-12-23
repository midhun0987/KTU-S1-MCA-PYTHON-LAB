#4.Count the occurrences of each word in a line of text.

a = input("Enter a line of text: ")
words = a.split()
word_count = {}

for word in words:
    word = word.strip('.,!?";:')
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)