lst = [1,1,2,3,4,3,0,0]

new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("Original list:", lst)
print("List after removing duplicates:", new_list)
