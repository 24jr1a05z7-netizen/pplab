word = input("Enter a word: ")

vowels = "aeiouAEIOU"

found = False
for ch in word:
    if ch in vowels:
        found = True
        break

if found:
    print("The word contains vowels")
else:
    print("The word does not contain vowels")
