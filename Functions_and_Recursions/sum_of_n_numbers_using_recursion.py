# FUNCTION TO CALCULATE SUM OF FIRST 'n' NATURAL NUMBERS RECURSIVELY

def sum(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    else:
        # Recursive case: sum of n and the sum of numbers before it
        return n + sum(n - 1)

# Take input from the user
a = int(input("Enter a number:    "))

# Call the function and display the result
print("Sum is:", sum(a))
