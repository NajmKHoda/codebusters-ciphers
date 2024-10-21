from string import ascii_uppercase as alphabet

counts = [0] * 26

print('Please input the text to be analyzed.')
text = input().upper()

for char in text:
    if char.isalpha():
        index = ord(char) - 65 # capital A is code 65
        counts[index] += 1

print('This is the resulting frequency table:')
print(f'      | {' '.join(alphabet)} |')
print(f'Freq. | {' '.join(str(count) if count > 0 else '-' for count in counts)} |')