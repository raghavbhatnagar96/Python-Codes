number = 42
guess = 0
count = 0
while guess != number:
    count = count + 1
    guess = input('Guess a number: ')
    if guess > number:
        print 'Too high'
    elif guess < number:
        print 'Too low'
    else:
        print 'Just right'
        break
    if count > 2:
        print 'That must have been complicated.'
        break
