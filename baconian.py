from string import ascii_uppercase as alphabet
from random import randint
from re import sub

# Build the cipher.
cipher = {}
code = 0
for letter in alphabet:
    cipher[letter] = code
    if letter not in 'I,U': # I,J and U,V have the same code
        code += 1

print("Please input the message to be encrypted.")
message = ''
valid = False
while not valid:
    message = sub('[^A-Z]', '', input().upper())
    if message == '':
        print('The message must contain at least one letter.')
    else:
        valid = True

print("Please input the false message to be used.")
false_message = ''
valid = False
while not valid:
    false_message = input().upper()
    if len(sub('[^A-Z]', '', false_message)) >= 5*len(message):
        valid = True
    else:
        print('That false message is too short. Try again.')

cipher_text = ''
i = 0 # The current index, only considering letters
rand_code = None # Used for excess characters
for false_char in false_message:
    if false_char.isalpha():
        if (i == 5*len(message)):
            cipher_text += '|'
        # Get the current code
        current_code = 0
        if i >= 5*len(message): # Excess characters
            if rand_code is None:
                rand_code = randint(24,31)
            current_code = rand_code
        else: # Significant characters
            current_char = message[i // 5]
            current_code = cipher[current_char]
        
        # Check the appropriate bit on the code
        check_bit = 0b10000 >> (i % 5)
        cipher_text += false_char.upper() if current_code & check_bit != 0 else false_char.lower()
        i += 1
        
        # Reset the random code for each group of 5 excess characters
        if i >= 5*len(message) and i % 5 == 0:
            rand_code = None
            
    else:
        cipher_text += false_char
    
print("This is the encrypted message. The region after | is insignificant.")
print(cipher_text)