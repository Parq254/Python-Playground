print ('I will add 5 to any number.')
num = input('Type a number:')

try:
    addnum = int(num) + 5
    print('5 +', num, 'is', addnum)
except:
    print('That is not a valid number')