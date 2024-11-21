list2 =[1, 2, 3]
print("My list is:", list2)
list2.append(9)
print("My list after adding is: ", list2)
list2.remove(2)
print("My list after removing: ", list2)
item = 3
if item in list2:
    print("My list contains the item on: ", list2.index(item))
else:
    print("User Message")