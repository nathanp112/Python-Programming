# Ask the user for a letter
user_text = input('Enter a letter: ')

# Make lowercase
user_text = user_text.lower()

# Check if the input is a vowel
if user_text in ['a', 'e', 'i', 'o', 'u']:
    print(f"The letter {user_text} is a vowel.")
else:
    print(f"The letter {user_text} is not a vowel.")