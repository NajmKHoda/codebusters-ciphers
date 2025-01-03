from string import ascii_uppercase as alphabet
from re import match

first_half = alphabet[:13]
second_half = alphabet[13:]

# Obtain the index of the given letter (0-25)
def index_of_letter(letter):
    capital = letter.upper()
    return ord(capital) - ord('A')

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
    return current_input

# Obtain the key.
print('Please input the key to be used.')
key = validated_input()

# Obtain the message.
print('Please input the message to be used.')
message = validated_input()
message = ''.join([ c.upper() for c in message if c.isalpha() ])

repeated_key = (key.upper() * ( len(message) // len(key) + 1 ))[:len(message)]

encrypted = ""
for mc, kc in zip(message, repeated_key):
    mi = index_of_letter(mc)
    ki = index_of_letter(kc) // 2
    if mi < 13:
        i = (mi + ki) % 13
        encrypted += second_half[i]
    else:
        i = (mi % 13) - ki
        encrypted += first_half[i]
    
print(f'The encrypted message is: { encrypted }')