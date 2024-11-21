# Task 1
print("Task 1: ")


def task1(arg1, arg2, arg3):
    return type(arg1).__name__, type(arg2).__name__, type(arg3).__name__


# call
print("Case 1: ", task1(1, "hi", 1.1))
print("Case 2: ", task1(1, 2, 3))
print("Case 3: ", task1("hi", "hello", "world"))