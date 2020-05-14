#! python3
# Stopwatch with prettified outputs that copies the results to the clipboard.
# To allow keyboard interrupts in PyCharm, tick: run->run...->Edit Configurations...->Emulate terminal in output console

import time
import pyperclip

# Display the program's instructions.
print('Press enter to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1
clipboard = []
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lapInfo = f'Lap #{str(lapNum).ljust(3)}: {str(totalTime).rjust(5)} ({str(lapTime).rjust(6)})'
        print(lapInfo, end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
        clipboard.append(lapInfo)
except KeyboardInterrupt:
    pyperclip.copy(clipboard)
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
