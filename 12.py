s = input("Enter a sentence: ")

# split the sentence into words
words = s.split()

# store words and their joined form in dictionary
d = {}

for w in words:
    d[w] = "-".join(w)

print("Dictionary:", d)
