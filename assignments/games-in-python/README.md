# 📘 Assignment: Hangman

## 🎯 Objective

Build a playable Hangman game in Python to practice string manipulation, control flow, and user input handling. The program should run in the terminal and be easy to test and extend.

## 📝 Tasks

### 🛠️ Implement Hangman Core

#### Description
Create a terminal-based Hangman game. The program should let a player repeatedly guess letters to reveal a hidden word until they either guess the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (in-code list or external file).
- Display the hidden word progress using underscores for unknown letters (e.g., `_ a _ _ _`).
- Accept single-letter guesses (case-insensitive) and update the progress accordingly.
- Track and display remaining incorrect guesses.
- Prevent and handle repeated or invalid inputs (e.g., digits or multiple characters).
- End the game with a clear win or lose message and reveal the full word when the game ends.

#### Example
```
Word: _ _ _ _ _
Guess a letter: a
Correct! Current word: _ a _ _ _
Incorrect guesses remaining: 5
...
```

### 🛠️ Optional Enhancements

#### Description
Add one or more optional features to make the game more robust or user-friendly.

#### Requirements (pick at least one)

- Read the word list from an external `words.txt` file and handle missing file errors gracefully.
- Add difficulty levels that change the number of allowed incorrect guesses.
- Show an ASCII-art hangman that progresses with incorrect guesses.
- Add a replay feature so the player can play multiple rounds without restarting the program.
- Implement basic unit tests for core functions (e.g., word selection, progress update, input validation).
- Save simple scoring or win/lose statistics to a file for later review.



