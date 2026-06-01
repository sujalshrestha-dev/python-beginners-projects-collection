# ⏱️ Timed Math Challenge

A CLI math quiz game that tests your arithmetic skills against the clock!
Choose your operation mode, set the number of problems, and see how fast you can solve them.

---

## ▶️ How to Run

1. Open the project folder in VS Code
2. Click the **Run ▶ button** on `timed_math_challenge.py`
3. Select a mode and number of problems
4. Solve as fast as you can!

---

## 🎮 Game Modes

| # | Mode |
|---|------|
| 1 | Only Addition |
| 2 | Only Subtraction |
| 3 | Only Multiplication |
| 4 | All Operations (Mixed) |

---

## 📊 Results Screen

At the end of the quiz you'll see:
- ✅ Total correct answers
- ❌ Total wrong attempts
- ⏱️ Time taken (minutes & seconds)

---

## 🧠 How It Works

- `Menu` class handles all user input and displays the game menu
- `MathQuiz` class generates random problems and runs the quiz loop
- Problems use random operands between **3 and 12**
- Wrong answers let you **retry** the same problem
- Timer starts on Enter and stops after the last problem

---

## 💡 Concepts Used

- Object Oriented Programming (Classes)
- `random` module
- `time` module
- `eval()` for expression solving
- Input Validation
- Loops & Conditionals

---

*by [sujalshrestha-dev](https://github.com/sujalshrestha-dev)*