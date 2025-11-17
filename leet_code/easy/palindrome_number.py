"""
LeetCode Problem #9: Palindrome Number
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number/

Problem Statement:
Given an integer x, return true if x is a palindrome, and false otherwise.
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: x = 121 || Output: true || Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121 || Output: false || Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10 || Output: false || Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
- -2^31 <= x <= 2^31 - 1
"""


def check_palindrome_by_conditions(number: int) -> bool:
    """Helper function to validate palindrome input conditions."""
    # Handle negative numbers and numbers ending with 0
    if number < 0 or (number != 0 and number % 10 == 0):
        return False

    # Single digit numbers are always palindromes
    if number < 10:
        return True

    return None  # Continue with palindrome check


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
    assert is_palindrome_by_reverse_half(121), "Test case 1 failed"
    print("✓ Test case 1 passed: 121 -> True")
    assert not is_palindrome_by_reverse_half(-121), "Test case 2 failed"
    print("✓ Test case 2 passed: -121 -> False")

    assert not is_palindrome_by_reverse_half(10), "Test case 3 failed"
    print("✓ Test case 3 passed: 10 -> False")

    assert is_palindrome_by_reverse_half(12321), "Test case 4 failed"
    print("✓ Test case 4 passed: 12321 -> True")

    assert is_palindrome_by_reverse_half(1221), "Test case 5 failed"
    print("✓ Test case 5 passed: 1221 -> True")

    assert is_palindrome_by_reverse_half(0), "Test case 6 failed"
    print("✓ Test case 6 passed: 0 -> True")

    assert is_palindrome_by_string_comparison(121), "Test case 7 failed"
    print("✓ Test case 7 passed: string_comparison method -> True")

    assert is_palindrome_by_string_reverse(121), "Test case 8 failed"
    print("✓ Test case 8 passed: string_reverse method -> True")

    print("\n✅ All test cases passed!")
