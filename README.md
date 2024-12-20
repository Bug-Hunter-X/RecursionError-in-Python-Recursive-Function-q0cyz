# RecursionError in Python

This repository demonstrates a common error that can occur in Python when using recursive functions: the `RecursionError`.  A `RecursionError` happens when a recursive function calls itself too many times, exceeding the maximum allowed recursion depth set by the Python interpreter.

The `bug.py` file contains a simple recursive function that calculates the sum of numbers from 1 to x.  While this function works correctly for small values of x, it will raise a `RecursionError` if x is large enough.

The `bugSolution.py` file provides a solution to this problem by using iteration instead of recursion.  This avoids the risk of exceeding the recursion depth limit.

## How to reproduce the bug

1. Clone this repository.
2. Run `bug.py`. It will work correctly for smaller values of 'x' but will throw a `RecursionError` for larger values, for example, 'x = 1000'