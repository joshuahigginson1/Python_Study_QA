# A script to define multiple different dice, and import them into a game.

# Imports -----------------------------------------------------------------------------------------------------------

import random


# Define Classes ---------------------------------------------------------------------------------------------------

class Dice:  # Create a class to model a dice.

    def __init__(self, sides):
        self.sides = sides
        self.name = str(sides) + " sided dice!"

    def dice_roll(self):  # Creates a function which rolls a dice.
        roll = None  # Initialise roll variable.
        roll = random.randrange(1, self.sides)  # Generates a random number between 1, and the number of sides of dice.

        return roll  # Returns a integer dice roll.


class SixSided(Dice):

    def __init__(self):
        self.sides = 6


class EightSided(Dice):

    def __init__(self):
        self.sides = 8


class TwentySided(Dice):

    def __init__(self):
        self.sides = 20