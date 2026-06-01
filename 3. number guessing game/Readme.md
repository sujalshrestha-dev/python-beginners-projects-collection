# 🔢 Number Guessing Game

A classic number guessing game where you try to guess a randomly generated number between 0 and 100 within a limited number of attempts.

---

## 🚀 How to Run

```bash
python number_guessing_game.py
```

---

## 🎮 How to Play

1. Choose how many guesses you want (1–10)
2. The program picks a random number between **0 and 100**
3. Enter your guess each round
4. The game tells you if your guess is too high, too low, or correct
5. Guess the number before you run out of attempts!

---

## 🖥️ Example

```
Welcome to the Number Guessing Game!
Guess a number between 0 and 100.

How many guesses do you want? (1-10): 5
Guess 1: 50
The guessed number is too high!
Guess 2: 25
The guessed number is low.
Guess 3: 35
The guessed number is high.
Guess 4: 30
🎉 You guessed it in 4 tries!
```

---

## 💡 Hints System

| Message | Meaning |
|---------|---------|
| `too high` | More than 10 above the number |
| `high` | Within 10 above the number |
| `too low` | More than 10 below the number |
| `low` | Within 10 below the number |

---

## 🛠️ Concepts Used

- `random` module
- Functions
- Loops & conditionals
- Exception handling (`try` / `except`)
- Input validation

---

*Part of the [python-beginners-projects-collection](https://github.com/sujalshrestha-dev/python-beginners-projects-collection) repository.*