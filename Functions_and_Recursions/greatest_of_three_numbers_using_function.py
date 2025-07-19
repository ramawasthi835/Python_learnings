# FUNCTION TO FIND THE GREATEST OF THREE NUMBERS

def great(a, b, c):
    # Check if 'a' is the greatest
    if a > b and a > c:
        print(f"{a} is greatest!!", end=" ")
    # Check if 'b' is the greatest
    elif b > a and b > c:
        print(f"{b} is greatest!!!")
    # Check if 'c' is the greatest
    elif c > a and c > b:
        print(f"{c} is greatest!!")
    # If none of the above, inputs might be equal
    else:
        print("Invalid Input!!")

# Take 3 numbers as input from the user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

# Call the function with input values
great(num1, num2, num3)

