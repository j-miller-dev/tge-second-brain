# Existential-Universal vs Universal-Existential Statements

The order of quantifiers matters.

## Existential-Universal

Form:

- `∃x ∀y P(x, y)`

Meaning:

- There exists an `x` that works for every `y`.

Example:

- “There is a student who solved every problem.”
- Symbolically: `∃s ∀p (Solved(s, p))`

This means one student solved all problems.

## Universal-Existential

Form:

- `∀y ∃x P(x, y)`

Meaning:

- For each `y`, there exists an `x` that works.

Example:

- “For every problem, there is a student who solved it.”
- Symbolically: `∀p ∃s (Solved(s, p))`

This means each problem has some student who solved it, but not necessarily the same student.

## Why they are different

- `∃x ∀y P(x, y)` requires one single `x` that works for all `y`.
- `∀y ∃x P(x, y)` allows a different `x` for each `y`.

Example with numbers:

- `∃m ∀n (m ≤ n)` is true: choose `m = 1`.
- `∀n ∃m (m < n)` is true: for each `n`, choose `m = n - 1`.
- `∃m ∀n (m < n)` is false: there is no single number smaller than every number.

The key difference is the order of the quantifiers.