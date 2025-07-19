# FILTERING NUMBERS DIVISIBLE BY 5

# Original list of integers
lst = [1, 7, 4, 7, 5, 15, 100, 65, 67, 90, 8]

# Define a function that returns True for numbers divisible by 5
def filte(x):
    return x % 5 == 0  # Cleaned up the condition

# Use filter() to get only those numbers from the list that are divisible by 5
filtered = filter(filte, lst)

# Convert the filtered object to a list and print it
print("Numbers divisible by 5:", list(filtered))
