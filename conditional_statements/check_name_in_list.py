# NAME LOOKUP IN A LIST

# Predefined list of names
names = ["ram", "divyanshu", "ketan", "sushma", "lokesh"]

# Taking user input
your_name = input("Enter your name: ").strip().lower()

# Check if the entered name exists in the list
if your_name in names:
    print("✅ Name found in the list!")
else:
    print("❌ Name not found in the list!")

# Print the full list for reference
print("Current names in the list:", names)
