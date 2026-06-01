# 📖 Madlibs Generator

A fun CLI madlibs game! It reads a story from a text file, finds all the
blank placeholders, asks you to fill them in, and prints the final silly story.

---

## 📂 Files

| File | Description |
|------|-------------|
| `madlibs_generator.py` | Main Python script |
| `story.txt` | The story template with placeholders |

---

## ▶️ How to Run

1. Open the `5. madlibs generator` folder in VS Code
2. Click the **Run ▶ button** on `madlibs_generator.py`
3. Enter a word for each placeholder when prompted
4. Read your hilarious story!

---

## 🧠 How It Works

- Reads `story.txt` which contains placeholders like `<NAME>`, `<ANIMAL>`, etc.
- Scans the story character by character to extract all unique placeholders
- Asks the user to input a word for each placeholder
- Replaces all placeholders with the user's answers
- Prints the final story

---

## 💡 Concepts Used

- File Handling (`open`, `read`)
- Sets (to store unique placeholders)
- Loops & String Manipulation
- `enumerate()` for character scanning
- Dictionary for storing answers

---

*by [sujalshrestha-dev](https://github.com/sujalshrestha-dev)*