# The Perfect Guess

A two-player number guessing game for the command line, built with Python.

## How it works
- Each player gets their own secret random number between 0 and 100.
- Player 1 guesses first and gets a "too high" or "too low" hint after every wrong guess.
- Player 2 then tries to find their number in fewer guesses than Player 1.
- The player who needs the fewest guesses wins. If both need the same number, it's a tie.

## Requirements
No external libraries. It only uses Python's built-in `random` module.

## Usage
python perfect_guess.py

## Concepts practiced
- `while` loops
- `if / elif / else` conditions
- `random.randint()`
- f-strings and user input

## Ideas for future updates
- Input validation (handle non-number entries)
- Multiple rounds with a score tracker
- Single-player mode against the computer