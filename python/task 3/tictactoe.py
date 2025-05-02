import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    if winner == "tie":
        print("Result: It's a tie!")
    elif winner == "user":
        print("🎉 You win this round!")
    else:
        print("💻 Computer wins this round!")

def main():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.")

    while True:
        user_choice = input("\nYour move: ").lower()
        if user_choice == "exit":
            print("\nThanks for playing!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()