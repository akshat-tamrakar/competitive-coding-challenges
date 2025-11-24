"""
LeetCode Problem #1071: Greatest Common Divisor of Strings
Difficulty: Easy
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/

Problem Statement:
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC" || Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB" || Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE" || Output: ""

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.
"""

from math import gcd


def is_divisor(divisor, longer_string, shorter_string) -> bool:
    """
    Check if divisor divides both target strings.

    Time Complexity: O(n + m) where n = len(longer_string), m = len(shorter_string)
        - String multiplication and comparison for both strings
    Space Complexity: O(n + m) for creating repeated divisor strings
    """
    divisor_length = len(divisor)

    # Check if divisor divides both strings
    for target_string in (longer_string, shorter_string):
        target_length = len(target_string)
        if target_length % divisor_length != 0:
            return False
        repetitions = target_length // divisor_length
        if divisor * repetitions != target_string:
            return False

    return True


def gcd_of_strings_3(str1: str, str2: str) -> str:
    """
    Time Complexity: O(min(n, m) * (n + m)) where n = len(str1), m = len(str2)
        - Iterates through all possible divisor lengths: O(min(n, m))
        - Each iteration calls is_divisor which is O(n + m)
    Space Complexity: O(n + m) for string operations in is_divisor
    """
    str1_length, str2_length = len(str1), len(str2)
    str1_is_longer = str1_length >= str2_length
    longer_string, shorter_string = (str1, str2) if str1_is_longer else (str2, str1)

    for divisor_length in range(min(str1_length, str2_length), 0, -1):
        candidate_divisor = shorter_string[:divisor_length]
        if is_divisor(candidate_divisor, longer_string, shorter_string):
            return candidate_divisor
    return ""


def gcd_of_strings_2(str1: str, str2: str) -> str:
    """
    Time Complexity: O(min(n, m) * (n + m)) where n = len(str1), m = len(str2)
        - While loop iterates through all possible divisor lengths: O(min(n, m))
        - Each iteration calls is_divisor which is O(n + m)
    Space Complexity: O(n + m) for string operations in is_divisor
    """
    str1_is_longer = len(str1) >= len(str2)
    longer_string, shorter_string = (str1, str2) if str1_is_longer else (str2, str1)
    substring_length = len(shorter_string)
    while substring_length:
        candidate_divisor = shorter_string[:substring_length]
        if is_divisor(candidate_divisor, longer_string, shorter_string):
            return candidate_divisor
        substring_length -= 1

    return ""


def gcd_of_strings_1(str1: str, str2: str) -> str:
    """
    Time Complexity: O(n + m) where n = len(str1), m = len(str2)
    Space Complexity: O(n + m) for string concatenation
    """
    if str1 + str2 != str2 + str1:
        return ""

    gcd_length = gcd(len(str1), len(str2))
    return str1[:gcd_length]


def gcd_of_strings(str1: str, str2: str) -> str:
    return gcd_of_strings_2(str1, str2)


if __name__ == "__main__":
    result1 = gcd_of_strings(str1="ABCABC", str2="ABC")
    assert result1 == "ABC", f"Test case 1 failed: expected 'ABC', got '{result1}'"
    print("✓ Test case 1 passed: str1='ABCABC', str2='ABC' -> 'ABC'")

    result2 = gcd_of_strings(str1="ABABAB", str2="ABAB")
    assert result2 == "AB", f"Test case 2 failed: expected 'AB', got '{result2}'"
    print("✓ Test case 2 passed: str1='ABABAB', str2='ABAB' -> 'AB'")

    result3 = gcd_of_strings(str1="LEET", str2="CODE")
    assert result3 == "", f"Test case 3 failed: expected '', got '{result3}'"
    print("✓ Test case 3 passed: str1='LEET', str2='CODE' -> ''")

    result4 = gcd_of_strings(str1="ABCDEF", str2="ABC")
    assert result4 == "", f"Test case 4 failed: expected '', got '{result4}'"
    print("✓ Test case 4 passed: str1='ABCDEF', str2='ABC' -> ''")

    result5 = gcd_of_strings(
        str1="TAUXXTAUXXTAUXXTAUXXTAUXX",
        str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX",
    )
    assert result5 == "TAUXX", f"Test case 5 failed: expected 'TAUXX', got '{result5}'"
    print(
        "✓ Test case 5 passed: str1='TAUXXTAUXXTAUXXTAUXXTAUXX', str2='TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX' -> 'TAUXX'"
    )

    print("\n✅ All test cases passed!")
