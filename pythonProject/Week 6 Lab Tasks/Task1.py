# Create a set of numbers between 10, 20

set1 = set(range(10, 21))
print("set 1: ", set1)

set2 = set(range(5, 16))
print("set 2: ", set2)

print("Difference: ", set1 - set2)
print("Common Numbers: ", set1.intersection(set2))

for value in set1:
    print("Set1: ",value)
for value in set2:
    print("Set2:", value)

