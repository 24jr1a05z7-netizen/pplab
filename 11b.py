import random

nums = [random.randint(1,100) for i in range(20)]

avg = sum(nums) / len(nums)

print("List:", nums)
print("Average:", avg)
