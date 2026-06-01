import random

print("Welcome to Rock, Paper, Scissors")
print("Choose a match type:")
print("1. Best of 2")
print("2. Best of 3")
print("3. Best of 5")

while True:
    try:
        choice = int(input("Choose option (1/2/3): "))

        match choice:
            case 1:
                target_wins = 1
                print("First to 1 win wins the match.")
                break

            case 2:
                target_wins = 2
                print("First to 2 wins wins the match.")
                break

            case 3:
                target_wins = 3
                print("First to 3 wins wins the match.")
                break

            case _:
                print("Please choose 1, 2, or 3.")

    except ValueError:
        print("Please enter a number.")

print("\nLet's start...\n")

choices = ["rock", "paper", "scissors"]

user_wins = 0
computer_wins = 0

while user_wins < target_wins and computer_wins < target_wins:

    computer_choice = random.choice(choices)

    user_choice = input(
        "Rock, Paper, Scissors (or r/p/s): "
    ).lower().strip()

    if user_choice not in ["rock", "paper", "scissors", "r", "p", "s"]:
        print("Invalid choice! Try again.\n")
        continue

    # Convert shortcuts to full words
    if user_choice == "r":
        user_choice = "rock"
    elif user_choice == "p":
        user_choice = "paper"
    elif user_choice == "s":
        user_choice = "scissors"

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        user_wins += 1

    else:
        print("Computer wins this round!")
        computer_wins += 1

    print(f"Score: You {user_wins} - {computer_wins} Computer\n")

if user_wins == target_wins:
    print("🎉 Congratulations! You won the match!")
else:
    print("❌ Computer won the match!")