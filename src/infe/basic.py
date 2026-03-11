from __future__ import annotations
import math

def is_even(n: int) -> bool:
    return n % 2 == 0

def is_odd(n: int) -> bool:
    return n % 2 != 0

def is_positive(n: int) -> bool:
    return n > 0

def is_negative(n: int) -> bool:
    return n < 0

def swap(a, b):
    return b, a

def largest_of_three(a: float, b: float, c: float) -> float:
    return max(a, b, c)

def sum_first_n(n: int) -> int:
    return (n * (n + 1)) // 2

def factorial(n: int) -> int:
    if n < 0: return 0
    return math.factorial(n)

def power(x: float, n: float) -> float:
    return x ** n

def multiplication_table(n: int, limit: int = 10) -> list:
    return [n * i for i in range(1, limit + 1)]

def sum_even_range(start: int, end: int) -> int:
    """Return sum of even numbers in range [start, end]."""
    return sum(n for n in range(start, end + 1) if n % 2 == 0)

def sum_odd_range(start: int, end: int) -> int:
    """Return sum of odd numbers in range [start, end]."""
    return sum(n for n in range(start, end + 1) if n % 2 != 0)
