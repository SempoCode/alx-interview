# 0x00. Pascal's Triangle

## Description

This project focuses on implementing Pascal's Triangle using Python. Pascal's Triangle is a triangular array of the binomial coefficients, with the elements of each row being the coefficients of the binomial expansion.

### Tasks

#### 0. Pascal's Triangle
Write a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of n:
- Returns an empty list if `n <= 0`.
- Assumes `n` will always be an integer.

### Example
If `n = 5`, the function should return the following list of lists:

```python
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

### Files
- `0-pascal_triangle.py`: Contains the function that generates Pascal's Triangle.
- `0-main.py`: Test file provided to check the implementation.

### Usage
To run the test file:

```bash
$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

### Learning Objectives
- Lists and list comprehensions in Python.
- Iterating over lists using loops.
- Using nested loops to build complex data structures.
- Conditional statements to handle logic.
- Efficiency considerations (time and space complexity).

---

## Author
- [Your Name]

```
