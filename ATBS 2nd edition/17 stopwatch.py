#! python3
# A simple stopwatch program.
# To allow keyboard interrupts in PyCharm, tick: run->run...->Edit Configurations...->Emulate terminal in output console

"""At a high level, here’s what your program will do:
1. Track the amount of time elapsed between presses of the ENTER key, with each key press starting a new “lap” on the timer.
2. Print the lap number, total time, and lap time.

This means your code will need to do the following:
1. Find the current time by calling time.time() and store it as a timestamp at the start of the program, as well as at the start of each lap.
2. Keep a lap counter and increment it every time the user presses ENTER.
3. Calculate the elapsed time by subtracting timestamps.
4. Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit."""

import time

# Display the program's instructions.
print('Press enter to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap #{lapNum}: {totalTime} ({lapTime})', end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
