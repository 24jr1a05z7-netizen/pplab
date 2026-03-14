import random

nums = [random.randint(1,100) for i in range(20)]

even_count = 0

for i in nums:
    if i % 2 == 0:
        even_count += 1

print("List:", nums)
print("Number of even numbers:", even_count)
