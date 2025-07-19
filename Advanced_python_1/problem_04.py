# ERROR HANDLING: Division with Zero Check

# Taking two integers as input from the user
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

# Using try-except to handle division and catch possible errors
try:
    # Attempt to divide a by b
    print(a / b)

# Handling the case where b is zero
except ZeroDivisionError:
    print("Error: We cannot divide a number by zero.")
