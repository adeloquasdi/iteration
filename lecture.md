- Review Types
  - int, float, bool (immutable)
  - str (immutable)
  - tuple (immutable, sequence, iterable), list (mutable, sequence, iterable)
  - dict (mutable, iterable)
  - range (immutable, sequence, iterable)
- Introduce a few "abstract" types
  - Sequence - indexable []
  - Iterable - loop over
  - Callable - function
- Introduce a few new operators
  - [] access elements (either by index or key, i.e. key in a key, value pair)
  - `in` boolean operator for membership
- Look at ways to repeat instructions
  - iteration (loops)
    - `while` loop
      ```python
        while (condition):
            (body)
      ```
    - `for` loop
      ```python
        for (name) in (iterable):
            (body)
      ```
    - Note that loops do not have their own scope (namespace)!
  - recursion (tradeoff between cognitive load and machine memory)
  - functional (black box repetition)

# Some Exercises

Consider the following problems:
1. Count the number of occurrences of a letter in a string
    `def count(text: str, letter: str) -> int:`
2. Collatz Sequence:
    - given some positive, non-zero integer n
    - if n is even, the next term is n/2
    - if n is odd, the next term is 3n + 1
    - if n is 1, the sequence terminates
   `def collatz(n: int) -> list[int]:`
   `some_list = some_list + [n]`

For each of these problems:
1. What your inputs for computing these would be, what your output would be,
   and what types in Python are most appropriate
2. Generate some examples include edge cases
3. Sketch out (in English) how you'd solve these problems,
   i.e. what loop are you using