def merge(list1, list2):
    result = list1 + list2
    result.sort()
    return result

a = [1,3,5]
b = [2,4,6]
print(merge(a,b))
