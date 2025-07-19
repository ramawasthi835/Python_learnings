# Defining a class for 2D vector
class twoD_vector: 
    def __init__(self, x=1, y=2):
        self.x = x  # Initialize x
        self.y = y  # Initialize y

    def show(self):
        # This will try to print x, y, and z
        # Note: z is not defined in this class but is expected in subclass
        print(f"Value of x is {self.x} and value of y is {self.y} and value of z is {self.z}")

# Subclass for 3D vector, inheriting from twoD_vector
class threeD_vector(twoD_vector):
    def __init__(self, x, y, z):
        # Initializes x, y, z directly (instead of calling super().__init__)
        self.x = x
        self.y = y
        self.z = z  # z is unique to 3D vector

    # Optional: show() could be overridden here but it relies on parent class method

# Creating object of threeD_vector
a = threeD_vector(4, 5, 6)

# Calling show method (inherited from twoD_vector)
a.show()

    


