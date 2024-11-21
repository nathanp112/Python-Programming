# Ask the user for an input
user_text = input("Enter an input string: ")
valid_title = user_text.istitle()
upper_txt = user_text.upper()
print("The string with UPPER case is " + upper_txt)
lower_txt = user_text.lower()
print("The string with LOWER case is " + lower_txt)
if valid_title:
    print(f"The title {valid_title} is valid ")
else:
    print(f"The title {valid_title} is not valid ")
