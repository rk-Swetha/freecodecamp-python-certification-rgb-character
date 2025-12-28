# freecodecamp-python-certification-rgb-character

# RGB Character – freeCodeCamp Python Certification

This repository contains my solution for the **“RGB Character”** challenge from the  
**freeCodeCamp Python Certification Course**.

---

## Problem Overview

The goal of this challenge is to create a function that:
- Validates a character name
- Validates character stats (Strength, Intelligence, Charisma)
- Ensures strict type checking
- Enforces total stat points
- Displays stats using dot-based visualization

---

## Function Rules

### Name Validation
- Must be a string
- Cannot be empty
- Maximum length: 10 characters
- Must not contain spaces

### Stat Rules
- Strength, Intelligence, Charisma must be integers
- Values must be between **1 and 4**
- Total stat points must equal **7**
- Boolean values are rejected

---

## Example Usage

```python
print(create_character("Arin", 3, 2, 2))

Output
Arin
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●●○○○○○○○○
```
---

## Build a Pin Extractor – freeCodeCamp Challenge

### Description
This challenge extracts a secret numeric PIN from poems.  
Each digit of the PIN is formed by counting the number of letters
in a specific word position for each line of the poem.

### Logic Overview
- Each poem is split into lines
- For each line:
  - The word at index `line_number` is selected
  - The length of that word becomes a digit in the PIN
  - If no such word exists, `0` is used
- One PIN is generated per poem
---
### Example

```python
print(pin_extractor([poem, poem2, poem3]))

Output
['51420', '44440', '11111']
```
---

## Build a Number Pattern Generator – freeCodeCamp Lab

### Description
This lab focuses on practicing basic Python concepts by generating
a number pattern using a `for` loop.

### Requirements
- The function accepts a single integer argument `n`
- Returns numbers from `1` to `n` separated by spaces
- Uses a `for` loop
- Handles invalid input with appropriate error messages
---
### Example

```python
print(number_pattern(5))

Output
1 2 3 4 5
```
---
### Error Handling

```python
number_pattern("5")

Output
Argument must be an integer value.
```
