import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Wählt ein zufälliges Wort aus der Liste."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def get_max_mistakes():
    """Gibt die maximale Anzahl an Fehlern zurück."""
    return len(STAGES) - 1


def build_display_word(secret_word, guessed_letters):
    """Baut das Wort mit Unterstrichen für fehlende Buchstaben."""
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    return display_word


def is_won(secret_word, guessed_letters):
    """Prüft, ob alle Buchstaben erraten wurden."""
    return all(letter in guessed_letters for letter in secret_word)


def process_guess(guess, secret_word, guessed_letters, mistakes):
    """Wertet einen Tipp aus und gibt (Ergebnis, Fehleranzahl) zurück."""
    if len(guess) != 1 or not guess.isalpha():
        return "invalid", mistakes
    if guess in guessed_letters:
        return "repeated", mistakes
    guessed_letters.append(guess)
    if guess in secret_word:
        return "correct", mistakes
    return "wrong", mistakes + 1