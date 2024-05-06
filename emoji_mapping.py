emoji = input('Enter emoji: ')
mapping = {
    '😀': 'happy',
    '🙁': 'sad',
    '😅': 'laugh',
    '😡': 'angry',
    '😍': 'love', 
}
output = ""
for character in emoji:
    output += mapping.get(character, '') + ' '
print(output)