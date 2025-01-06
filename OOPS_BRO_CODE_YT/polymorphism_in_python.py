'''
polymorphism = Greek word that means to "have many forms or faces"
Poly = Many
Morphe = Form

TWO WAYS TO ACHIEVE POLYMORPHISM
1. Inheritance = An object could be treated of the same type as a parent class
2. "Duck Typing" = Object must have necessary attributes/methods
'''
from abc import ABC, abstractmethod
class Shape:

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return  self.side * self.side
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return  self.base * self.height * 0.5
# circle = Circle() # Because the circle object is inheritted from the shape, it can be considered a shape aand circle.
# square = Square()
# list of shapes

class Pizza(Circle):
    def __init__(self,radius, toppings):
        super().__init__(radius)
        self.toppings = toppings



shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza( 15, "pepperoni")]
# Note here even though pizza class doesn't have the area method, but since it inherits from the circle
# class, we get the area method of the circle class.
for shape in shapes:
    print(f"Area of {shape.__class__.__name__} is {shape.area()}")