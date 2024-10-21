from string import ascii_uppercase as alphabet
from re import match

# Obtain the index of the given letter (0-25)
def index_of_letter(letter):
    capital = letter.upper()
    return ord(capital) - 65 # Unicode index of A is 65

# Inverse function of the above
def letter_of_index(index):
    return chr(index + 65)

# Ensures that the inputted phrase is valid for this cipher's purposes.
def validated_input():
    current_input = ''
    valid = False
    while not valid:
        current_input = input().upper()
        if match('[A-Z]', current_input):
            valid = True
        else:
            print('Invalid input. Please try again.')

# Obtain the key.
print('Please input the key to be used.')
key = validated_input()

# Obtain the message.
print('Please input the message to be used.')
message = validated_input()
