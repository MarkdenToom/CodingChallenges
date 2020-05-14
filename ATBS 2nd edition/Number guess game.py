# Functions as desired

import random

print('Guess a number between one and ten!')
secretNumber = random.randint(1, 10)

for i in range(0, 3):
    guess = int(input('Guess: '))
    if guess == secretNumber:
        print('Congratulations, you won!')
        break
    if guess != secretNumber:
        print("Nope!")      # how do i made this not show up after the last failed attempt?
else:
    print('You failed.')

#   Old code down below. It doesn't print 'Nope!' after a third failed attempt.

#import random
#print('Guess a number between one and ten!')
#secret_number = random.randint(1, 10)
#guess_count = 0
#guess_limit = 3
#while guess_count < guess_limit:
#    guess = int(input('Guess: '))
#    guess_count += 1
#    if guess == secret_number:
#        print('Congratulations, you won!')
#        break
#    elif not guess == secret_number and guess_count < guess_limit:
#        print('Nope!')
#else:
#    print('You failed.')