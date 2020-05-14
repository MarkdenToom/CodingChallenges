# Simple multiplication test
# Done

import random
import time

import pyinputplus as pyip

numberOfQuestions = 10  # total number of questions
correctAnswers = 0  # default number of right answers at the start of the test
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)  # Pick two random numbers:
    num2 = random.randint(0, 9)

    prompt = f'#{questionNumber}: {num1} x {num2} = '  # display question
    try:
        pyip.inputStr(prompt,  # display the question we defined in the line above this try clause
                      allowRegexes=[f'^{num1 * num2}$'],  # regex for right answer
                      blockRegexes=[('.*', 'Incorrect!')],  # regex for wrong answer
                      timeout=8, limit=3)  # 8 seconds per answer, with 3 tries each
    except pyip.TimeoutException:  # what happens when time runs out
        print('Out of time!')
    except pyip.RetryLimitException:  # what happens when the limit of tries has been reached
        print('Out of tries!')
    else:  # what happens when the correct answer has been given
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)  # Brief pause to let user see the result of their answer before asking the next question

if correctAnswers == numberOfQuestions:
    print(f'Perfect score: {correctAnswers} / {numberOfQuestions}!')
if correctAnswers > numberOfQuestions / 2 and correctAnswers != numberOfQuestions:
    print(f'You passed: {correctAnswers} / {numberOfQuestions}!')
if correctAnswers <= numberOfQuestions / 2:
    print(f'You failed: {correctAnswers} / {numberOfQuestions}!')
