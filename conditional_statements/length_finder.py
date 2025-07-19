# USERNAME LENGTH VALIDATION

# Take username input from the user
user = input("Enter username: ")

# Check the length of the username
if len(user) < 10:
    print("❌ Username has less than 10 characters!")
elif len(user) == 10:
    print("✅ Username has exactly 10 characters!")
else:
    print("✅ Username has more than 10 characters!")
