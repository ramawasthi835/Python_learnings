from functools import reduce

# Original list
l = [1, 2, 3, 4, 5, 6]

# ----------------------------
# MAPPING: Apply a function to all items in a list
# ----------------------------

# Define a lambda function to square a number
square = lambda x: x * x

# Apply the square function to each element of the list using map
squared_l = map(square, l)

# Convert map object to list and print
print("Squares of list elements:", list(squared_l))

# ----------------------------
# FILTERING: Filter elements based on a condition
# ----------------------------

# Function to check if a number is even
def ifeven(n):
    return n % 2 == 0

# Use filter to keep only even numbers
evens = filter(ifeven, l)
print("Even numbers in the list:", list(evens))

# ----------------------------
# REDUCING: Combine elements of the list into a single value
# ----------------------------

# Define a lambda function to subtract elements in sequence
sub = lambda x, y: x - y

# Reduce applies the sub function cumulatively: (((((1 - 2) - 3) - 4) - 5) - 6)
print("Cumulative subtraction of list elements:", reduce(sub, l))


