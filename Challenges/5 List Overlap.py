list1 = [1, 20, 30, 100, 53, 23]
list2 = [2, 20, 10, 15, 100, 52, 23]

print (set(list1).intersection(list2))

list3 = [num for num in list1 if num in list2]
print(list3)