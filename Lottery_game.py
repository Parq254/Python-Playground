winning_number = 5
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input('Guess a number: '))
    guess_count += 1
    if guess == winning_number:
        print('You won')
    else:
        print('Try again')
