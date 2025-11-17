"""
LeetCode Problem #20: Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()" || Output: true

Example 2:
Input: s = "()[]{}" || Output: true

Example 3:
Input: s = "(]" || Output: false

Example 4:
Input: s = "([])" || Output: true

Example 5:
Input: s = "([)]" || Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""


def valid_parentheses_1(s: str):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False

    return not stack


def valid_parentheses_2(s: str):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""


if __name__ == "__main__":
    assert valid_parentheses_1("()"), "Test case 1 failed"
    print("✓ Test case 1 passed: '()' -> True")

    assert valid_parentheses_1("()[]{}"), "Test case 2 failed"
    print("✓ Test case 2 passed: '()[]{}' -> True")

    assert not valid_parentheses_1("(]"), "Test case 3 failed"
    print("✓ Test case 3 passed: '(]' -> False")

    assert valid_parentheses_1("([])"), "Test case 4 failed"
    print("✓ Test case 4 passed: '([])' -> True")

    assert not valid_parentheses_1("([)]"), "Test case 5 failed"
    print("✓ Test case 5 passed: '([)]' -> False")

    assert valid_parentheses_1("[()]"), "Test case 6 failed"
    print("✓ Test case 6 passed: '[()]' -> True")

    assert valid_parentheses_2("()"), "Test case 7 failed"
    print("✓ Test case 7 passed: valid_parentheses_2 method -> True")

    print("\n✅ All test cases passed!")
