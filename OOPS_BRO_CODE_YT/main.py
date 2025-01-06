from numpy.testing.print_coercion_tables import print_coercion_table

from car import Car

# Instance of the class
car1 = Car("BMW",2021,"Red", False)
car2 = Car("Toyota",2024,"Blue", True)
car3 = Car("Honda",2022,"Green", True)
print(car1.model) # Here the dot is the access object operator.
print(car1.year)
print(car1.color)
print(car1.for_sale)
print()
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print()
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car2.drive()
car3.drive()
print()
car1.stop()
car2.stop()
car3 .stop()
print()
car1.describe()
car2.describe()
car3.describe()

class Student:

    # Class variable
    class_year = 2024
    num_of_students = 0

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        Student.num_of_students = Student.num_of_students + 1

student1 = Student("Gary", 20, "Computer Science")
student2 = Student("Amir", 30, "Mechanical Engineering")
student3 = Student("Patrick", 55, "Mechanical Engineering")


print(student1.class_year) # We can access the class variable using the name of the class.
print(Student.class_year) # Class variable this is a good practice.
print(student2.class_year)
print(student1.name)
print(student1.age)
print(student1.major)
print(Student.num_of_students)
print(f"My graduating class of {Student.class_year} has {Student.num_of_students} students.")


class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.is_alive = True
        self.age = age
        self.color = color

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal): # Inheritance

    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby", 10, "Black")
cat = Cat("Fluffy", 3, "White")
mouse = Mouse("Murphy", 1, "Brown")

print(dog.name)
print(dog.is_alive)
print(dog.age)
print(dog.color)
dog.eat()
dog.sleep()
print()
print(cat.name)
print(cat.is_alive)
print(cat.age)
print(cat.color)
cat.eat()
cat.sleep()

cat.speak()
dog.speak()
mouse.speak()

class Is_Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Is_Animal): # Parent

    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Is_Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator): # Multiple inhereitance.
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nimo")

rabbit.flee()
hawk.hunt()
fish.flee() # From the prey class
fish.hunt() # From the predator class
rabbit.eat() # From the grand parent class
rabbit.sleep()
rabbit.flee()
fish.eat()
fish.sleep()