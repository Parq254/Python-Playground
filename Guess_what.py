answer = input('Would you like to play a game(Y/N) :').upper()
if answer == 'Y':
    guess = input('Pick a number between one-five: ').lower()
    if guess == 'one':
        print('Kiss : Neck')
    elif guess == 'two':
        print('Kiss : Ear')
    elif guess == 'three':
        print('Kiss : Thigh')
    elif guess == 'four':
        print('Kiss : Lips')
    elif guess == 'five':
        print('Kiss : Hand')
    else:
        print('Wrong number pick again')
elif answer == 'N':
    print("We'll play another time")
