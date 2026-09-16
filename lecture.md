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
    `count('mississippi', 'i') -> 4`
2. Collatz Sequence:
    - given some positive, non-zero integer n
    - if n is even, the next term is n/2
    - if n is odd, the next term is 3n + 1
    - if n is 1, the sequence terminates
   `def collatz(n: int) -> list[int]:`
   `some_list = some_list + [n]`
   ```example
   collatz(1) -> [1]
   collatz(2) -> [2, 1]
   collatz(3) -> [3, 10, 5, 16, 8, 4, 2, 1]
   ```

For each of these problems:
1. What your inputs for computing these would be, what your output would be,
   and what types in Python are most appropriate
2. Generate some examples include edge cases
3. Sketch out (in English) how you'd solve these problems,
   i.e. what loop are you using


# Useful Functions

```example
>>> text = 'mississippi'
>>> for index, letter in enumerate(text):
...     print(index, letter)
    
0 m
1 i
2 s
3 s
4 i
5 s
6 s
7 i
8 p
9 p
10 i
```

```example
>>> text[0]
'm'
>>> text[1:]
'ississippi'
>>> for x, y in zip(text, text[1:]):
...     print(x, y)
    
m i
i s
s s
s i
i s
s s
s i
i p
p p
p i
>>> count = 0
>>> for x, y in zip(text, text[1:]):
...     if x == y:
...         count += 1
    
>>> count
3
>>> text
'mississippi'
```

```example
>>> lambda param: str(param)
<function <lambda> at 0x0000027DC1A04D50>
>>> x = lambda param: str(param)
>>> x(1)
'1'
>>> hand = ('K', 'Q', 'A')
>>> face_cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
>>> face_cards['A']
14
>>> sorted(hand)
['A', 'K', 'Q']
>>> sorted(hand, key=lambda card: face_cards[card])
['Q', 'K', 'A']
```