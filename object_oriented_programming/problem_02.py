# Multilevel inheritance

# Base class
class animal:
    def breed(self):
        print("This is a dog")

# Intermediate class inheriting from animal
class pets(animal):
    pass  # No additional methods or attributes

# Derived class inheriting from pets (which inherits from animal)
class dog(pets):
    
    # Static method to simulate barking
    @staticmethod
    def bark():
        print("bhooo!!! bhooo!!")

# Creating an instance of the most derived class
pitbull = dog()

# Calling inherited method from animal class
pitbull.breed()

# Calling static method defined in dog class
pitbull.bark()

