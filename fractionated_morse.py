from string import ascii_uppercase as alphabet
from re import sub, search, findall

# Ensures that input has at least one letter.
def validated_input(validator):
    response = ''
    valid = False
    while not valid:
        response = input()
        if validator(response):
            valid = True
        else:
            print('That input is not valid. Try again.')
    return response

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

# This will be mapped to the alphabet.
trigraphs = [
    '...', '..-', '..x', '.-.', '.--', '.-x', '.x.', '.x-', '.xx', '-..', '-.-', '-.x', '--.',
    '---', '--x', '-x.', '-x-', '-xx', 'x..', 'x.-', 'x.x', 'x-.', 'x--', 'x-x', 'xx.', 'xx-'
]

# Prompt the user for a keyword.
print('Please enter the keyword to be used.')
keyword = sub('[^A-Z]', '', validated_input(lambda x: search('[A-Za-z]', x)).upper())
actual_keyword = ''
available_letters = list(alphabet)
for char in keyword: # Remove duplicate characters.
    if char not in actual_keyword:
        actual_keyword += char
        available_letters.remove(char)

# Prompt the user for an offset.
max_offset = 26 - len(actual_keyword)
print(f'Enter the offset for this keyword (0-{max_offset})')
offset = int(validated_input(lambda x: x.isdigit() and int(x) >= 0 and int(x) <= max_offset))

# Offset the keyword through wraparound
cipher_alphabet = actual_keyword + ''.join(available_letters)
split_point = len(actual_keyword) + max_offset - offset
cipher_alphabet = cipher_alphabet[split_point:] + cipher_alphabet[:split_point]

# Create the trigraph cipher.
trigraph_cipher = dict((trigraphs[i], cipher_alphabet[i]) for i in range(26))

# Prompt the user for a message.
print('Please enter the message to be encrypted.')
message = validated_input(lambda x: search('[A-Za-z]', x)).upper()

# Make a string of morse code.
morse_string = ''
for word in findall(r'\b[A-Z]+\b', message):
    for char in word:
        morse_string += morse_code[char] + 'x'
    morse_string = morse_string[:-1] # Cleave the last x
    morse_string += 'xx'
morse_string = morse_string[:-2] # Cleave the last xx
while len(morse_string) % 3 != 0:
    morse_string += 'x'

print(f'The Morse code for this message is: \n{morse_string}')

code = ''
i = 0
while i < len(morse_string):
    trigraph = morse_string[i:i+3]
    code_char = trigraph_cipher[trigraph]
    code += code_char
    i += 3

print(f'The resulting code is: \n{code}')