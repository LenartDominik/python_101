import random

print("Welcome to the game: 'Paper, Rock, Scissors'. Let's play! ")

picks = ("rock", "paper", "scissors")

    
while True:    
    player = None
    computer = random.choice(picks)
    
    while player not in picks:
        player = input("Enter one pick of these three: (rock, paper, scissors): ").strip().lower()
   

    print(f"Player choice: {player}")
    print(f"Computer choice: {computer}")
    
    if player == computer:
        print("It's a draw!")
    elif player == "paper" and computer == "rock":
        print("Congratulations. You won")
    elif player == "rock" and computer == "scissors":
        print("Congratulations. You won!")
    elif player == "scissors" and computer == "paper":
        print("Congratulations. You won!")
    else:
        print("Unfortunately, you lost!")
        
    play_again = input("Do you want to play again? Type 'yes' to play or 'exit' to quit: ").strip().lower()
    if play_again == "exit":
        print("Thanks for playing!")
        break
    elif play_again == "yes":
        print("Let's play again!")
    else:
        print("Invalid input. Please type 'yes' to play or 'exit' to quit.")
