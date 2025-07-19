# FUNCTION TO CONVERT INCHES TO CENTIMETERS

def convert(inches):
    # 1 inch = 2.4 cm (approx.)
    return 2.4 * inches

# Take user input in inches
a = int(input("Enter Inches   :"))

# Call the function and print the result with 'cm' label
print(convert(a), 'cm')

