'''
Super() = Function used in a child class to call methods from a parent class (superclass). Allows you
          you to extend the functionality of the inherited methods

    - Making a change to an attribute without the use of super method, could become time consuming.
'''
from IPython.terminal.shortcuts import create_identifier


class Shape:
    def __init__(self, color, is_filled):
        self.color = color  # Common attribute
        self.filled = is_filled  # Common attribute
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'} shape")

class Circle(Shape):

    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) # calling the constructor of the parent class.
        self.radius = radius

    # Method overridding, if the child uses a similar method as that of a parent, you will use that method.
    # i.e. the one used by the child.
    def describe(self):
        super().describe()  # Here we are extending the functionality of the describe method.
        print(f"Area of the circle is {3.14 * self.radius * self.radius} cm^2")
        # For using the describe method of the parent class we can use the super method.


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()  # Here we are extending the functionality of the describe method.
        print(f"Area of the square is { self.width * self.width} cm^2")
        # For using the describe method of the parent class we can use the super method.

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()  # Here we are extending the functionality of the describe method.
        print(f"Area of the triangle is {0.5 * self.width * self.height} cm^2")
        # For using the describe method of the parent class we can use the super method.

circle = Circle('red', True, 10)
circle.describe()
# print(circle.color)
# print(circle.filled)
# print(circle.radius)
#
square = Square('blue', False, 6)
square.describe()
# print(square.color)
# print(square.filled)
# print(square.radius)
#
triangle = Triangle('green', True, 6, 10)
triangle.describe()
# print(triangle.color)
# print(triangle.filled)
# print(triangle.radius)