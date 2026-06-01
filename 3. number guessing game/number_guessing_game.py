import random


def check(number, main_number):
    if number == main_number:
        return True
    elif number > main_number:
        if (number - main_number) > 10:
            print("The guessed number is too high!")
        else:
            print("The guessed number is high.")
    else:
        if (main_number - number) > 10:
            print("The guessed number is too low!")
        else:
            print("The guessed number is low.")
    return False


print("Welcome to the Number Guessing Game!")
print("Guess a number between 0 and 100.\n")

# Get max guesses
while True:
    try:
        max_guesses = int(input("How many guesses do you want? (1-10): "))

        if max_guesses < 1:
            print("Number of guesses must be at least 1.")
        elif max_guesses > 10:
            print("Number of guesses cannot be greater than 10.")
        else:
            break

    except ValueError:
        print("Please enter numbers only.")


main_number = random.randint(0, 100)

for guessed in range(1, max_guesses + 1):

    # Get valid guess
    while True:
        try:
            number = int(input(f"Guess {guessed}: "))

            if number < 0 or number > 100:
                print("Please enter a number between 0 and 100.")
            else:
                break

        except ValueError:
            print("Please enter numbers only.")

    if check(number, main_number):
        print(f"🎉 You guessed it in {guessed} try!")
        break

    elif guessed == max_guesses:
        print(f"❌ You failed! The number was {main_number}.")