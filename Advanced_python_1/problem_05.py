# FUNCTION TO GENERATE AND SAVE MULTIPLICATION TABLES

# Define a function that generates the multiplication table for a given number
def printer(a):
    # List comprehension to generate the table (1 to 10)
    table = [a * i for i in range(1, 11)]

    # Append the table to 'tables.txt' file
    with open("tables.txt", "a") as w:
        w.write(f"Table of {a}: {str(table)}\n")

# Generate multiplication tables for numbers from 100 to 10000 (inclusive)
for i in range(100, 10001):
    printer(i)
