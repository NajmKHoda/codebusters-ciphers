from string import ascii_uppercase
from math import gcd
alphabet = list(ascii_uppercase)

# Encrypts a character using an affine cipher.
# NOTE: This assumes that gcd(a, 26) = 1.
def affine_cipher(plain_char, a, b):
    
    cipher_char = ""
    if plain_char == " ":
        cipher_char = " "
    elif plain_char.isalpha():
        index = alphabet.index(plain_char)
        cipher_index = (a*index + b) % 26
        cipher_char += alphabet[cipher_index]
            
    return cipher_char

# Translate text given a dictionary of char-to-char conversions.
# NOTE: This drops characters that are not letters or spaces.
def translate(text, dictionary):
    
    translated_text = ""
    for char in text:
        if (char.isalpha()):
            translated_char = dictionary[char.upper()]
            translated_text += translated_char
        elif (char == " "):
            translated_text += " "
    
    return translated_text

# Prompt user for an a value
print("""An affine cipher is defined by the function E(x):
    E(x) = (ax+b) mod 26
Input the value for a. Note that a must be an integer that is coprime with 26.
In other words, the greatest common divisor of a and 26 must be 1.""")
a = 0
valid = False
while (not valid):
    a = input()
    try:
        a = int(a)
    except:
        print("That is not an integer. Please try again.")
    else:
        if (gcd(a, 26) == 1):
            valid = True
        else:
            print("{} is not coprime with 26. Please try again.".format(a))

# Prompt user for a b value.
print("Input the value for b. Note that b must be an integer.")
b = 0
valid = False
while (not valid):
    b = input()
    try:
        b = int(b)
    except:
        print("That is not an integer. Please try again.")
    else:
        valid = True

# Generate the cipher.
cipher = {x:affine_cipher(x,a,b) for x in alphabet}
reverse_cipher = {y:x for x, y in cipher.items()}

# Print the affine cipher's function and the resulting cipher table
affine_eq = ""
if (b > 0):
    affine_eq = f"E(x) = ({a}x+{b}) mod 26"
elif (b < 0):
    affine_eq = f"E(x) = ({a}x{b}) mod 26"
else:
    affine_eq = f"E(x) = {a}x mod 26"
print(f"The affine cipher defined by the function {affine_eq} generates the following cipher: \n")

print(f"PT | {' '.join(alphabet)}")
print(f"CT | {' '.join(cipher[x] for x in alphabet)}\n")

print(f"CT | {' '.join(alphabet)}")
print(f"PT | {' '.join(reverse_cipher[x] for x in alphabet)}\n")

# Ask the user if they wish for encryption or decryption
print("Would you like to ENCRYPT or DECRYPT a message?")
valid = False
while (not valid):
    response = input()
    if (response.upper() == "ENCRYPT"):
        valid = True
        # Encrypt the inputted message.
        print("Input a message to be encrypted. All characters that are not letters/spaces will be dropped.")
        message = input()
        print(f"The encrypted message is: \n{translate(message, cipher)}")
    elif (response.upper() == "DECRYPT"):
        valid = True
        # Decrypt the inputted message.
        print("Input a message to be decrypted. All characters that are not letters/spaces will be dropped.")
        message = input()
        print(f"The encrypted message is: \n{translate(message, reverse_cipher)}")
    else:
        print("That is not a valid response. Please input either ENCRYPT or DECRYPT.")
        