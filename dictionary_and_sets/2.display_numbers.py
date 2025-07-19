# PROGRAM TO COLLECT UNIQUE NUMBERS INTO A SET

# Create an empty set to store unique numbers
unique_numbers = set()

# Ask user how many numbers to enter
n = int(input("How many numbers do you want to add? "))

# Loop to take 'n' inputs from user
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    unique_numbers.add(num)  # Automatically avoids duplicates

# Display the unique numbers entered
print("\nUnique numbers entered:")
print(unique_numbers)
