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


