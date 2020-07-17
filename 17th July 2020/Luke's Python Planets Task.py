"""
Create a list of planets within our solar system.
Iterate through the list, but if you come across pluto, skip it!
"""


# Define Function
def planet_counting(list_counting, ignore):
    for count, planet in enumerate(planets_list):
        if planet in planets_to_ignore:
            print(f'{planet} is not a planet!')
            continue
        else:
            print(f'{planet} is the {count}th planet in our list!')


# Define Variables
planets_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planets_to_ignore = ['Pluto']

# Execute Code
planet_counting(planets_list, planets_to_ignore)
