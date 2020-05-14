# Done

import random

number_of_streaks = 0  # define number of streaks
streak_list = []  # create an empty list for streaks

# add H or T to streak_list
for experimentNumber in range(10000):
    coin_flip = random.randint(0, 1)  # flips the coin
    if coin_flip == 0:  # if the coin comes up as heads, add a H to the streakList.
        streak_list.append("H")
    elif coin_flip == 1:  # if the coin comes up as tails, add a T to the streakList.
        streak_list.append("T")

# add to the total number of streaks when you get a streak of 6 tails or 6 heads in a row
for i in range(len(streak_list)):
    if streak_list[i] == "H" and streak_list[i - 1] == "H" and streak_list[i - 2] == "H" and streak_list[i - 3] == "H" and streak_list[i - 4] == "H" and streak_list[i - 5] == "H":
        number_of_streaks += 1
    elif streak_list[i] == "T" and streak_list[i - 1] == "T" and streak_list[i - 2] == "T" and streak_list[i - 3] == "T" and streak_list[i - 4] == "T" and streak_list[i - 5] == "T":
        number_of_streaks += 1

# Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (number_of_streaks / 100))
