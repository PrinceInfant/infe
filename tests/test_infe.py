from infe import (
    is_even, is_odd, factorial, is_prime, 
    is_palindrome_number, is_happy, is_armstrong, 
    is_strong, max_digit, min_digit, count_eo_digits,
    count_vc, no_spaces, is_anagram,
    max_list, second_max, unique, rotate_left
)

def test_basic_math():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_odd(3) is True
    assert factorial(5) == 120

def test_primes():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(4) is False

def test_number_properties():
    assert is_strong(145) is True
    assert is_happy(19) is True
    assert is_armstrong(153) is True
    assert max_digit(129) == 9
    assert min_digit(129) == 1
    assert count_eo_digits(1234) == (2, 2)

def test_strings():
    assert count_vc("Hello") == (2, 3)
    assert no_spaces("H e l l o") == "Hello"
    assert is_anagram("Listen", "Silent") is True

def test_lists():
    assert max_list([1, 5, 3]) == 5
    assert second_max([1, 5, 3, 4]) == 4
    assert unique([1, 2, 2, 3]) == [1, 2, 3]
    assert rotate_left([1, 2, 3], 1) == [2, 3, 1]
