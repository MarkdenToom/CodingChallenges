# Functioning

import sys

print("Let's play the car game!")
print("Type 'help' to see commands")
command = ""
started = False

while True:
    command = input('> ').lower()
    if command == 'help':
        print("""start - to start the car
stop - to stop the car
exit - to exit the car""")
    elif command == 'start':
        if started:
            print("You try to start the car, but notice it's already running")
        else:
            started = True
            print('You turn the keys in the ignition and the engine starts revving')
    elif command == 'stop':
        if started:
            started = False
            print('You slam the brakes and quickly pull the keys out of the ignition')
        else:
            print("You slam the brakes, but notice the car isn't even running")
    elif command == 'exit':
        print('Have a good one')
        sys.exit()  # this could be a simple break in this code as well, but i'm using this for learning purposes.
    else:
        print('I am sorry, i do not understand that command')
