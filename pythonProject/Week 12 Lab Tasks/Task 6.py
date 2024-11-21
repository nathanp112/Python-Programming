# Create a module that searches for a student by either their student number, first name or last name
# Ask the user which field they would like to search
# Ask the user for a value they would like to search
# If user selects student number,
#     Determine if student_number.txt file exists in system.
#         If yes,
#             Display success message and output student number, first name and last name
#          If no,
#               Display sorry message
#
# If user selects first name,
#     Search all files in system. that have a value of {first name}. Display the first hit.
#         If yes,
#             Display success message and output student number, first name and last name
#         If no,
#             Display sorry message
#
# Likewise for last name

import os


def search_student(field, value):
    # find the file in the directory
    if field == "student number":
        print("Hello")
        if os.path.exists(f"{value}.txt"):
            print("1")
            with open(f"{value}.txt", 'r') as file:
                first_name = file.readline().strip()
                last_name = file.readline().strip()
                print("Success, Student is found")
                print(f"{first_name} {last_name}")
        else:
            print("Sorry student not found")


def main():
    field = input("Enter the field you want to search: ")
    value = input("Enter the value you want to search: ")
    search_student(field, value)


if __name__ == "__main__":
    main()
