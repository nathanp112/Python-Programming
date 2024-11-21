# Open the file in step 1) and read its contents
# Output each line on new line

def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip)


# call
read_file("task1.txt")
