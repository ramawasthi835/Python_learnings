# PROGRAM TO PRINT THE MULTIPLICATION TABLE OF A GIVEN NUMBER USING A WHILE LOOP

# Take input from the user
a = int(input("Enter a number for its table       : "))

# Initialize counter
i = 1

# Loop to print the table from 1 to 10
while i <= 10:
    print(f"{a} * {i} = {a * i}")
    i += 1
