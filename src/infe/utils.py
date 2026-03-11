def bin_to_dec(binary_str: str) -> int:
    return int(binary_str, 2)

def dec_to_bin(n: int) -> str:
    return bin(n).replace("0b", "")

def find_missing_number(arr: list, n: int) -> int:
    # Find missing number in array of 1 to N
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
