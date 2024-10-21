import numpy as np
from re import search, sub

def validated_input(prompt, validator):
    print(prompt)
    response = ''
    while True:
        response = input()
        if validator(response):
            return response
        else:
            print('That is not a valid input. Try again.')

def check_key(key):
    if not key.isdigit(): return False
    used_digits = ''
    for digit in key:
        if digit in used_digits: # No duplicate digits
            return False
        else:
            used_digits += digit
    return True
    
def ceil_div(a,b):
    return -(a // -b)

# Prompt the user for a message.
message = validated_input("Please enter the message.", lambda x: search('[A-Za-z]', x))
message = sub('[^A-Z]', '', message.upper())

# Prompt the user for a key.
key = validated_input("Please enter a numerical key.", check_key)
num_rows = ceil_div(len(message), len(key))
num_columns = len(key)

# Generate the Complete Columnar array
cipher_array = np.full((num_rows, num_columns), 'X')
for i, char in enumerate(message):
    cipher_array[i // num_columns][i % num_columns] = char
cipher_array = cipher_array.T # This makes it easier to work with

sections = [None] * len(key)
for i, row in enumerate(cipher_array):
    true_index = int(key[i]) - 1
    sections[true_index] = ''.join(row)
code = ''.join(sections)

print(f'The resulting code is: {code}')
