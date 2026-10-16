# game_logic.py
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage and the secret word with underscores for unguessed letters."""
    print(STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    # Game loop
    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check if all letters of the secret word have been guessed
        won = True
        for letter in secret_word:
            if letter not in guessed_letters:
                won = False
                break
        if won:
            break

        # Prompt user for a guess
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        # Add guess to list of guessed letters
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
        else:
            mistakes += 1
            print(f"Wrong! '{guess}' is not in the word.\n")

    # Final display and end message
    display_game_state(mistakes, secret_word, guessed_letters)

    # Win / Loss check
    won = all(letter in guessed_letters for letter in secret_word)
    if won:
        print("Congratulations! You saved the snowman!")
    else:
        print("Oh no! The snowman completely melted! Game over.")


if __name__ == "__main__":
    play_game()
