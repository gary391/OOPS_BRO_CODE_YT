from abc import ABC, abstractmethod # ABC means abstract base class

class Vehicle(ABC):
    '''
    @abstractmethod decorator is used to mark a method as abstract.
    This means that the method must be overridden by any subclass that
    inherits from the abstract class.
    '''
    @abstractmethod
    def go(self): # We don't define the method in the parent
        # class but the implementation happens in the children class.
        pass

    @abstractmethod
    def stop(self):
        pass

# vehicle = Vehicle() # This is not possible for this abstract class.

# create children which will inhert from the abstract class.
class Car(Vehicle):
    def go(self):
        print("Car is driving.")

    def stop(self):
        print("Car is stopping.")


class Motocycle(Vehicle):
    def go(self):
        print("Motocycle is moving.")


    def stop(self):
        print("Motocycle is stopping.")


class Boat(Vehicle):

    def go(self):
        print("you sail the boat.")

    def stop(self): # If you forgot to define an abstract method, you will get a type error.
        print("you anchor the boat.")
boat = Boat()
boat.go()
boat.stop()

# motorcyle = Motocycle()
#
# motorcyle.go()
# motorcyle.stop()

# car = Car()
#
# car.go()
# car.stop()