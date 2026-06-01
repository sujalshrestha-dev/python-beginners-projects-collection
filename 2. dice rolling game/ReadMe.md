# 🎲 Dice Rolling Game

A collection of dice rolling programs — from a simple roller to full multiplayer games — built with Python.

---

## 📁 Files

| File | Description |
|------|-------------|
| `simple.py` | Basic dice roller |
| `simple_with_additional_features.py` | Dice roller with history and multi-dice support |
| `dice_rolling_game_main.py` | Full dice game collection with 3 game modes |

---

## 🎮 simple.py

The most basic version. Roll two dice and see the result.

**How to run:**
```bash
python simple.py
```

**Example:**
```
Roll the dice? (y/n) y
(4, 6)
Roll the dice? (y/n) n
Thanks for playing!
```

---

## ➕ simple_with_additional_features.py

A more advanced roller — choose how many dice, track your roll history, and see totals.

**How to run:**
```bash
python simple_with_additional_features.py
```

**Commands:**

| Command | Description |
|---------|-------------|
| `roll` | Roll 1–6 dice and see the total |
| `history` | View all past rolls |
| `clear` | Clear roll history |
| `quit` | Exit |

---

## 🕹️ dice_rolling_game_main.py

The full game experience — 3 different dice games in one program.

**How to run:**
```bash
python dice_rolling_game_main.py
```

**Games:**

### 1. 2-Player Battle
- Two players take turns rolling each round
- Choose how many rounds to play (1–10)
- Highest total score at the end wins

### 2. 🐷 Pig Game
- 2 players take turns rolling
- Keep rolling to stack points
- Roll a **1** and lose all your turn points
- First player to reach **100 points** wins

### 3. 🎯 21 Dice Game
- You vs the computer
- Roll and hold, trying to get as close to **21** as possible
- Go over 21 and you **bust**
- Computer auto-rolls until it reaches 17+
- Closest to 21 wins

---

## 🛠️ Concepts Used

- `random` module
- Functions
- Loops & conditionals
- Lists & dictionaries
- Exception handling

---

*Part of the [python-beginners-projects-collection](https://github.com/sujalshrestha-dev/python-beginners-projects-collection) repository.*