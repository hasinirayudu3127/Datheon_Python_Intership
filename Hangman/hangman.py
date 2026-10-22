import random
from pathlib import Path

# Name of the word list file
WORD_FILE = "google-10000-english-no-swears.txt"

# Load words from the provided text file
def load_words():
    file_path = Path(__file__).parent / WORD_FILE

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = [
                line.strip().lower()
                for line in file
                if line.strip().isalpha() and len(line.strip()) >= 4
            ]

        if not words:
            raise ValueError("The word list is empty.")

        return words

    except FileNotFoundError:
        print(f"Error: Could not find '{WORD_FILE}'.")
        print("Place the text file in the same folder as hangman.py.")
        raise SystemExit(1)


# Hangman drawings: index 0 = no wrong guesses, index 6 = game over
stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def play_hangman():
    words = load_words()
    word = random.choice(words)

    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("=" * 35)
    print("     HANGMAN WORD GUESSING GAME")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {max_attempts} wrong guesses available.")

    while wrong_guesses < max_attempts:
        # Display guessed letters and blanks
        display = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )

        print("\nWord:", display)
        print("Guessed letters:", " ".join(sorted(guessed_letters))
              if guessed_letters else "None")
        print(f"Wrong guesses: {wrong_guesses}/{max_attempts}")
        print(stages[wrong_guesses])

        # Check whether the player has won
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            print("You win!")
            return

        guess = input("Enter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter one letter only.")
            continue

        # Prevent repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another!")
            continue

        guessed_letters.add(guess)

        # Check the guess
        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Incorrect guess!")

    # Display final state when attempts run out
    print(stages[max_attempts])
    print("\nGame over! The word was:", word)
    print("Better luck next time!")


if __name__ == "__main__":
    play_hangman()