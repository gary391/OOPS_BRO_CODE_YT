"""
Nested class = A class  defined within another class

class Outer:
    class Inner:

Benefits: Allows you to logically group classes that are closely related
         Enscapsulates private details that aren't relevant outside of the outer class
         keeps the namespace clean; reduces the possibility of naming conflicts.

         ## Note there is a naming collision here, but python will not error out.
"""
from packaging.version import CmpLocalType


#
# class Nonprofile:
#     class Employee:
#         print("This is the second class")


class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} is a {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employee = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position) # Here we are creating Employee object, by passing in name and position.
        self.employee.append(new_employee)

    def list_employee(self):
        return [ f"{employee.get_details()}"for employee in self.employee]

company1 = Company("Google")
print(company1.company_name)
company1.add_employee("John", "Software Engineer")
company1.add_employee("Kelly", "Jr. Software Engineer")
company1.add_employee("Spongebob", "Cook")

for employee in company1.list_employee():
    print(employee)


company2 = Company("Facebook")
company2.add_employee("Johny", "cleaner")
company2.add_employee("Kay", "Mechanic")
company2.add_employee("bob", "developer")

for employee in company2.list_employee():
    print(employee)

