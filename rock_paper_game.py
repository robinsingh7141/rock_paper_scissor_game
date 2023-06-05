#rock_paper_game
import random

options = ("rock","paper", "scissors")
running = True
while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("you Win!")
    elif player == "paper" and computer == "rock":
        print("you Win!")
    elif player == "scissors" and computer =="paper":
        print("you Win!")
    else:
        print("you lose!")

    if not input("play again ? (y/n): ").lower() == "y":
        running = False
        
print("Thanks for playing!")
