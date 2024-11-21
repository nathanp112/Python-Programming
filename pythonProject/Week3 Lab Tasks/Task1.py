# Ask the user for a number
user_number = input("Enter a number:")
res = user_number.isdigit()
if res:
    print(f"{res},The character {user_number} is numeric. ")

else:
    print(f"{res}The number {user_number} is not numeric ")
