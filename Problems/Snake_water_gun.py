import random

# Computer randomly selects 1 (snake), 2 (water), or 3 (gun)
computer = random.choice([1, 2, 3])

# User enters their move
user_move = input("Enter your move (snake:s, water:w, gun:g)   :")

# Dictionary to map user's input to numeric values
moves = {"s": 1, "w": 2, "g": 3}

# Get the numeric value of the user's move
move = moves.get(user_move)

# Check for tie
if(computer == move):
    print("Tied")
else:
    # All possible win/lose conditions
    if(computer == 1 and move == 2):
        print("You lose")  # Snake drinks water
    elif(computer == 1 and move == 3):
        print("You win")   # Gun kills snake

    elif(computer == 2 and move == 1):
        print("You win")   # Snake drinks water
    elif(computer == 2 and move == 3):
        print("You lose")  # Water douses gun

    elif(computer == 3 and move == 1):
        print("You lose")  # Gun kills snake
    elif(computer == 3 and move == 2):
        print("You Win")   # Water douses gun

    else:
        # Handles invalid inputs or unexpected errors
        print("Error occurred!!")

    
