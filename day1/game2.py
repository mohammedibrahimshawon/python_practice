import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

    while True:
        user_choice = input("Your choice: ").lower()

        if user_choice == 'quit':
            print("Thanks for playing! Goodbye!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

        computer_choice = random.choice(choices)

if __name__ == "__main__":
    play_game()
