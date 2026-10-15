# Python Practice Solutions: Conditionals

Three beginner Python programs that use `if`/`elif`/`else` decisions. Each one has hard-coded inputs at the top, so you can change the values and run it again.

## Programs

### 1. Leap year check
Decides whether a year is a leap year.

- **Input:** `year = 2024`
- **Rule:** A year is a leap year if it is divisible by 4 and not by 100, or if it is divisible by 400.
- **Output:** `2024 is a leap year.`
- **Examples:** 1900 is not a leap year (divisible by 100, not by 400). 2000 is a leap year (divisible by 400).

### 2. Positive, negative or zero
Classifies a number by its sign.

- **Input:** `num = -7`
- **How it works:** An `if`/`elif`/`else` chain checks `num > 0`, then `num < 0`, and otherwise treats the number as zero.
- **Output:** `-7 is a negative number.`

### 3. Largest of three numbers
Finds the biggest of three values using comparisons.

- **Input:** `a = 12`, `b = 45`, `c = 27`
- **How it works:** Each number is compared against the other two with `>=`. The first one that is at least as large as both others becomes `largest`.
- **Output:** `The largest of 12, 45 and 27 is: 45`

## Concepts Covered

- `if` / `elif` / `else`
- Comparison operators (`>`, `<`, `>=`, `==`, `!=`)
- Logical operators (`and`, `or`)
- Modulo (`%`) for divisibility checks
- f-strings for output

## Running

Requires Python 3.6 or newer (f-strings). Save a program to a file and run:

```
python program.py
```

To try other values, change the input variables at the top of the program (`year`, `num`, or `a`, `b`, `c`).
