# Create a new module
# Create a function that
#     Write a file named Student_Number.txt
#         The contents should be their first name and last name on separate lines
# Create a function that
#     Ask the user for their student number
#     Ask the user for their first name
#     Ask the user for their last name
#     Calls the function above with the user input

def student_info(student_number, first_name, last_name):
    print(student_number, first_name, last_name)
    filename = f"{student_number}.txt"
    with open(filename, "w") as file:
        file.write(f" First Name:{first_name} \n Last Name: {last_name}")


def main():
    student_number = input("Enter Student Number:")
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    student_info(student_number, first_name, last_name)


if __name__ == '__main__':
    main()

# call


