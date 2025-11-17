"""
LeetCode Problem #1446: Consecutive Characters
Difficulty: Easy
Link: https://leetcode.com/problems/consecutive-characters/

Problem Statement:
The power of the string is the maximum length of a non-empty substring that contains only one unique character.
Given a string s, return the power of s.

Example 1:
Input: s = "leetcode" || Output: 2 ||Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba" || Output: 5 || Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:
- 1 <= s.length <= 500
- s consists of only lowercase English letters.
"""


class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        
        count = 1
        max_count = 1
        previous = s[0]
        
        for char in s[1:]:
            if char == previous:
                count += 1
            else:
                previous = char
                count = 1
            
            if count > max_count:
                max_count = count
        
        return max_count


if __name__ == "__main__":
    solution = Solution()
    
    assert solution.maxPower("leetcode") == 2, "Test case 1 failed"
    print("✓ Test case 1 passed: 'leetcode' -> 2")
    
    assert solution.maxPower("abbcccddddeeeeedcba") == 5, "Test case 2 failed"
    print("✓ Test case 2 passed: 'abbcccddddeeeeedcba' -> 5")
    
    assert solution.maxPower("aabbbbcccdddddddddddddddeeeeehhijjjkkkkaaccddddd") == 15, "Test case 3 failed"
    print("✓ Test case 3 passed: Interview example -> 15")
    
    assert solution.maxPower("a") == 1, "Test case 4 failed"
    print("✓ Test case 4 passed: 'a' -> 1")
    
    assert solution.maxPower("aaaaa") == 5, "Test case 5 failed"
    print("✓ Test case 5 passed: 'aaaaa' -> 5")
    
    assert solution.maxPower("abcdef") == 1, "Test case 6 failed"
    print("✓ Test case 6 passed: 'abcdef' -> 1")
    
    print("\n✅ All test cases passed!")

