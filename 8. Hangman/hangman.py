import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
words_path = os.path.join(script_dir, "words.txt")

STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]

DIFFICULTY = {
    "1": ("Easy",   8),
    "2": ("Medium", 6),
    "3": ("Hard",   4),
}

def load_words():
    with open(words_path, "r") as f:
        return [line.strip().lower() for line in f if line.strip().isalpha()]

def display(secret, guessed):
    return " ".join(c if c in guessed else "_" for c in secret)

def show_menu():
    print("=" * 35)
    print("         💀 HANGMAN GAME 💀")
    print("=" * 35)
    print("1. Easy   (8 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard   (4 attempts)")
    print("=" * 35)

def get_difficulty():
    while True:
        choice = input("Select difficulty (1-3): ").strip()
        if choice in DIFFICULTY:
            return DIFFICULTY[choice]
        print("Invalid choice, please enter 1, 2, or 3.")

def play():
    show_menu()
    difficulty_name, max_attempts = get_difficulty()

    words = load_words()
    secret = random.choice(words)
    guessed = set()
    wrong = 0

    # Adjust stages to match max_attempts
    stage_indices = [int(i * (len(STAGES) - 1) / max_attempts) for i in range(max_attempts + 1)]

    print(f"\n🎮 Difficulty : {difficulty_name}")
    print(f"📝 The word has {len(secret)} letters\n")

    while wrong < max_attempts:
        print(STAGES[stage_indices[wrong]])
        print(f"\nWord    : {display(secret, guessed)}")
        print(f"Guessed : {', '.join(sorted(guessed)) if guessed else '-'}")
        print(f"Attempts left : {max_attempts - wrong}\n")

        if "_" not in display(secret, guessed):
            print(f"🎉 You won! The word was '{secret.upper()}'")
            return

        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1:
                print("Please enter a single letter!")
            elif not guess.isalpha():
                print("Only letters allowed!")
            elif guess in guessed:
                print("You already guessed that letter!")
            else:
                break

        guessed.add(guess)

        if guess in secret:
            print(f"✅ '{guess}' is in the word!")
        else:
            print(f"❌ '{guess}' is not in the word!")
            wrong += 1

    print(STAGES[-1])
    print(f"\n💀 Game over! The word was '{secret.upper()}'")

play()