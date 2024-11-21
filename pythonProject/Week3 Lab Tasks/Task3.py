# Ask user for input
user_input = input("Enter a text: ")
# Ask user for character
user_char = input("Enter a character: ")
char_to_find = user_input.find(user_char)
print(char_to_find)
# if user_char>0
if user_char in user_input:
    print(f"The position {char_to_find} is found ")
else:
    print(f"The position {char_to_find} is not found ")

