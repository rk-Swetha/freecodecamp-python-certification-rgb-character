"""
Build a Number Pattern Generator
Part of the freeCodeCamp Python Certification Course

Author: Swetha R.K.
"""

def number_pattern(n):
    """
    Returns a space-separated number pattern from 1 to n.
    """
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    result = ""
    for i in range(1, n + 1):
        if i == 1:
            result = str(i)
        else:
            result += " " + str(i)
    return result
