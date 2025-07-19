# HINDI TO ENGLISH DICTIONARY PROGRAM

# Predefined translation dictionary
translation = {
    "namaste": "hello",
    "waha": "there",
    "yaha": "here",
    "subha": "morning",
    "raat": "night"
}

# Display available Hindi words
print("""
🗣️ Hindi to English Translation Dictionary 🗣️
Choose one of the following Hindi words to get its English translation:

1. namaste
2. waha
3. yaha
4. subha
5. raat
""")

# Take user input
word = input("Enter the Hindi word to translate: ").strip().lower()

# Display translation if available
meaning = translation.get(word)
if meaning:
    print(f"✅ The word **'{word}'** translates to **'{meaning}'** in English.")
else:
    print("❌ Sorry, that word is not in the dictionary.")
