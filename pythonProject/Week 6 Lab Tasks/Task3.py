my_dict = {"a": 1, "b":2, "c":3}
print("The value of b:", my_dict.get('b'))

del my_dict["a"]
print("Dictionary after removing a: ", my_dict)

for key, value in my_dict.items():
    print("Key and Value: ", key, value)