string_list = ["apple", "banana", "cherry"]
integer_list = [1, 2, 3]

combined_set = set(string_list + integer_list)
print("Set is:", combined_set)

combined_set.add("oranges")
combined_set.add(7)
print("After adding the set is:", combined_set)

combined_set.remove("apple")
print("After removing set is: ", combined_set)

new_set = set(list(combined_set)[:3])
print("New set ", new_set)


for value in combined_set.union(new_set):
    print("Value are: ",value)

