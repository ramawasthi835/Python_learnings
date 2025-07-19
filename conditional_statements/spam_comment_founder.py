# SIMPLE SPAM DETECTION IN A USER COMMENT

# Take input from the user
comment = input("Enter your comment: ").lower()  # convert to lowercase for case-insensitive check

# List of common spam phrases
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# Check if any spam phrase is in the comment
if any(phrase in comment for phrase in spam_keywords):
    print("🚨 Spam message detected!")
else:
    print("✅ Congratulations, no spam found!")
