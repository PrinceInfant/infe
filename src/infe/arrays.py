from __future__ import annotations

def max_list(arr: list):
    """Return the largest element in a list."""
    if not arr: return None
    return max(arr)

def second_max(arr: list):
    """Return the second largest number in a list."""
    if len(arr) < 2: return None
    first = second = float('-inf')
    for n in arr:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    return second if second != float('-inf') else None

def unique(arr: list) -> list:
    """Remove duplicates from a list while maintaining order."""
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

def rotate_left(arr: list, n: int) -> list:
    """Rotate list to the left by N positions."""
    if not arr: return arr
    n = n % len(arr)
    return arr[n:] + arr[:n]

def rotate_right(arr: list, n: int) -> list:
    """Rotate list to the right by N positions."""
    if not arr: return arr
    n = n % len(arr)
    return arr[-n:] + arr[:-n]
