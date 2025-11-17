"""
LeetCode Problem #13: Roman to Integer
Difficulty: Easy
Link: https://leetcode.com/problems/roman-to-integer/

Problem Statement:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III" || Output: 3 || Explanation: III = 3.

Example 2:
Input: s = "LVIII" || Output: 58 || Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV" || Output: 1994 || Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


def roman_to_int_by_subtraction(s: str) -> int:
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    prev_value = 0

    for char in reversed(s):
        curr_value = roman_values[char]

        # If current value is greater than or equal to previous value, add it else subtract it (handles cases like IV, IX, XL, etc.)
        if curr_value >= prev_value:
            total += curr_value
        else:
            total -= curr_value

        prev_value = curr_value

    return total


def roman_to_int_by_replacement(s: str) -> int:
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = (
        s.replace("IV", "IIII")
        .replace("IX", "VIIII")
        .replace("XL", "XXXX")
        .replace("XC", "LXXXX")
        .replace("CD", "CCCC")
        .replace("CM", "DCCCC")
    )

    total = 0
    for x in s:
        total += roman_values[x]

    return total


def roman_to_int_by_lookup(s: str) -> int:
    # Dictionary for special cases (subtractive combinations)
    special_cases = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    # Dictionary for single Roman numerals
    single_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    i = 0

    while i < len(s):
        # Check if current and next character form a special case
        if i + 1 < len(s) and s[i : i + 2] in special_cases:
            total += special_cases[s[i : i + 2]]
            i += 2
        else:
            # If not a special case, add the single value
            total += single_values[s[i]]
            i += 1

    return total


# Test cases
test_cases = [
    "III",  # 3
    "IV",  # 4
    "LVIII",  # 58
    "MCMXCIV",  # 1994
]

for test_arg in test_cases:
    print()
    assert (
        roman_to_int_by_subtraction(test_arg)
        == roman_to_int_by_replacement(test_arg)
        == roman_to_int_by_lookup(test_arg)
    )
