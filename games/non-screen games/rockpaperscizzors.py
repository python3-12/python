import random

choices = ["rock", "paper", "scissors"]
wins = 0
losses = 0

# Track the player's history in-memory only
player_history = {"rock": 0, "paper": 0, "scissors": 0}

def get_computer_choice():
    # If no history yet, pick randomly
    total = sum(player_history.values())
    if total == 0:
        return random.choice(choices)
    
    # Predict the player's next move based on history
    predicted_player = max(player_history, key=player_history.get)
    
    # Computer chooses the winning move against predicted player move
    if predicted_player == "rock":
        return "paper"
    elif predicted_player == "paper":
        return "scissors"
    else:
        return "rock"

def determine_winner(player, computer):
    global wins, losses
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        wins += 1
        return "You win!"
    else:
        losses += 1
        return "Computer wins!"

def play_game():
    print("Welcome to rock, paper, scissors!")
    while True:
        player_choice = input("\nEnter rock, paper, or scissors (or 'quit' to stop, 'score' to view score): ").lower()
        
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        if player_choice == "score":
            print(f"Wins: {wins} Losses: {losses}")
            continue
        
        if player_choice not in choices:
            print("Invalid choice. Try again.")
            continue
            
        # Update in-memory history
        player_history[player_choice] += 1 
        
        computer_choice = get_computer_choice()
        
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)

# Run the smart game
play_game()
