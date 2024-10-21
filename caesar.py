letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Query for the Caesar shift
shift = 0
valid = False

print('Please input the Caesar shift. This should be a number.')
while not valid:
    shift = input()
    valid = shift.isdigit()
    if not valid:
        print("That shift is invalid. Try again.")
shift = int(shift)

# Generate the cipher
cipher = {}
for index, letter in enumerate(letters):
    cipherLetter = letters[(index + shift) % 26]
    cipher[letter] = cipherLetter
    
# Print the cipher
plainOutput = ' '.join(letters)
cipherOutput = ' '.join(cipher.values())
print('')
print('This the Caesar cipher, given a shift of: {}'.format(shift))
print("Plain  | {}".format(plainOutput))
print("Cipher | {}".format(cipherOutput))
print('')

# Query for the phrase to be encrypted.
phrase = 0
valid = False

print('Please input the phrase to be encrypted. This can only contain letters and spaces.')
phrase = input().upper()

# Encrypt the phrase
encrypted = ""
for char in phrase:
    if char == " ":
        encrypted += " "
    elif char.isalpha():
        encrypted += cipher[char]

# Output the encrypted phrase
print("The Caesar encryption is: {}".format(encrypted))