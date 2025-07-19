import math

# CLASS-BASED CALCULATOR IMPLEMENTATION
class Calculator:

    # Static method: Does not depend on class or instance attributes
    @staticmethod
    def greet():
        print("Hello User!!")  # Friendly welcome message

    # Method to calculate the square of a number
    def square(self, num):
        return num * num

    # Method to calculate the cube of a number
    def cube(self, num):
        return num ** 3

    # Method to calculate the square root of a number
    def sqrt(self, num):
        return math.sqrt(num)

# Create an instance of the Calculator class
instance_1 = Calculator()

# Call the static greet method
instance_1.greet()

# Call methods and store the results
a = instance_1.square(2)
print("Square of 2:", a)

b = instance_1.cube(2)
print("Cube of 2:", b)

d = instance_1.sqrt(9)
print("Square root of 9:", d)

        