# PROGRAM TO FIND THE GREATEST OF FOUR NUMBERS

# Taking four numbers as input from the user
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

# Check and print which number is the greatest
if a > b and a > c and a > d:
    print(f"{a} is the greatest number!")
elif b > a and b > c and b > d:
    print(f"{b} is the greatest number!")
elif c > a and c > b and c > d:
    print(f"{c} is the greatest number!")
elif d > a and d > b and d > c:
    print(f"{d} is the greatest number!")
else:
    print("There is a tie or all numbers are equal.")
