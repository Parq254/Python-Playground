def greetings(self):
    name = input('Enter name: ').capitalize()
    age = int(input('Enter age: '))
    print(f'Good morning {name} {age}')


greetings(input)
