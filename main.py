import random

# Die ASCII-Art-Stufen des schmelzenden Schneemanns (von intakt bis zum Ende)
SNOWMAN_STAGES = [
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    """
     ___  
    /___\\ 
    (o o) 
    """,
    """
     ___  
    /___\\ 
    """
]

WORD_LIST = ["snowman", "python", "winter", "schnee"]


def play_game():
    secret_word = random.choice(WORD_LIST)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = len(SNOWMAN_STAGES) - 1

    print("Welcome to Snowman Meltdown!\n")

    while incorrect_guesses < max_incorrect:
        # Aktuellen Schneemann anzeigen
        print(SNOWMAN_STAGES[incorrect_guesses])

        # Wortfortschritt anzeigen (z. B. _ _ _ _ _ _ _)
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"Word:  {display_word}\n")

        # Überprüfen, ob das Wort komplett erraten wurde
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations, you win!")
            return

        # Eingabe vom Spieler
        guess = input("Guess a letter: ").lower().strip()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Bitte gib einen einzelnen gültigen Buchstaben ein.\n")
            continue

        if guess in guessed_letters:
            print("Du hast diesen Buchstaben bereits geraten!\n")
            continue

        guessed_letters.add(guess)

        # Prüfen, ob der Buchstabe im Wort ist
        if guess not in secret_word:
            incorrect_guesses += 1

    # Spiel verloren (maximale Fehlversuche erreicht)
    print(SNOWMAN_STAGES[incorrect_guesses])
    print(f"Game Over! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()