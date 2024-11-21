# Ask the user for a year
year = int(input('Enter a year: '))

# conditions apply
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f" {year} is a leap")

else:
    print(f" {year} is not a leap year")