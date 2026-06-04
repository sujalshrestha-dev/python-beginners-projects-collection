# 🟩 Wordle Game

A CLI version of the popular Wordle game! Guess the secret 5-letter word within 6 attempts.
Get colored hints after every guess to guide you to the answer.

---

## ▶️ How to Run

1. Open the `7. wordle` folder in VS Code
2. Click the **Run ▶ button** on `wordle.py`
3. Start guessing!

---

## 🎮 How to Play

- Guess any **5-letter word** and press Enter
- After each guess you get a color-coded hint:

| Color | Meaning |
|-------|---------|
| 🟩 **Green** | Right letter, right spot |
| 🟨 **Yellow** | Right letter, wrong spot |
| ⬛ **Gray** | Letter not in the word |

- You have **6 attempts** to guess the word
- The secret word is randomly picked from `words.txt`

---

## 📂 Files

| File | Description |
|------|-------------|
| `wordle.py` | Main game script |
| `words.txt` | Word list of 5-letter words |

---

## 🧠 How It Works

- Loads all 5-letter words from `words.txt`
- Picks a random secret word
- After each guess, runs a **two-pass hint check**:
  - First pass finds **green** (correct position)
  - Second pass finds **yellow** (wrong position)
- Handles duplicate letters correctly

---

## 💡 Concepts Used

- File Handling
- Functions
- Loops & Conditionals
- Lists & String Manipulation
- ANSI color codes for terminal colors
- `random` module

---

*by [sujalshrestha-dev](https://github.com/sujalshrestha-dev)*