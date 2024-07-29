import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    previous_guesses = []
    attempts = 0

    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        previous_guesses.append(guess)

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

        print(f"Previous guesses: {previous_guesses}")

if __name__ == "__main__":
    guess_the_number()
