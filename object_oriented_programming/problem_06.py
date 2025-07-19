# NUMBER GUESSING GAME
# The program generates a random number between 1 and 9.
# The user has to guess the number, with hints provided.

from random import randint

# Generate a random key between 1 and 9
key = randint(1, 9)

# Initialize guess counter and placeholder
count = 0
guess = 0

# Loop until the correct number is guessed
while guess != key:
    count += 1
    guess = int(input("Guess any number between 1 to 9: "))
    
    if guess == key:
        print(f"You guessed the number!!!\nNumber = {key}\nAttempts = {count}")
    else:
        # Give a hint based on the guess
        if guess > key:
            print("Hint: Guess lower")
        else:
            print("Hint: Guess higher")


