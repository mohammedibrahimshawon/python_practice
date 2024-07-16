import random

def choose_word():
    words = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Incorrect guess.")

        if attempts == 0:
            print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_game()
