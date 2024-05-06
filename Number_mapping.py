phone = input('Phone: ')
mapping = {
           '1': 'one',
           '2': 'two',
           '3': 'three',
           '4': 'four'
}
output = ""
for x in phone:
    output += mapping.get(x , '') + ' '
print(output)
