# 💀 Hangman Game

A CLI Hangman game with full ASCII art stages and difficulty modes!
Guess the secret word one letter at a time before the hangman is complete.

---

## ▶️ How to Run

1. Open the `8. hangman` folder in VS Code
2. Click the **Run ▶ button** on `hangman.py`
3. Select a difficulty and start guessing!

---

## 🎮 How to Play

- A secret word is randomly chosen from `words.txt`
- Guess **one letter at a time**
- The hangman drawing grows with every wrong guess
- Reveal the full word before you run out of attempts to win!

---

## ⚙️ Difficulty Modes

| Mode | Attempts |
|------|----------|
| 🟢 Easy | 8 attempts |
| 🟡 Medium | 6 attempts |
| 🔴 Hard | 4 attempts |

---

## 📂 Files

| File | Description |
|------|-------------|
| `hangman.py` | Main game script |
| `words.txt` | Word list for random word selection |

---

## 🎨 ASCII Art Stages

The hangman drawing has **7 stages** and scales automatically to match
the chosen difficulty — so it always fully builds by your last wrong guess.

+---+        +---+        +---+
|   |        |   |        |   |
|        O   |        O   |
|            |       /|\  |
|            |       / \  |
|            |            |
=========    =========    =========
Stage 0      Stage 3      Stage 6

---

## 🧠 How It Works

- Loads words from `words.txt` using `os.path` for reliable file access
- Picks a random secret word
- Tracks guessed letters in a **set** to avoid duplicates
- ASCII stages are **scaled to difficulty** using index mapping
- Validates every input (single letter, not already guessed)

---

## 💡 Concepts Used

- File Handling & `os.path`
- Functions
- Loops & Conditionals
- Sets
- String Manipulation
- Lists & Indexing
- Input Validation
- `random` module

---

*by [sujalshrestha-dev](https://github.com/sujalshrestha-dev)*