"""
Static method = A method that belong to a class rather than any object from that class (instance)
usually used for general utility functions.
# Instance methods = Best for operation an instances of the class (objects)
# static methods = Best for utility functions that do not need access to class data.
"""


class MyEmployee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self): # Each instance of this class will have its own info method
        return f"{self.name} is a {self.position}"

    @staticmethod #General utility method, no need to have instance of the class.
    def is_valid_position(position):
        valid_position =["Manager", "Cook", "Cashier", "Janitor"]
        return position in valid_position


myemployee1 = MyEmployee("John", "Manager")
myemployee2 = MyEmployee("Jane", "Cook")
myemployee3 = MyEmployee("Bob", "Janitor")
myemployee4 = MyEmployee("Alice", "Cashier")
print(MyEmployee.is_valid_position("Jockey"))


print(myemployee1.get_info())
print(myemployee2.get_info())
print(myemployee3.get_info())
print(myemployee4.get_info())