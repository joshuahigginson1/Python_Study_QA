"""

Task:




Dev Notes:

"""


# Declare Imports ----------------------------------------------------------------------------------------------------


# Define Classes -----------------------------------------------------------------------------------------------------
class Bird_Super_Parent:
    def __init__(self, name, nest_location, wingspan, fav_berries):
        self.name = name
        self.nest_location = nest_location
        self.wingspan = wingspan
        self.fav_berries = fav_berries


class Bird_No_Wings(Bird_Super_Parent):

    def __init__(self, name, nest_location, fav_berries):
        super(Bird_Super_Parent).__init__(name, nest_location, fav_berries)


# Execute Code -------------------------------------------------------------------------------------------------------

bird_4 = Bird_No_Wings("PingPong", "Island Shoreline", "Magic Berries")