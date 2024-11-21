from typing import List

list4: list[str] = []
for i in range(5):
    user_input = input("Please enter something: ")
    if user_input not in list4:
        list4.append(user_input)
        print(list4)