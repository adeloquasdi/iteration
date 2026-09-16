def count(text: str, letters: str) -> int:
    count = 0
    for letter in text:
        if letter in letters:
            count += 1
    return count

def collatz(n: int) -> list[int]:
    nums = []
    while n != 1:
        nums = nums + [n]
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    return nums + [n]

# Students are records of (Student Name, Birth Year, Height in Inches)
students = [
    ('Alice', 2001, 59),
    ('Bob', 2004, 67),
    ('Charlie', 2005, 71),
    ('Daisy', 2005, 67),
    ('Eve', 2004, 63)
]

# Grades are records of (Course, Student Name, Letter Grade)
# Assignment statement: grades in global, list[tuples[str, str, str]]
grades = [
    ('DS1043', 'Alice', 'A'),
    ('DS1043', 'Bob', 'A'),
    ('DS1043', 'Charlie', 'B'),
    ('DS1043', 'Daisy', 'B'),
    ('DS1043', 'Eve', 'C'),
    ('CS2023', 'Alice', 'A'),
    ('CS2023', 'Bob', 'B'),
    ('CS2023', 'Charlie', 'C'),
    ('CS2023', 'Daisy', 'A'),
    ('CS2023', 'Eve', 'B')
]

# Assignment statement: gpa_scale in global, dict[str, float]
gpa_scale = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

# Function definition statement (10 lines): calculate_gpas in global
# Callable, returns dict[str, float]
# grades as local of type tuple[str, str, str]
def calculate_gpas(grades: tuple[str, str, str]) -> dict[str, float]:
    gpa = {} # assignment gpa to locals, dictionary
    for course, name, grade in grades: # for statement
        if name not in gpa: # if statment
            gpa[name] = [gpa_scale[grade]] # [4.0],
        else: #else
            gpa[name] = gpa[name] + [gpa_scale[grade]]
    for student in gpa:
        gpa[student] = sum(gpa[student]) / len(gpa[student])
    return gpa

# Function call
calculate_gpas(grades)

# locals
# grades -> see above
# gpa -> dict {'Alice': [4.0, 4.0], 'Bob': [4.0], 'Charlie': [3.0]}
# course -> str 'DS1043' 'DS1043' 'DS1043'
# name -> str   'Alice'  'Bob'    'Charlie'
# grade -> str  'A'      'A'      'B'