import random

numbers = []

for i in range(20):
    n = random.randint(1, 100)
    numbers.append(n)

print("List:", numbers)

average = sum(numbers) / len(numbers)

print("Average:", average)
