#! python3 -O
# Creates 35 different US state capitals multiple choice tests with all questions in random order and answer sheets too.
# Done

"""Here is what the program does:
1. Creates 35 different quizzes
2. Creates 50 multiple-choice questions for each quiz, in random order
3. Provides the correct answer and three random wrong answers for each question, in random order
4. Writes the quizzes to 35 text files
5. Writes the answer keys to 35 text files

This means the code will need to do the following:
1. Store the states and their capitals in a dictionary
2. Call open(), write(), and close() for the quiz and answer key text files
3. Use random.shuffle() to randomize the order of the questions and multiple-choice options"""

import random
from os import chdir

chdir(r'C:\Users\Beheerder\Py3Projects\9 Generating Random Quiz Files')  # set cwd where we want to save the quizzes

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California':
            'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
            'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
            'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana':
            'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey':
            'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
            'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania':
            'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia':
            'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming':
            'Cheyenne'}

for quizNum in range(35):  # generate 35 quizzes
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')  # Create the quizzes
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')  # Create answer key files
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')  # Write out the header for the quiz.
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')  # >1 write() functions =~= append
    quizFile.write('\n\n')

    states = list(capitals.keys())  # convert to shufflable list
    random.shuffle(states)  # shuffle the order of the states

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]  # correct answers are the capitals linked to their states
        wrongAnswers = list(capitals.values())  # wrong answers are all capitals
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # delete correct answers from wrong answers list
        wrongAnswers = random.sample(wrongAnswers, 3)  # create list of 3 wrong answers for the question (duplicates?)
        answerOptions = wrongAnswers + [correctAnswer]  # create list of 3 wrong and 1 right answer
        random.shuffle(answerOptions)  # shuffle the list of possible answers randomly

        # Write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n")  # 'ABCD'[i] is an array that cycles through all
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()
