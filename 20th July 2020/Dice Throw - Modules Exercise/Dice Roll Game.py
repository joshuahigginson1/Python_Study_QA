# A script to practice module importing with dice.py.

# Declare Imports ---------------------------------------------------------------------------------------------------

import dice

# Define Functions --------------------------------------------------------------------------------------------------


# Declare variables -------------------------------------------------------------------------------------------------

times_rolled = 0
dice_total = 0
dice_counter = 0
game_dice = dice.SixSided()

# Execute code  -------------------------------------------------------------------------------------------------------

print("Welcome to Josh's dice game!")

times_rolled = int(input("How many times would you like to roll a dice? "))

for dice_rolls in range(times_rolled):
    dice_total += game_dice.dice_roll()
    dice_counter += 1
    print(f"After {dice_counter} rolls, the total number is {dice_total}!")

print("Thank you!")
