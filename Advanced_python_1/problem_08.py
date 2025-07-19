# PRINTING LIST ELEMENTS VERTICALLY

# List of numbers (multiples of 7)
lst = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# Convert each number to string and join them with newline character to print vertically
vertical = "\n".join(str(num) for num in lst)

# Print the vertical list
print(vertical)
