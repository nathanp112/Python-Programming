# Student ID: 101485672
# Student Name: Nathan Prince
# 1) Ask the user for a filename. (0.5 marks)
# a) Check to determine if filename has an extension (1 mark)
# i) If not, add a “.txt” extension (1 mark)
# b) Check to determine if the filename already exists in the current working directory (1.5 marks)
# i) If so, raise an exception (your choice) with an appropriate, descriptive message (1 mark)
# c) If no exception, proceed to Step 2

import os


def get_filename():
    filename = input("Please enter a file name: ")
    if "." not in filename:
        filename += ".txt"

    # Filename exists or not
    if os.path.exists(filename):
        raise FileExistsError(f"The filename already exists.")
    return filename


# Create a file with the name the user inputted in step 1

def create_file(filename):
    with open(filename, "w"):
        print("File created.")


# Ask for content
def get_content():
    content = input("Enter the content")
    if len(content) < 10:
        raise ValueError("Content must be 10 characters wrong")
    return content


def appended_content(filename, content):
    with open(filename, "a") as file:
        file.write(content + '\n')


# Calling

try:
    filename = get_filename()
    print("File name is " + filename)
    create_file(filename)
    content = get_content()
    appended_content(filename, content)
    print("Data is entered successfully")
except ( ValueError, FileExistsError) as Err:
    print("Error", Err)
