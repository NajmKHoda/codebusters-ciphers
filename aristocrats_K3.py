from string import ascii_uppercase as letters

# Returns a string with duplicates removed.
def remove_duplicates(key):
    true_key = ''
    for c in key:
        if c not in true_key: true_key += c
    
    return true_key

# Returns an alphabet constructed from the given key and offset
def create_alphabet(key, offset):
    remainder = ''.join(c for c in letters if c not in key)
    prefix = remainder[-offset:] if offset > 0 else ''
    suffix = remainder[:-offset] if offset > 0 else remainder

    return prefix + key + suffix

def validate_input(prompt, fn):
    valid = False
    response = input(prompt)
    while not valid:
        valid = fn(response)
        if not valid:
            print('Invalid response.')
            response = input(prompt)
    
    return response

# Main program

# Prompt user for key
key = validate_input('Enter an alphabetic key: ', lambda x: x.isalpha())
key = remove_duplicates(key.upper())

# Prompt user for offsets
max_offset = 26 - len(key)
offset_pt = validate_input(f'Enter a plaintext offset (0-{max_offset}): ', lambda x: x.isdigit() and int(x) < max_offset)
offset_pt = int(offset_pt)
offset_ct = validate_input(f'Enter a ciphertext offset (0-{max_offset}): ', lambda x: x.isdigit() and int(x) < max_offset)
offset_ct = int(offset_ct)

# Alphabets
pt_alphabet = create_alphabet(key, offset_pt)
ct_alphabet = create_alphabet(key, offset_ct)

# Cipher maps
forward_cipher = { p:c for p,c in zip(pt_alphabet, ct_alphabet) }
reverse_cipher = { c:p for p,c in zip(pt_alphabet, ct_alphabet) }

# Display the cipher
print('This creates the following cipher:\n')

print(f'PT | { ' '.join(pt_alphabet) } |')
print(f'CT | { ' '.join(ct_alphabet) } |\n')

print(f'PT | { ' '.join(letters) } |')
print(f'CT | { ' '.join(forward_cipher[c] for c in letters) } |\n')

print(f'CT | { ' '.join(letters) } |')
print(f'PT | { ' '.join(reverse_cipher[c] for c in letters) } |\n')

# Prompt user for message
message = input('Enter the message to encrypt (or nothing to stop): ').upper()

# Encrypt and print message
encrypted = ''.join(forward_cipher[c] if c.isalpha() else c for c in message)
print('The encrypted message is:')
print(encrypted)