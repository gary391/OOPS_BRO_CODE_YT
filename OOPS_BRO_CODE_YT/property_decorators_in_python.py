"""
@Property = Decorator used for define a method as a property (it can be accessed like an
attribute. Benefit: Add additional logic when read, write or delete attributes
Gives you getter, setter, and deleter method.
"""
class Rectangle:
    def __init__(self, width, height):
        self._width = width # _ makes the attribute internal
        self._height = height

    @property
    def width(self):
        return f"{self.width:.1f}cm"

    @property
    def height(self):
        return f"{self.width:.1f}cm"

# If you want modify the way you see the width and height with a decimal digit and cm appended after it.
rect = Rectangle(10, 20)
print(rect._width)
print(rect._height)