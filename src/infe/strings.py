from __future__ import annotations

def count_vc(s: str) -> tuple[int, int]:
    """Return count of (vowels, consonants) in a string."""
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

def no_spaces(s: str) -> str:
    """Remove all spaces from a string."""
    return s.replace(" ", "")

def char_freq(s: str) -> dict:
    """Return frequency of each character in a string."""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def dup_chars(s: str) -> list:
    """Return a list of duplicate characters in a string."""
    freq = char_freq(s)
    return [char for char, count in freq.items() if count > 1]

def is_anagram(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams of each other."""
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

def first_non_rep(s: str):
    """Return the first non-repeating character in a string."""
    freq = char_freq(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None

def first_rep(s: str):
    """Return the first repeating character in a string."""
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None
