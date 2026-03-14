def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

numbers = [1, 2, 3, 4, 5]
print(is_sorted(numbers))
