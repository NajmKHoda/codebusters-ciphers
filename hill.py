import numpy as np

# Performs a ceiling division, literally only used once
def ceil_div(a, b):
    return -(a//-b)

# Obtain an appropriate keyword and generate the 2x2 matrix
print('Please input a 4-letter keyword for the Hill cipher. Note that the resulting matrix must have a determinant that is nonzero and coprime with 26.')
keyword = ''
keyword_matrix = np.zeros((2, 2)).astype(int)
valid = False
while not valid:

    keyword = input().upper() # User inputs keyword

    if keyword.isalpha() and len(keyword) == 4:

        # Generate the corresponding 2x2 matrix
        for index, char in enumerate(keyword):
            num = ord(char) - 65 # Turn Unicode to 0-26
            keyword_matrix[index//2][index%2] = num
        print(f'The matrix for keyword "{keyword}" is\n{keyword_matrix}')

        # Check the determinant
        determinant = np.linalg.det(keyword_matrix)
        if all(determinant != x for x in (0, 2, 13)):
            valid = True
        else:
            print(f'This matrix has an invalid determinant ({determinant}). Please type in another keyword.')
    
    else:
        print('That keyword is invalid. Please try again.')

# Obtain the message.
print('Please input the message to be encrypted. Note that this can only contain letters.')
message = ''
valid = False
while not valid:
    message = input()
    message = ''.join(c.upper() for c in message if c.isalpha())
    if message != '':
        if len(message)%2 != 0:
            message += "Z" # Make the message length an even number (divisible by 2)
        valid = True
    else:
        print('That message is not valid. Please try again.')

# Generate the matrix for the message
message_matrix = np.zeros((2, ceil_div(len(message), 2))).astype(int)
for index, char in enumerate(message):
    num = ord(char) - 65
    message_matrix[index%2][index//2] = num
print(f'The matrix for the message "{message}" is\n{message_matrix}')

# Compute the encrypted matrix
encrypted_matrix = keyword_matrix @ message_matrix % 26
print(f'The encrypted matrix is\n{encrypted_matrix}')

# Translate the matrix into a code
code = ''
for column in encrypted_matrix.T:
    for num in column:
        code += chr(num + 65) # Turn 0-26 back to Unicode

# Output the code, aaaaaand we're done! :)
print(f'resulting in the code "{code}".')