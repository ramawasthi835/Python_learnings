# PROGRAM TO CALCULATE THE SUM OF NATURAL NUMBERS UP TO A GIVEN NUMBER

# Take input from the user
a = int(input("Enter a number to find the sum from 1 up to that number: "))

# Initialize sum variable
sum1 = 0

# Loop through 1 to 'a' and accumulate the sum
for i in range(1, a + 1):
    sum1 += i

# Display the result
print(f"Sum of numbers from 1 to {a} is: {sum1}")
