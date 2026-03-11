from __future__ import annotations

def is_armstrong(n: int) -> bool:
    """
    Check if a number is an Armstrong number.
    
    An Armstrong number of order n is a number in which each digit 
    is raised to the power n and their sum is equal to the number itself.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if n is an Armstrong number, False otherwise.
    """
    if not isinstance(n, int) or n < 0:
        return False
        
    s = str(n)
    power = len(s)
    total = sum(int(digit) ** power for digit in s)
    return total == n


def find_armstrong(limit: int) -> list:
    """
    Find all Armstrong numbers from 0 up to the given limit.
    
    Args:
        limit (int): The upper bound for searching Armstrong numbers.
        
    Returns:
        list: A list of Armstrong numbers up to the limit.
    """
    return [n for n in range(limit + 1) if is_armstrong(n)]


def generate_armstrong(start: int, end: int) -> list:
    """
    Generate Armstrong numbers within a specific range [start, end].
    
    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        
    Returns:
        list: A list of Armstrong numbers within the range.
    """
    return [n for n in range(start, end + 1) if is_armstrong(n)]
