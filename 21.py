word = input("Enter a word: ")
words = ["a","am","man","an","arm","ram","ran"]

result = []

for w in words:
    temp = word
    valid = True
    for ch in w:
        if ch in temp:
            temp = temp.replace(ch,'',1)
        else:
            valid = False
            break
    if valid:
        result.append(w)

print("Possible words:", result)
