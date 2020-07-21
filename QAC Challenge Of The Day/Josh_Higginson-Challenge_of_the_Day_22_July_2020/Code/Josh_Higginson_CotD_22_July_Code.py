"""
CotD 22nd July 2020 - CODE FILE

Task:

Define a class named Rectangle, which can be constructed by a length and width.
The Rectangle class needs to have a method that can compute area.
Finally, write a unit test to test this method.


Dev Notes:

Euler's formula: Faces + Vertices - Sides = 2

"""


# Define Classes -----------------------------------------------------------------------------------------------------

class Rectangle:  # Here, I'm defining class Rectangle.

    def __init__(self, height, width):  # Here in the initialisation method, I take in the height and width.
        self.vertices = 4
        self.sides = 4
        self.height = height
        self.width = width

    def area(self):  # My method for defining area.

        if self.height <= 0 and self.width <= 0:
            raise ValueError("Please enter positive integer values for width and height.")

        elif not isinstance(self.height, int) and not isinstance(self.width, int):
            raise ValueError("Please enter integer values for width and height.")

        elif self.height <= 0 or not isinstance(self.height, int):
            raise ValueError("Please enter a positive integer value for height.")

        elif self.width <= 0 or not isinstance(self.width, int):
            raise ValueError("Please enter a positive integer value for width.")

        else:
            return self.height * self.width  # returns the area.
