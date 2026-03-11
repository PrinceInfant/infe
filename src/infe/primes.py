from __future__ import annotations
import math

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def primes_in_range(start: int, end: int) -> list:
    return [n for n in range(start, end + 1) if is_prime(n)]

def sum_primes(limit: int) -> int:
    return sum(primes_in_range(2, limit))

def prime_factors(n: int) -> list:
    factors = []
    d = 2
    temp = abs(n)
    while temp > 1:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
        if d * d > temp:
            if temp > 1: factors.append(temp)
            break
    return factors

def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0: return 0
    return abs(a * b) // math.gcd(a, b)

def are_coprime(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1

def is_composite(n: int) -> bool:
    if n < 4: return False
    return not is_prime(n)
