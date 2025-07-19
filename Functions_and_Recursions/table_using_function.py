# FUNCTION TO PRINT MULTIPLICATION TABLE OF A GIVEN NUMBER

def table(n):
    # Loop through numbers 1 to 10
    for i in range(1, 11):
        # Print formatted multiplication result
        print(f"{n} * {i} = {n * i}")

# Take input from the user
n = int(input("Enter the number for its table: "))

# Call the function
table(n)
