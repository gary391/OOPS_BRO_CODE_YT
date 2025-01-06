"""
Class method = Allow operation related to the class itself
               Take(cls) as the fisrt parameter, which represents the class itself.

Instance methods = Best for operations on instances of the class (objects)
Static methods = Best for utility functions that do not need access to class data.
Class methods = Best for class-level data or require access to the class itself.
"""

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # Increase the count variable by 1 when a instance of Student object is created.
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "No student has been created yet"
        else:
            return f"Average GPA: {cls.total_gpa/cls.count:.2f}"


student1 = Student("John", 3.5)
student2 = Student("Jane", 4.0)
student3 = Student("Bob", 3.0)
print(Student.get_count())
print(Student.get_average_gpa())