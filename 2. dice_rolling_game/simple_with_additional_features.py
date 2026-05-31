import random

history = []

while True:
    print("\nOptions: roll | history | clear | quit")
    choice = input("Enter command: ").lower()

    if choice == "roll":
        while True:
            try:
                count = int(input("How many dice? (1-6): "))
                if 1 <= count <= 6:
                    break
                else:
                    print("Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input! Enter a number.")

        rolls = [random.randint(1, 6) for _ in range(count)]
        total = sum(rolls)

        print(f"\n🎲 Rolled {count} dice: {rolls}")
        print(f"Total: {total}")

        history.append({"dice": count, "rolls": rolls, "total": total})

    elif choice == "history":
        if not history:
            print("\nNo rolls yet!")
        else:
            print(f"\n--- Roll History ({len(history)} rolls) ---")
            for i, entry in enumerate(history, 1):
                print(f"{i}. {entry['dice']} dice → {entry['rolls']}  |  Total: {entry['total']}")

    elif choice == "clear":
        history.clear()
        print("History cleared!")

    elif choice == "quit":
        print("Thanks for playing!")
        break

    else:
        print("Invalid command!")