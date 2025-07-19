import random 
import os

# Function that executes a single round of the game
def game():
    moves = {"s": 1, "w": 2, "g": 3}  # Mapping user input to numbers
    user_move = input("Enter your move(snake:s, water:w, gun:g)   :")
    computer = random.choice([1, 2, 3])  # Random move by computer
    move = moves.get(user_move)  # Convert user move to number

    if(computer == move):  # Tie condition
        return 2
    else:
        # Game logic: comparing user move and computer move
        if(computer == 1 and move == 2):
            print("You lose")
            return 0
        elif(computer == 1 and move == 3):
            print("You win")
            return 1
        elif(computer == 2 and move == 1):
            print("You win")
            return 1
        elif(computer == 2 and move == 3):
            print("You lose")
            return 0
        elif(computer == 3 and move == 1):
            print("You lose")
            return 0
        elif(computer == 3 and move == 2):
            print("You Win")
            return 1
        else:
            print("Error occured!!")
            return 0

# Ask user whether to play or not
play = int(input("Hello Player!!!\n If you wish to play the game enter 1 or to exit enter 0   :"))

streak = 0  # Initialize current win streak

# Read high score from file
with open("Hi-Score.txt", "r") as r:
    max_streak = r.read()
max_streak = int(max_streak)

# Loop until user exits
while(play == 1):
    a = game()  # Play a round
    if(a == 1):  # Player wins
        streak += 1
        print("Streak=", streak)
    elif(a == 0):  # Player loses
        print("Oopss!!!! Streak Broke...")
        streak = 0
        print("Streak=", streak)
    elif(a == 2):  # Tie
        print(f"Game Tied!!\n Streak={streak}")
    else:  # Any unexpected return
        print("Error")
    
    # Ask again if player wants to continue
    play = int(input("Hello Player!!!\n If you wish to play the game enter 1 or to exit enter 0   :"))

# After game loop, check if current streak is a new high score
if(streak > max_streak):
    with open("Hi-Score.txt", "w") as f:
        f.write(str(streak))
    print("Congratulations! New High Score:", streak)
else:
    print("Your Final Streak:", streak)
    print("High Score remains:", max_streak)
