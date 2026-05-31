import random


# ─────────────────────────────────────────
#  GAME 1 — 2-Player Battle
# ─────────────────────────────────────────
def two_player_battle():
    print("\n🎮 2-Player Battle — Highest roll wins!\n")
    scores = {"Player 1": 0, "Player 2": 0}
    rounds = 0

    while True:
        try:
            rounds = int(input("How many rounds? (1-10): "))
            if 1 <= rounds <= 10:
                break
            print("Enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input!")

    for r in range(1, rounds + 1):
        print(f"\n--- Round {r} ---")
        for player in ["Player 1", "Player 2"]:
            input(f"{player}, press Enter to roll...")
            roll = random.randint(1, 6)
            print(f"{player} rolled: {roll} 🎲")
            scores[player] += roll

        if scores["Player 1"] > scores["Player 2"]:
            print(f"Round winner: Player 1")
        elif scores["Player 2"] > scores["Player 1"]:
            print(f"Round winner: Player 2")
        else:
            print("Round tied!")

    print("\n🏆 Final Scores:")
    for player, score in scores.items():
        print(f"  {player}: {score}")

    if scores["Player 1"] > scores["Player 2"]:
        print("\n🎉 Player 1 wins the game!")
    elif scores["Player 2"] > scores["Player 1"]:
        print("\n🎉 Player 2 wins the game!")
    else:
        print("\n🤝 It's a tie!")


# ─────────────────────────────────────────
#  GAME 2 — Pig Game
# ─────────────────────────────────────────
def pig_game():
    print("\n🐷 Pig Game — First to 100 wins!")
    print("Roll to earn points, but rolling a 1 loses your turn points!\n")

    scores = {"Player 1": 0, "Player 2": 0}
    players = ["Player 1", "Player 2"]
    current = 0

    while max(scores.values()) < 100:
        player = players[current]
        turn_score = 0
        print(f"\n{'─'*30}")
        print(f"🎯 {player}'s turn  |  Total: {scores[player]}")
        print(f"{'─'*30}")

        while True:
            action = input("Roll or Hold? (r/h): ").lower()

            if action == "r":
                roll = random.randint(1, 6)
                print(f"  Rolled: {roll} 🎲")

                if roll == 1:
                    print("  💀 Rolled a 1! Turn score lost.")
                    turn_score = 0
                    break
                else:
                    turn_score += roll
                    print(f"  Turn score: {turn_score}  |  Banked: {scores[player]}")

            elif action == "h":
                scores[player] += turn_score
                print(f"  ✅ Held! {player} banks {turn_score}. Total: {scores[player]}")
                break

            else:
                print("  Enter 'r' to roll or 'h' to hold.")

        if scores[player] >= 100:
            print(f"\n🎉 {player} reached {scores[player]} points and wins!")
            break

        current = 1 - current  # switch player

    print("\n🏆 Final Scores:")
    for player, score in scores.items():
        print(f"  {player}: {score}")


# ─────────────────────────────────────────
#  GAME 3 — 21 Dice Game
# ─────────────────────────────────────────
def game_21():
    print("\n🎯 21 Dice Game — Get closest to 21 without busting!")
    print("You go first, then the computer plays.\n")

    # Player's turn
    player_total = 0
    print("--- Your Turn ---")
    while True:
        action = input(f"Total: {player_total} | Roll or Hold? (r/h): ").lower()

        if action == "r":
            roll = random.randint(1, 6)
            player_total += roll
            print(f"  Rolled: {roll} 🎲  |  Total: {player_total}")

            if player_total > 21:
                print("  💥 Busted! You went over 21.")
                break
            elif player_total == 21:
                print("  🎯 Perfect 21!")
                break

        elif action == "h":
            print(f"  ✅ You hold at {player_total}.")
            break
        else:
            print("  Enter 'r' to roll or 'h' to hold.")

    # Computer's turn
    print("\n--- Computer's Turn ---")
    computer_total = 0
    while computer_total < 17:  # computer rolls until 17+
        roll = random.randint(1, 6)
        computer_total += roll
        print(f"  Computer rolled: {roll} 🎲  |  Total: {computer_total}")

    if computer_total > 21:
        print("  💥 Computer busted!")
    else:
        print(f"  Computer holds at {computer_total}.")

    # Result
    print(f"\n📊 You: {player_total}  |  Computer: {computer_total}")

    if player_total > 21:
        print("🏆 Computer wins! You busted.")
    elif computer_total > 21:
        print("🏆 You win! Computer busted.")
    elif player_total > computer_total:
        print("🏆 You win!")
    elif computer_total > player_total:
        print("🏆 Computer wins!")
    else:
        print("🤝 It's a tie!")


# ─────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────
def main():
    print("=" * 40)
    print("       🎲 DICE ROLLING GAMES 🎲")
    print("=" * 40)

    while True:
        print("\nSelect a game:")
        print("  1. 2-Player Battle")
        print("  2. Pig Game")
        print("  3. 21 Dice Game")
        print("  q. Quit")

        choice = input("\nEnter choice: ").lower()

        if choice == "1":
            two_player_battle()
        elif choice == "2":
            pig_game()
        elif choice == "3":
            game_21()
        elif choice == "q":
            print("\nThanks for playing! 👋")
            break
        else:
            print("Invalid choice!")

        again = input("\nBack to menu? (y/n): ").lower()
        if again != "y":
            print("\nThanks for playing! 👋")
            break


main()