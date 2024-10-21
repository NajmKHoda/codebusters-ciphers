from string import ascii_uppercase as alphabet
from re import sub, match

# Prompt the user for a keyword
print('Please enter the keyword to be used.')
keyword = ''
valid = False
while not valid:
    keyword = input().upper()
    if match('[A-Z]', keyword):
        valid = True
    else:
        print('The keyword must contain at least one letter.')

# Remove all non-alpha and duplicate characters
true_keyword = ''
for char in keyword:
    if char.isalpha() and char not in true_keyword:
        true_keyword += char

# Obtain the offset.
print(f'Please enter the numerical offset for the keyword (0-{26 - len(true_keyword)}).')
offset = 0
valid = False
while not valid:
    offset = input()
    if match(r'\D', offset):
        print('That is not a positive integer. Please try again.')
    else:
        offset = int(offset)
        if offset >= 0 and offset <= (26 - len(true_keyword)):
            valid = True
        else:
            print('That offset is outside of the specified range. Please try again,')

# Construct the altered alphabet.
altered_alphabet = true_keyword
for letter in alphabet:
    if letter not in true_keyword:
        altered_alphabet += letter
if (offset > 0): # Wrap around the other side
    cutoff = 26 - offset
    wrap_around = altered_alphabet[cutoff:]
    altered_alphabet = wrap_around + altered_alphabet[:cutoff]

# Ask whether K1 or K2 encryption is to be used.
print('Would you like to use K1 (keyword in plaintext) or K2 (keyword in ciphertext) encryption?')
cipher = {}
valid = False
while not valid:
    encryption_type = input().upper()
    match encryption_type:
        case 'K1': # K1: plain alphabet contains keyword, cipher alphabet remains the same
            cipher = dict(zip(altered_alphabet, alphabet))
            valid = True
        case 'K2': # K2: cipher alphabet contains keyword, plain alphabet remains the same
            cipher = dict(zip(alphabet, altered_alphabet))
            valid = True
        case _:
            print('That is not a valid response (K1 or K2). Please try again.')

# Display the cipher table
print(f'The keyword {keyword} with offset {offset} results in the following {encryption_type} cipher:\n')
print(f'PT | {' '.join(altered_alphabet if encryption_type == 'K1' else alphabet)} |')
print(f'CT | {' '.join(alphabet if encryption_type == 'K1' else altered_alphabet)} |\n')

# Obtain the message
print('Please input the message to be encrypted.')
message = ''
valid = False
while not valid:
    message = input().upper()
    if match('[A-Z]', message):
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

print(f'The encrypted code is:\n{code}')