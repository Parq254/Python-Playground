email = input('Email Address: ')

if email.count('@') == 1 and len(email) >= 5:
    if email.find('.com') == len(email) - 4:
        print('valid Email')
    else:
        print('Invalid Email, must end with .com')
else:
    print('Invalid Email,must contain one @ and be longer than 5 characters')