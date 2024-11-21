# Ask user for a number
number = int(input("Enter a number: "))

# Determine if the number is positive, negative or neutral
if number < 0:
    print(f"The number: {number} is negative.")

elif number > 0:
    print(f"The number: {number} is positive.")

else:
    print(f"The number: {number} is neutral (zero).")
