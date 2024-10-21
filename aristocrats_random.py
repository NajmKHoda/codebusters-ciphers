from string import ascii_uppercase as alphabet
from random import choice
from re import sub, match

# Randomize the cipher
available_letters = list(alphabet)
cipher = {}
for letter in alphabet:

    # Randomly select a letter
    cipher_letter = choice(available_letters) 
    while cipher_letter == letter: # Ensure that no letter can ever map to itself
        cipher_letter = choice(available_letters)

    # Add the letter to the cipher
    cipher[letter] = cipher_letter
    available_letters.remove(cipher_letter)

# Prompt the user for a message
print('Please enter the message to be encrypted.')
message = ''
valid = False
while not valid:
    message = input().upper()
    if (match('[A-Z]', message)):
        valid = True
    else:
        print('The message must contain at least one letter.')

print('Would you like to use Patristocrat formatting? (Y/N)')
patristocrat = False
valid = False
while not valid:
    response = input().upper()
    if response == 'YES' or response == 'Y':
        patristocrat = True
        valid = True
    elif response == 'NO' or response == 'N':
        patristocrat = False
        valid = True
    else:
        print('That is not a valid response. Try again.')

# Encrypt the message
code = ''
if patristocrat:
    stripped_message = sub('[^A-Z]', '', message)
    for i, char in enumerate(stripped_message):
        code += cipher[char]
        if i % 5 == 4:
            code += ' ' # Add a space between each group of 5
else: # Just a good ol' Aristocrat
    for char in message:
        if char.isalpha():
            code += cipher[char]
        else:
            code += char

print('The randomized Aristocrat cipher is shown below:\n')
print(f'PT | {' '.join(alphabet)} |')
print(f'CT | {' '.join(cipher[letter] for letter in alphabet)} |\n')
print(f'The resulting code from this cipher is:\n{code}')