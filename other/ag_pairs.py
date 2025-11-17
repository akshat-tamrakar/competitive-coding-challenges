"""
Problem: AG Pairs Counter
Difficulty: Easy
Source: Practice Problem

Problem Statement:
Given a string A consisting of uppercase letters, count the number of ordered pairs (i, j) where:
- A[i] = 'A'
- A[j] = 'G'
- i < j (i comes before j)

In other words, count how many times character 'G' appears after character 'A' in the string.

Example 1:
Input: A = "ABCGAG" || Output: 3 || Explanation: Pairs are (0,3), (0,5), (4,5) where indices have A followed by G

Example 2:
Input: A = "GAB" || Output: 0 || Explanation: No 'A' before 'G'

Example 3:
Input: A = "AAG" || Output: 2 || Explanation: Pairs are (0,2), (1,2) - both A's pair with the G

Example 4:
Input: A = "AAAGGG" || Output: 9 || Explanation: Each of 3 A's pairs with each of 3 G's = 3 × 3 = 9 pairs

Algorithm:
- Iterate through the string
- Count number of 'A's seen so far
- When encountering 'G', add the count of 'A's to total pairs
- This works because each 'G' can pair with all 'A's that came before it

Time Complexity: O(n) where n is the length of string
Space Complexity: O(1)
"""


def count_ag_pairs(A: str) -> int:
    a_count = 0
    total_pairs = 0

    for char in A:
        if char == "A":
            a_count += 1
        elif char == "G":
            total_pairs += a_count

    return total_pairs


if __name__ == "__main__":
    assert count_ag_pairs("ABCGAG") == 3, "Test case 1 failed"
    print("✓ Test case 1 passed: 'ABCGAG' -> 3")

    assert count_ag_pairs("GAB") == 0, "Test case 2 failed"
    print("✓ Test case 2 passed: 'GAB' -> 0")

    assert count_ag_pairs("AAG") == 2, "Test case 3 failed"
    print("✓ Test case 3 passed: 'AAG' -> 2")

    assert count_ag_pairs("AGG") == 2, "Test case 4 failed"
    print("✓ Test case 4 passed: 'AGG' -> 2")

    assert count_ag_pairs("AAAGGG") == 9, "Test case 5 failed"
    print("✓ Test case 5 passed: 'AAAGGG' -> 9")

    print("\n✅ All test cases passed!")
