import random

# Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def load_words(filename):
    with open(filename, "r") as f:
        words = [line.strip().lower() for line in f if len(line.strip()) == 5]
    return words

def get_hint(guess, secret):
    hint = []
    secret_list = list(secret)
    guess_list = list(guess)
    result = ["gray"] * 5

    # First pass - green
    for i in range(5):
        if guess_list[i] == secret_list[i]:
            result[i] = "green"
            secret_list[i] = None
            guess_list[i] = None

    # Second pass - yellow
    for i in range(5):
        if guess_list[i] is not None and guess_list[i] in secret_list:
            result[i] = "yellow"
            secret_list[secret_list.index(guess_list[i])] = None

    # Build colored output
    for i in range(5):
        char = guess[i].upper()
        if result[i] == "green":
            hint.append(f"{GREEN}{BOLD} {char} {RESET}")
        elif result[i] == "yellow":
            hint.append(f"{YELLOW}{BOLD} {char} {RESET}")
        else:
            hint.append(f"{GRAY}{BOLD} {char} {RESET}")

    return "".join(hint), result

def print_legend():
    print(f"{GREEN}{BOLD} A {RESET} = Correct spot")
    print(f"{YELLOW}{BOLD} A {RESET} = Wrong spot")
    print(f"{GRAY}{BOLD} A {RESET} = Not in word")
    print()

def play():
    words = load_words("words.txt")
    secret = random.choice(words)
    attempts = 6

    print("=" * 35)
    print("         🟩 WORDLE GAME 🟩")
    print("=" * 35)
    print("Guess the 5-letter word!")
    print()
    print_legend()

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{attempts}: ").strip().lower()
            if len(guess) != 5:
                print("Please enter a 5-letter word!")
            elif not guess.isalpha():
                print("Only letters allowed!")
            else:
                break

        hint, result = get_hint(guess, secret)
        print("Result : " + hint)
        print()

        if result == ["green"] * 5:
            print(f"🎉 You got it in {attempt} attempt(s)! The word was '{secret.upper()}'")
            return

    print(f"😢 Out of attempts! The word was '{secret.upper()}'")

play()