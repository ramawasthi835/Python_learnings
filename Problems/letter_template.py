# Printing a template message with placeholders
print('''
Dear [Your name]
You are selected!!!!
[Date]''')

# Taking user's name as input
name = input("Enter your name: ")

# Taking date as input
date = input("Enter date: ")

# Printing the final message with user inputs
print(f'''
Dear {name}
You are selected!!!!
{date}''')

