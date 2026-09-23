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

# Reading Code Example

```python
def tokenize(text, delimiters=' .,!?;:/"'):
    token = ''
    tokens = []
    for character in text:
        if character in delimiters:
            tokens = tokens + [token]
            token = ''
        else:
            token = token + character
    if len(token) > 0:
        tokens = tokens + [token]
    return tokens

tokenize('Be yourself, everyone else is taken.')
```

1.  `def tokenize(text, delimiters=' .,!?;:/"'):`
    - Function Definition Statement (header line 1, body lines 2-12)
    - def (keyword), tokenize (identifier)
    - Parameters: text (positional parameter), delimiters (keyword parameter)
2.  `    token = ''`
    - Assignment Statement
    - token (identifier) = (keyword) '' (literal value)
3.  `    tokens = []`
    - Assignment Statement
    - tokens (identifier) = (keyword) [] (literal value)
4.  `    for character in text:`
    - For Loop Statement (header line 4, body lines 5-9)
    - for (keyword) character (identifier) in (keyword) text (identifier)
5.  `        if character in delimiters:`
    - If Statement
    - if (keyword) character (identifier) in (operator) delimiters (identifier)
6.  `            tokens = tokens + [token]`
    - Assignment Statement
    - tokens (identifier) = (keyword) tokens (identifier) + (operator) [token]
    - `[token]` is a new list containing the value of `token`
7.  `            token = ''`
    - Assignment Statement
8.  `        else:`
    - Else Statment (header line 8, body line 9)
9.  `            token = token + character`
    - Assignment Statement
10. `    if len(token) > 0:`
    - If Statement (header line 10, body line 11)
11. `        tokens = tokens + [token]`
    - Assignment Statement
12. `    return tokens`
    - Return statement
    - return (keyword) tokens (identifier)
13. 
14. `tokenize('Be yourself!')`
    - Function call
    - tokenize (identifier, type Callable)
    - Argument list: 'Be yourself!' (literal value)


| Local Name | Type | Values                                                                           |
|------------|------|----------------------------------------------------------------------------------|
| text       | str  | 'Be yourself!'                                                                   |
| delimiters | str  | ' .,!?;:/"'                                                                      |
| token      | str  | 'B', 'Be', '', 'y', 'yo', 'you', 'your', 'yours', 'yourse', 'yoursel', 'yourself' |
| tokens     | list | [], ['Be'], ['Be', 'yourself']                                                   |
| character  | str  | 'B','e', ' ', 'y', 'o', 'u', 'r', 's', 'e', 'l', 'f', '!'                        |

# Star Operator

Not multiplication like `2 * 3`

We can "pop" the first, last, or first and last elements off of a sequence
```example
>>> student_record = ('Alice', 100001, 3.75)
>>> name, *rest = student_record
>>> name
'Alice'
>>> rest
[100001, 3.75]
>>> *rest, gpa = student_record
>>> name, *rest, gpa = student_record
```

We can "unpack" a sequence to len(sequence) values for passing to a function
```example
>>> def some_fucntion(name, id, gpa):
...     print(name, id, gpa)
...
>>> some_function(*student_record)
Alice 100001 3.75
```

If we don't care about some value, we call it _ by convention
```python
for name, *_ in student_records:
    print(name)
```

If we want to accept any number of positional arguments, we use * then an identifier as a parameter.
If we want to accept any number of keyword arguments, we use ** then an identifier as a parameter.
```example
>>> def some_function(*args, **kwargs):  # very common names in Python's standard libraries
...     for arg in args:
...         print(arg)
...     print('Keyword name = ', kwargs['name'])
...
>>> some_function(1, 2, name='Alice')
1
2
Keyword name = Alice
```

# Useful Functions, Implemented

## Map
```python
def my_map(func, seq):
    result = []
    for element in seq:
        result += [func(element)]
    return result
```

## Filter
```python
def my_filter(func, seq):
    result = []
    for element in seq:
        if func(element):
            result += [element]
    return result
```


## Reversed
```python
def my_reversed(seq):
    result = []
    for index in range(len(seq) -1, -1, -1):
        result += [seq[index]]
    return result
```

## Enumerate

```python
def my_enumerate(seq):
    index = 0
    result = []
    for element in seq:
        result += [(index, element)]
        index += 1
    return result
```

## Zip

```python
def transpose(*args):
    stop = len(min(*args, key=len))
    index = 0
    result = []
    while index < stop:
        element = ()
        for seq in args:
            element += (seq[index],)
        index += 1
        result += [element]
    return result
```