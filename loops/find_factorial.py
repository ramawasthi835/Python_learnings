# PROGRAM TO CALCULATE FACTORIAL OF A GIVEN NUMBER

# Take input from the user
a = int(input("Enter a number to calculate its factorial: "))

# Initialize product to 1
product = 1

# Multiply numbers from 1 to 'a'
for i in range(1, a + 1):
    product *= i

# Display the result
print(f"Factorial of {a} is: {product}")
