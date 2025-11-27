"""
LeetCode Problem #680: Valid Palindrome II
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome-ii/

Problem Statement:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba" || Output: true

Example 2:
Input: s = "abca" || Output: true || Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc" || Output: false

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""


def is_palindrome_helper(s: str, left: int, right: int) -> bool:
    """
    Check if substring is a palindrome using two pointers.

    Time Complexity: O(n) where n is the length of the substring
    Space Complexity: O(1) - only using pointer variables
    """
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def valid_palindrome_1(s: str) -> bool:
    """
    Two-pointer with substring slicing approach.

    Time Complexity: O(n) where n = len(s)
    Space Complexity: O(n) - creates substring slices
    """
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] != s[right]:
            skip_left = s[left + 1 : right + 1]
            skip_right = s[left:right]
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]

        left += 1
        right -= 1

    return True


def valid_palindrome_2(s: str) -> bool:
    """
    Two-pointer approach with one deletion allowed (optimal).

    Time Complexity: O(n) where n = len(s)
        - Single pass with two pointers
        - At most one additional palindrome check of remaining substring
    Space Complexity: O(1) - only using pointer variables
    """
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping left character or right character
            skip_left = is_palindrome_helper(s, left + 1, right)
            skip_right = is_palindrome_helper(s, left, right - 1)
            return skip_left or skip_right
        left += 1
        right -= 1

    return True


def valid_palindrome_3(s: str) -> bool:
    """
    Recursive approach with deletion counter.

    Time Complexity: O(n) where n = len(s)
        - At most two recursive calls when mismatch found
    Space Complexity: O(n) - recursion call stack depth
    """

    def check_palindrome(left: int, right: int, deletions_remaining: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                if deletions_remaining == 0:
                    return False
                # Try deleting either left or right character
                return check_palindrome(
                    left + 1, right, deletions_remaining - 1
                ) or check_palindrome(left, right - 1, deletions_remaining - 1)
            left += 1
            right -= 1
        return True

    return check_palindrome(0, len(s) - 1, 1)


def valid_palindrome_4(s: str) -> bool:
    """
    Iterative approach with explicit mismatch handling.

    Time Complexity: O(n) where n = len(s)
    Space Complexity: O(1) - only using pointer variables
    """
    left, right = 0, len(s) - 1
    mismatch_found = False

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if mismatch_found:
                return False
            # Check if removing left or right character makes it palindrome
            if is_palindrome_helper(s, left + 1, right):
                return True
            if is_palindrome_helper(s, left, right - 1):
                return True
            return False

    return True


def valid_palindrome(s: str) -> bool:
    """
    Main function to check if string can be palindrome with at most one deletion.
    Currently uses valid_palindrome_2 (optimal approach).
    """
    return valid_palindrome_2(s)


if __name__ == "__main__":
    assert valid_palindrome(s="aba"), "Test case 1 failed"
    print('✓ Test case 1 passed: s="aba" -> True')

    assert valid_palindrome(s="abca"), "Test case 2 failed"
    print('✓ Test case 2 passed: s="abca" -> True')

    assert not valid_palindrome(s="abc"), "Test case 3 failed"
    print('✓ Test case 3 passed: s="abc" -> False')

    assert valid_palindrome(s="racecar"), "Test case 4 failed"
    print('✓ Test case 4 passed: s="racecar" -> True')

    assert valid_palindrome(s="deeee"), "Test case 5 failed"
    print('✓ Test case 5 passed: s="deeee" -> True')

    assert valid_palindrome(
        s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    ), "Test case 6 failed"
    print(
        '✓ Test case 6 passed: s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga" -> True'
    )

    assert not valid_palindrome(s="abcdef"), "Test case 7 failed"
    print('✓ Test case 7 passed: s="abcdef" -> False')

    assert valid_palindrome(s="a"), "Test case 8 failed"
    print('✓ Test case 8 passed: s="a" -> True')

    assert valid_palindrome(s="ab"), "Test case 9 failed"
    print('✓ Test case 9 passed: s="ab" -> True')

    print("\n✅ All test cases passed!")
