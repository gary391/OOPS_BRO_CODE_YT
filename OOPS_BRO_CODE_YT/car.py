class Car:
    # This is the constructor method.
    # Dunder = Double underscrore.
    # Is used to make object of the class.
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Methods are actions that objects can perform.

    def drive(self):
        print(f"You drive the {self.color} {self.model}.")

    def stop(self):
        print(f"You stop the {self.color} {self.model}.")

    def describe(self):
        print(f"This is a {self.color} {self.model} from {self.year}.")