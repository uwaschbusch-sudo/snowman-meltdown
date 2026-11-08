from ascii_art import STAGES
import game_logic


def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt die Schneemann-Stufe und das Wort an."""
    print(STAGES[mistakes])
    print("Word: ", game_logic.build_display_word(secret_word, guessed_letters))
    print("\n")


def show_guess_result(result, guess):
    """Gibt die Meldung zum Ergebnis eines Tipps aus."""
    if result == "invalid":
        print("Please enter a single valid letter.\n")
    elif result == "repeated":
        print(f"You already guessed '{guess}'. Try a different letter.\n")
    elif result == "correct":
        print(f"Good job! '{guess}' is in the word.\n")
    else:
        print(f"Wrong! '{guess}' is not in the word.\n")


def play_game():
    """Führt eine Spielrunde aus."""
    secret_word = game_logic.get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = game_logic.get_max_mistakes()

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        if game_logic.is_won(secret_word, guessed_letters):
            break

        guess = input("Guess a letter: ").lower()
        result, mistakes = game_logic.process_guess(
            guess, secret_word, guessed_letters, mistakes
        )
        show_guess_result(result, guess)

    display_game_state(mistakes, secret_word, guessed_letters)

    if game_logic.is_won(secret_word, guessed_letters):
        print("Congratulations! You saved the snowman!")
    else:
        print(f"The secret word was: {secret_word}")
        print("Oh no! The snowman completely melted! Game over.")


def main():
    """Steuert das Spiel und die Wiederholungsabfrage."""
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing Snowman Meltdown!")
            break


if __name__ == "__main__":
    main()