letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

phrase = ""
valid = False

print('Please input the phrase to be encrypted. This can only include letters and spaces.')
phrase = input().upper()

encrypted = ""
for char in phrase:
    if char == " ":
        encrypted += " "
    elif char.isalpha():
        index = letters.index(char)
        encrypted += letters[25 - index]
        
print("The Atbash encryption is: {}".format(encrypted))