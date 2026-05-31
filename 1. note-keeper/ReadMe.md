# 📝 Note Keeper

A simple command-line note-taking app built with Python. You can add, view, and clear notes — all saved to a local text file.

---

## 🚀 Features

- Add notes and save them to a file
- View all saved notes
- Clear all notes at once
- Basic error handling for file operations

---

## 📁 Project Structure

```
note-keeper/
├── note_keeper.py
└── notes.txt
```

---

## ⚙️ Setup

1. Clone or download the project.
2. Open `note_keeper.py` and update the `FILE_PATH` to match your system:

```python
FILE_PATH = r"C:\Your\Path\Here\notes.txt"
```

3. Run the script:

```bash
python note_keeper.py
```

---

## 🖥️ Usage

When you run the program, you'll see:

```
Options: add | show | clear | quit
Enter command:
```

| Command | Description          |
|---------|----------------------|
| `add`   | Add a new note       |
| `show`  | Display all notes    |
| `clear` | Delete all notes     |
| `quit`  | Exit the program     |

---

## 📌 Example

```
Options: add | show | clear | quit
Enter command: add
Enter your note: Buy groceries
Note added!

Options: add | show | clear | quit
Enter command: show

--- Your Notes ---
Buy groceries
```

---

## 🛠️ Concepts Used

- File handling (`open`, `read`, `write`, `append`)
- Exception handling (`try`, `except`)
- Functions
- Loops and conditionals

---

