import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    print("=== Rock, Paper, Scissors Game ===")
    
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors (or 'q' to quit): ").lower()
        
        if user_choice == "q":
            print("Thanks for playing! Goodbye 👋")
            break
        
        if user_choice not in choices:
            print("❌ Invalid choice! Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("😮 It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scisdsors" and computer_choice == "paper")
        ):
            print("🎉 You win!")
        else:
            print("💀 You lose!")

if __name__ == "__main__":
    play_game()
