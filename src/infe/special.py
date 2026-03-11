from __future__ import annotations
import math
from .digits import sum_digits

def is_perfect(n: int) -> bool:
    if n < 2: return False
    divisors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n: divisors.append(n // i)
    return sum(divisors) == n

def is_abundant(n: int) -> bool:
    if n < 2: return False
    divisors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n: divisors.append(n // i)
    return sum(divisors) > n

def fibonacci_series(n_terms: int) -> list:
    series = [0, 1]
    while len(series) < n_terms:
        series.append(series[-1] + series[-2])
    return series[:n_terms]

def is_perfect_square(n: int) -> bool:
    if n < 0: return False
    root = int(math.isqrt(n))
    return root * root == n

def is_perfect_cube(n: int) -> bool:
    cube_root = round(abs(n) ** (1/3))
    return cube_root ** 3 == abs(n)

def is_triangular(n: int) -> bool:
    if n < 0: return False
    return is_perfect_square(8 * n + 1)

def is_automorphic(n: int) -> bool:
    square = n * n
    return str(square).endswith(str(n))

def is_kaprekar(n: int) -> bool:
    if n == 1: return True
    sq = n * n
    s = str(sq)
    for i in range(1, len(s)):
        l, r = int(s[:i]), int(s[i:])
        if r > 0 and l + r == n: return True
    return False

def is_strong(n: int) -> bool:
    """Check if sum of factorials of digits equals the number."""
    total = sum(math.factorial(int(d)) for d in str(abs(n)))
    return total == n

def is_happy(n: int) -> bool:
    seen = set()
    temp = n
    while temp != 1 and temp not in seen:
        seen.add(temp)
        temp = sum(int(d)**2 for d in str(temp))
    return temp == 1

def is_magic(n: int) -> bool:
    temp = n
    while temp > 9:
        temp = sum_digits(temp)
    return temp == 1

def is_peterson(n: int) -> bool:
    """A Peterson number is the same as a Strong number."""
    return is_strong(n)
