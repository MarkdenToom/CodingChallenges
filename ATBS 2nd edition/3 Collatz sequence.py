import sys


def collatz(number):    # The code works the way I want it to and looks nice!
    if number % 2 == 0:
        number //= 2
        print(number)
        return number
    elif number % 2 == 1:
        number = number * 3 + 1
        print(number)
        return number


while True:
    try:
        n = input("Enter number: ")
        if n == "":
            sys.exit()
        while n != 1:
            n = collatz(int(n))
    except ValueError:
        print("Please use a valid integer. Enter a blank answer to exit.")
