"""
9 Palindrome Number
===================
Given an integer x, return true if x is a palindrome , and false otherwise.
"""

from printopia import print_return, print_return_info


def check_palindrome_by_conditions(number: int) -> bool:
    """Helper function to validate palindrome input conditions."""
    # Handle negative numbers and numbers ending with 0
    if number < 0 or (number != 0 and number % 10 == 0):
        return False

    # Single digit numbers are always palindromes
    if number < 10:
        return True

    return None  # Continue with palindrome check


@print_return_info
def is_palindrome_by_reverse_half(number: int) -> bool:
    if (validation_result := check_palindrome_by_conditions(number)) is not None:
        return validation_result

    reversed_half_number = 0

    # Reverse half of the number
    while number > reversed_half_number:
        reversed_half_number = reversed_half_number * 10 + number % 10
        number //= 10

    # For even length numbers: x == half_reversed
    # For odd length numbers: x == half_reversed//10
    return number == reversed_half_number or number == reversed_half_number // 10


@print_return_info
def is_palindrome_by_string_comparison(number: int) -> bool:
    if (validation_result := check_palindrome_by_conditions(number)) is not None:
        return validation_result

    # Convert to string for easier comparison
    number_as_string = str(number)

    # Compare characters from start and end moving inward
    left_index, right_index = 0, len(number_as_string) - 1
    while left_index < right_index:
        if number_as_string[left_index] != number_as_string[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True


@print_return_info
def is_palindrome_by_string_reverse(number: int) -> bool:
    number_str = str(number)
    return number_str == number_str[::-1]


def test_palindrome_functions():
    test_cases = [
        (121, True),  # Regular palindrome
        (-121, False),  # Negative numbers are not palindromes
        (10, False),  # Not a palindrome
        (12321, True),  # Odd length palindrome
        (1221, True),  # Even length palindrome
        (0, True),  # Single digit is always a palindrome
    ]

    for number, _ in test_cases:
        assert (
            is_palindrome_by_string_reverse(number)
            == is_palindrome_by_string_comparison(number)
            == is_palindrome_by_reverse_half(number)
        ), f"Failed for input: {number}"


if __name__ == "__main__":
    test_palindrome_functions()
