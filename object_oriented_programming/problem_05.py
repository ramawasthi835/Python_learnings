# Define a class named vector
class vector:
    # Constructor to initialize vector components
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    # Overload the + operator to add two vectors
    def __add__(self, v2):
        return vector(self.i + v2.i, self.j + v2.j, self.k + v2.k)
    
    # Overload the * operator to compute dot product of two vectors
    def __mul__(self, v2):
        return self.i * v2.i + self.j * v2.j + self.k * v2.k

    # Method to compute cross product of two vectors
    def cross(self, v2):
        i = self.j * v2.k - self.k * v2.j
        j = self.k * v2.i - self.i * v2.k
        k = self.i * v2.j - self.j * v2.i
        return vector(i, j, k)
    
    # String representation of the vector
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
# Create two vector objects
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)

# Print the result of vector addition
print(v1 + v2)

# Print the result of dot product
print(v1 * v2)
