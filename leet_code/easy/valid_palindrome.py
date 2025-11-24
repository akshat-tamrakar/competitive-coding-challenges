"""
LeetCode Problem #125: Valid Palindrome
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome/

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama" || Output: true || Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car" || Output: false || Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " " || Output: true || Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""

import string


def compare_half(clean_str: str) -> bool:
    """
    Time Complexity: O(n) - string slicing and comparison
    Space Complexity: O(n) - creates reversed substring
    """
    middle_index = len(clean_str) // 2
    return (
        clean_str[:middle_index] == clean_str[-middle_index:][::-1]
        if middle_index > 0
        else True
    )


def is_palindrome_1(s: str) -> bool:
    """
    Time Complexity: O(n) - iterate through string once to clean, once to compare
    Space Complexity: O(n) - store cleaned string
    """
    clean_str = "".join(char.lower() for char in s if char.isalnum())
    return compare_half(clean_str)


def is_palindrome_2(s: str) -> bool:
    """
    Time Complexity: O(n) - single pass through string
    Space Complexity: O(1) - only using pointer variables
    """
    left_pointer, right_pointer = 0, len(s) - 1

    while left_pointer < right_pointer:
        while left_pointer < right_pointer and not s[left_pointer].isalnum():
            left_pointer += 1
        while left_pointer < right_pointer and not s[right_pointer].isalnum():
            right_pointer -= 1
        if s[left_pointer].lower() != s[right_pointer].lower():
            return False
        left_pointer += 1
        right_pointer -= 1
    return True


def is_palindrome_3(s: str) -> bool:
    """
    Time Complexity: O(n) - translate and compare operations
    Space Complexity: O(n) - store cleaned string and translation table
    """
    chars_to_remove = string.punctuation + string.whitespace
    trans_table = str.maketrans("", "", chars_to_remove)
    clean_str = s.translate(trans_table).lower()
    return compare_half(clean_str)


def is_palindrome_4(s: str) -> bool:
    """
    Approach 4: Manual character filtering (alphanumeric only)
    Time Complexity: O(n) - iterate through string once
    Space Complexity: O(n) - store filtered string
    """
    allowed_chars = string.ascii_letters + string.digits
    clean_str = ""
    for char in s:
        if char in allowed_chars:
            clean_str += char.lower()
    return compare_half(clean_str)


def is_palindrome(s: str) -> bool:
    return is_palindrome_3(s)


if __name__ == "__main__":
    assert is_palindrome(s="A man, a plan, a canal: Panama"), "Test case 1 failed"
    print('✓ Test case 1 passed: "A man, a plan, a canal: Panama" -> True')

    assert not is_palindrome(s="race a car"), "Test case 2 failed"
    print('✓ Test case 2 passed: "race a car" -> False')

    assert is_palindrome(s=" "), "Test case 3 failed"
    print('✓ Test case 3 passed: " " -> True')

    assert is_palindrome(s="aa"), "Test case 4 failed"
    print('✓ Test case 4 passed: "aa" -> True')

    assert not is_palindrome(s="0P"), "Test case 5 failed"
    print('✓ Test case 5 passed: "0P" -> False')

    assert is_palindrome(s="1b1"), "Test case 6 failed"
    print('✓ Test case 6 passed: "1b1" -> True')
