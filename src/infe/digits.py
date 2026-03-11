from __future__ import annotations

def count_digits(n: int) -> int:
    return len(str(abs(n)))

def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

def sum_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

def product_digits(n: int) -> int:
    prod = 1
    for d in str(abs(n)):
        prod *= int(d)
    return prod

def is_palindrome_number(n: int) -> bool:
    s = str(abs(n))
    return s == s[::-1]

def is_disarium(n: int) -> bool:
    s = str(abs(n))
    total = sum(int(digit) ** (i + 1) for i, digit in enumerate(s))
    return total == n

def is_neon(n: int) -> bool:
    square = n * n
    return sum_digits(square) == n

def is_spy(n: int) -> bool:
    return sum_digits(n) == product_digits(n)

def is_duck(n: int) -> bool:
    s = str(n)
    return '0' in s and s[0] != '0'

def is_harshad(n: int) -> bool:
    if n <= 0: return False
    return n % sum_digits(n) == 0

def max_digit(n: int) -> int:
    return int(max(str(abs(n))))

def min_digit(n: int) -> int:
    return int(min(str(abs(n))))

def count_eo_digits(n: int) -> tuple[int, int]:
    """Return count of (even, odd) digits."""
    s = str(abs(n))
    even = sum(1 for d in s if int(d) % 2 == 0)
    odd = len(s) - even
    return even, odd

def sum_even_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)) if int(d) % 2 == 0)

def sum_odd_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)) if int(d) % 2 != 0)

def is_ascending_digits(n: int) -> bool:
    s = str(abs(n))
    return all(s[i] <= s[i+1] for i in range(len(s)-1))

def is_descending_digits(n: int) -> bool:
    s = str(abs(n))
    return all(s[i] >= s[i+1] for i in range(len(s)-1))
