#! python3
# countdown.py - A simple countdown script.

"""At a high level, here’s what your program will do:
1. Count down from 5.
2. Play a sound file (alarm.wav) when the countdown reaches zero.

This means your code will need to do the following:
1. Pause for 1 second in between displaying each number in the countdown by calling time.sleep().
2. Call subprocess.Popen() to open the sound file with the default application."""

import subprocess
import time
from os import chdir

chdir(r'C:\Users\Beheerder\Py3Projects\automate_online-materials')

timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)
