"""
LeetCode Problem: Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
- Input: s = "()" → Output: true
- Input: s = "()[]{}" → Output: true  
- Input: s = "(]" → Output: false
- Input: s = "([])" → Output: true
- Input: s = "([)]" → Output: false
"""
from printopia import print_return_info


@print_return_info
def valid_parentheses_1(s: str):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    
    return not stack


@print_return_info
def valid_parentheses_2(s: str):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return s == ''


if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([])", "([)]", "[()]"]
    
    for test in test_cases:
        valid_parentheses_1(test)
        valid_parentheses_2(test)
