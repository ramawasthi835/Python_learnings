# CLASS DEMONSTRATION: Programmer Info

# Define a class called Programmer
class Programmer:
    # Class attribute shared by all instances
    company = "Microsoft"

    # Constructor to initialize instance attributes
    def __init__(self, name, salary):
        self.name = name        # Instance attribute for name
        self.salary = salary    # Instance attribute for salary

    # Method to display information about the programmer
    def get_info(self):
        print(f"Name is {self.name}, Salary is {self.salary}, working at {self.company}")

# Creating instances (objects) of the Programmer class
employee_1 = Programmer("Ram", 1200000)
employee_2 = Programmer("Ketan", 1000000)

# Calling the method to display info of the first employee
employee_1.get_info()
