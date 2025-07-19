# CHECK IF A POST MENTIONS THE USER'S NAME

# Take user input for the post content
post = input("Enter your post: ")

# Take the user's name
a = input("Enter your name: ")

# Check if the name is mentioned in the post (case-insensitive)
if a.lower() in post.lower():
    print("✅ This post talks about you!")
else:
    print("❌ This post does not talk about you.")
