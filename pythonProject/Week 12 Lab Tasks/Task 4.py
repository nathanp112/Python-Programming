# Open the file in step 3) and read its contents
# Output the content in a tabular format of columns and values


import csv


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))


read_csv("task3.csv")
