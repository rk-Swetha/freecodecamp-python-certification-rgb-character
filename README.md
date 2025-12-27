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

**## Output **
Arin
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●●○○○○○○○○
