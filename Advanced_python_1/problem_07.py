# STRING FORMATTING IN PYTHON

# Taking user input
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
number = int(input("Enter your phone number: "))

# Using the format() method to create a formatted string
formatted = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, number)

# Printing the formatted string
print(formatted)
