import random

nums = [random.randint(1,100) for i in range(20)]

nums_sorted = sorted(nums)

print("List:", nums)
print("Second Smallest:", nums_sorted[1])
print("Second Largest:", nums_sorted[-2])
