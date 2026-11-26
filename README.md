# python-practice

Python practice repo. It has the first few exercises I wrote while learning the language, plus a small CLI app that grew out of them.

## What's here

```
python lessons/
  lesson 1.py    # input, type casting, f-strings, age from birth year
  lesson2.py     # if/else on an exam score
  lesson3.py     # ATM: pin check, withdrawal, balance update

python_learning_hub/
  main.py        # menu-driven CLI
  modules/       # the three lessons rewritten as functions with validation
  requirements.txt
```

`python_learning_hub` is the same three exercises refactored into modules, with input validation and a loop menu:

```bash
cd python_learning_hub
python main.py
```

```
  PYTHON LEARNING HUB
1. User Profile & Age Calculator
2. Grade Checker
3. ATM Simulator
4. Exit
```

No third-party packages. Standard library only, tested on Python 3.10+.

The bare lesson files are kept as they were originally written. They are not imported by the app; `modules/` is the cleaned-up version.
