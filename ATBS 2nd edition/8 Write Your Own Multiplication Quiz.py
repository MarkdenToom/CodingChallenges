# Simple multiplication test
# WIP

# TODO Timer is very much broken and I don't feel like there's a need to fix it.

import random
import time
import threading

correctAnswers = 0  # default number of right answers at the start of the test
numberOfQuestions = 10  # total number of questions
# main loop for asking all questions
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)  # Pick two random numbers:
    num2 = random.randint(0, 9)
    right_answer = num1 * num2
    given_answer = ()
    wrong_answers = 0
    while given_answer != right_answer:
        t = threading.Timer(8, print, ['Out of time!'])
        t.start()
        given_answer = input(f'#{questionNumber}: {num1} x {num2} = ')  # ask question
        if not given_answer.isdecimal():  # if the given answer isn't a number:
            print('Invalid answer')
            continue
        if int(given_answer) != right_answer:
            if int(wrong_answers) == 2:  # when 3 tries have failed:
                print('Out of tries!')
                t.cancel()
                break
            else:
                print('Wrong answer, try again!')
                wrong_answers += 1  # number of tries - 1
                continue
        print('Correct!')
        t.cancel()
        correctAnswers += 1
        time.sleep(1)  # Brief pause to let user see the result of their answer before asking the next question
        break

# print results of the test
if correctAnswers == numberOfQuestions:
    print(f'Perfect score: {correctAnswers} / {numberOfQuestions}!')
if correctAnswers > numberOfQuestions / 2 and correctAnswers != numberOfQuestions:
    print(f'You passed: {correctAnswers} / {numberOfQuestions}!')
if correctAnswers <= numberOfQuestions / 2:
    print(f'You failed: {correctAnswers} / {numberOfQuestions}!')
