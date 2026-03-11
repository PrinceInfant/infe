# infe

[![PyPI version](https://img.shields.io/pypi/v/infe?style=for-the-badge&color=green&cacheSeconds=0)](https://pypi.org/project/infe)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Tests](https://github.com/PrinceInfant/infe/actions/workflows/python-tests.yml/badge.svg)](https://github.com/PrinceInfant/infe/actions/workflows/python-tests.yml)

A professional, comprehensive Python math and string utility library for interviews, competitive programming, and educational purposes.

## Features

### 🔢 Basic Operations
- `is_even`, `is_odd`, `is_positive`, `is_negative`
- `swap`, `largest_of_three`, `sum_first_n`
- `factorial`, `power`, `multiplication_table`
- `sum_even_range`, `sum_odd_range`

### 🔢 Digit-Based Programs
- `count_digits`, `reverse_number`, `sum_digits`, `product_digits`
- `is_palindrome_number`, `is_disarium`, `is_neon`, `is_spy`
- `is_duck`, `is_harshad`, `max_digit`, `min_digit`
- `count_eo_digits` (Even/Odd count), `sum_even_digits`, `sum_odd_digits`

### 🔢 Primes & Factors
- `is_prime`, `primes_in_range`, `sum_primes`, `prime_factors`
- `gcd`, `lcm`, `are_coprime`, `is_composite`

### 🔢 Special Numbers
- `is_armstrong`, `is_perfect`, `is_abundant`, `fibonacci_series`
- `is_strong` (formerly Krishnamurthy), `is_happy`, `is_magic`
- `is_perfect_square`, `is_perfect_cube`, `is_triangular`

### 🔤 String Utilities
- `count_vc` (Vowels/Consonants), `no_spaces`, `char_freq`
- `dup_chars`, `is_anagram`, `first_non_rep`, `first_rep`

### 📋 List/Array Utilities
- `max_list`, `second_max`, `unique` (Remove duplicates)
- `rotate_left`, `rotate_right`

---

## Installation

```bash
pip install infe
```

## Usage

```python
import infe

# Check for a Strong (Krishnamurthy) number
print(infe.is_strong(145))  # True

# String operations
v, c = infe.count_vc("Hello World")
print(f"Vowels: {v}, Consonants: {c}")

# List operations
my_list = [10, 20, 30, 20, 10]
print(infe.unique(my_list))  # [10, 20, 30]
```

## Running Tests

```bash
pip install pytest
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
