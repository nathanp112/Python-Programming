# Open a file text file for writing
# create a list of strings
# write to the file each item of the list, appending each item to a new line of the file

def write_file(filename, data):
    # to open a file: with open(filename, mode)
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')


# calling
write_file("task1.txt", ["hallo", "wiegehts", "esmirsehrgut"])
