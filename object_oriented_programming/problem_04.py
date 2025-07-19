# Define a class to represent complex numbers
class complex:
    # Constructor to initialize real and imaginary parts
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    # Overload the + operator to add two complex numbers
    def __add__(self, c2):
        return complex(self.real + c2.real, self.imaginary + c2.imaginary)
    
    # Overload the * operator to multiply two complex numbers
    def __mul__(self, c2):
        # (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        real_part = self.real * c2.real - self.imaginary * c2.imaginary
        imaginary_part = self.real * c2.imaginary + self.imaginary * c2.real
        return complex(real_part, imaginary_part)
    
    # String representation of the complex number
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
# Create two complex number instances
c1 = complex(1, 2)
c2 = complex(3, 4)

# Add the two complex numbers (not printed)
c3 = c1 + c2

# Multiply the two complex numbers and print the result
print(c1 * c2)
