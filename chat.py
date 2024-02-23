# Get input character from the user
character = input("Enter a character: ")

# Check and categorize the character
if character.isupper():
    print("Capital letter")
elif character.islower():
    print("Small case letter")
elif character.isdigit():
    print("Digit")
else:
    print("Special symbol")
