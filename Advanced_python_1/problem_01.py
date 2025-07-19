# ERROR HANDLING

# Using try-except to catch file-related errors
try:
    # Attempt to open and read from 'file1.txt'
    with open("file1.txt", "r") as r1:
        print(r1.read)  # ⚠️ This will print a reference to the read method, not the file content

    # Attempt to open and read from 'file.txt'
    with open("file.txt", "r") as r2:
        print(r2.read())  # Correct usage: call read() with parentheses

    # Again trying to open 'file.txt' (redundant; same as above)
    with open("file.txt", "r") as r3:
        print(r3.read())  # Reads the file content again

# Catching specific error if any of the files are not found
except FileNotFoundError as e:
    print("File does not exist")  # Friendly message to user
