"""
Composition = The composed object directly owns its components,
which cannot exist independently  "owns-a" relationship - You are owning something
"""

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheels_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power) # This is composition, as we are creating a engine and wheel objects inside the car class.
        self.wheels = [Wheel(wheels_size) for _ in range(4)] # Car has for wheels, 4 wheels

    def display_car(self):
        return f"{self.make} {self.model} has {self.engine.horse_power} horse power and {self.wheels[0].size} in size"
car1 = Car("Ford", "Mustang", 400, 22)
car2 = Car("Chevrolet", "Corvette", 670, 19)

# Note the engine and wheel object exist inside the Car object, if the car object cess to exist those attributes also
# cess to exist.
print(car.display_car())