name = input('Enter your name: ')
if len(name) < 3:
    print('Name must be  at least 3 characters long')
elif len(name) > 3:
    print('Green light')
    print(f'{name} is of correct length')
