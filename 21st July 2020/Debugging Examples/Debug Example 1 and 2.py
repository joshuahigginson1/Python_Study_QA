# Define Functions --------------------------------------------------------------------------------------------------


def product(n):
    total = 1  # Single = not double ==.
    for i in n:  # i, not n.
        total *= i
    return total  # Return has an indent error.


# Define Variables --------------------------------------------------------------------------------------------------
price = {"Burger": 3.10}  # Created new dictionary for 'price'.

user_funds = 10.31
item_price = price["Burger"]  # Price is not defined.

# Execute Code ------------------------------------------------------------------------------------------------------

if item_price < user_funds:
    print("You have enough money!")  # print was capitalised.
if item_price == user_funds:  # Double == not single =.
    print("You have the precise amount of money")
if item_price < user_funds:
    print("Sorry you don't have enough money")  # Missing quotations.

print(product([4, 4, 5]))
