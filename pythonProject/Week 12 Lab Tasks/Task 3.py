# Open a csv file for writing
# create 3 rows that store username, first name, last name and age data (four columns)
# write the data to the csv file under the correct column

import csv


def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "First Name", "Last Name", "Age"])
        for row in data:
            writer.writerow(row)


# usage/cal
rows = [
    ["uname1", "Nathan", "Prince", "100"],
    ["uname2", "Betty", "Boop", "100"],
    ["uname3", "Joaquin", "Flores", "100"]
    ]
write_csv('task3.csv', rows)