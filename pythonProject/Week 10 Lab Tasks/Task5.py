print("Task 5: ")
import re


def task5(postal_code):
    pattern = r'^[a-zA-Z][0-9] [0-9][]a-zA-Z][0-9]$'
    if re.match(pattern, postal_code):
        return True
    return False


print("Case 1: ", task5("abc"))
