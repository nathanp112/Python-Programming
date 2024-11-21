print("Task 2:")


def task2(text, num):
    if not isinstance(text, str) or not isinstance(num, int) or num < 2:
        return False
    else:
        return text * num


# Call
print("Case 1: ", task2("hello", -2))
print("Case 2: ", task2("World", 5))
print("Case 3: ", task2("Hello", "Bye"))
print("Case 4: ", task2("Sky", "Blue"))

