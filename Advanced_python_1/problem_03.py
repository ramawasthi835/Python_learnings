# LIST COMPREHENSION and ERROR HANDLING

try:
    # Taking user input and converting to integer
    a = int(input("Enter a number for its table: "))

    # Generating multiplication table using list comprehension
    table = [a * i for i in range(1, 11)]
    print(table)

    # Appending the table to a file named 'tables.txt'
    with open("tables.txt", "a") as w:
        w.write(f"Table of {a}: {str(table)}\n")

# Handling the case where user input is not a valid integer
except ValueError:
    print("Please enter a valid integer.")

# Handling file-related errors
except FileNotFoundError:
    print("The file 'tables.txt' was not found.")

# Catch-all for any unexpected errors
except Exception as e:
    print(f"An unexpected error occurred: {e}")
