# program that runs the Zombie Dice Bots game with homemade bots
# WIP

"""Project task:
A bot that, after the first roll, randomly decides if it will continue or stop
A bot that stops rolling after it has rolled two brains
A bot that stops rolling after it has rolled two shotguns
A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
A bot that stops rolling after it has rolled more shotguns than brains"""

import zombiedice
import random


class RandomStop:  # fixed
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults and random.randint(0, 1) == 0:
            diceRollResults = zombiedice.roll()


class TwoBrains:  # fixed
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brain = 0
        while brain < 2:
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                return
            brain += diceRollResults['brains']


class TwoShotguns:  # fixed
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotgun = 0
        while shotgun < 2:
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                return
            shotgun += diceRollResults['shotgun']


class OneToFourExceptTwoShotguns:  # fixed
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # initial roll
        shotgun = 0
        rolls = 1
        max_rolls = random.randint(1, 4)
        while diceRollResults and rolls <= max_rolls:
            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            if diceRollResults is None:  # AKA when you die:
                return
            shotgun += diceRollResults['shotgun']
            rolls += 1


class ShotgunsOverBrains:  # fixed
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotgun = 0
        brain = 0
        while shotgun >= brain:
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                return
            shotgun += diceRollResults['shotgun']
            brain += diceRollResults['brains']


zombies = (
    RandomStop(name='RandomStop'),
    TwoBrains(name='TwoBrains'),
    TwoShotguns(name='TwoShotguns'),
    OneToFourExceptTwoShotguns(name='OneToFourExceptTwoShotguns'),
    ShotgunsOverBrains(name='ShotgunsOverBrains'),
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
