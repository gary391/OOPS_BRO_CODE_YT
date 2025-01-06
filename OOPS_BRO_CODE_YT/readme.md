class variable = Shared among all instances of a class
                Defined outside the constructor
                Allow you to share data among all object created from that class


Inheritance = Allows a class to inherit attribute and methods from another clas 
              Helps with code reusablility and extensiblility
              class Child (Parent)

Multiple Inheritance = inherit from more than one parent class C(A,B)
                        C(A,B) - In python we can have multiple parents.
Multilevel Inheritance = inherit from a parent which inherits from another parent
                        C(B) <- B(A) <- A
                        Here C as the child, B as the parent and A as the grandparent.

Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed. 
                They can contain abstract methods, which are declared but have no implementation. 
                Abstract classes benefits:
                1. Prevents instantiation of the class itself
                2. Requires children to use inherited abstract methods
                - Abstract class are incomplete so we don't want to create an object from an abstract class.

Super() = Function used in a child class to call methods from a parent class (superclass). Allows you 
          you to extend the functionality of the inherited methods