import random
guess = ''
second_guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'
if toss == guess:  # fixed comparing 0 and 1 to heads and tails bug
    print('You got it!')
else:
    while second_guess not in ('heads', 'tails'):  # fixed allowing any input bug
        print('Nope! Guess again!')
        second_guess = input()  # fixed triple s in variable name bug
    if toss == second_guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
