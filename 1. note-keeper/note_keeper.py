FILE_PATH = r"C:\Users\shres\Documents\2 Projects\Python beginner Projects collection\1. note-keeper\notes.txt"


def add_note():
    note = input("Enter your note: ")
    try:
        with open(FILE_PATH, "a") as file:
            file.write(note + "\n")
        print("Note added!\n")
    except Exception as e:
        print("Error:", e)


def show_notes():
    try:
        with open(FILE_PATH, "r") as file:
            content = file.read()
            if content:
                print("\n--- Your Notes ---")
                print(content)
            else:
                print("No notes found.\n")
    except FileNotFoundError:
        print("No notes file exists yet.\n")
    except Exception as e:
        print("Error:", e)


def clear_notes():
    try:
        with open(FILE_PATH, "w") as file:
            pass
        print("All notes cleared!\n")
    except Exception as e:
        print("Error:", e)


while True:
    try:
        print("Options: add | show | clear | quit")
        choice = input("Enter command: ").lower()

        if choice == "add":
            add_note()

        elif choice == "show":
            show_notes()

        elif choice == "clear":
            clear_notes()

        elif choice == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid command!\n")

    except Exception as e:
        print("Error:", e)