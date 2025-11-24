"""
LeetCode Problem #167: Two Sum II - Input Array Is Sorted
Difficulty: Medium
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem Statement:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

Example 1:
Input: numbers = [2,7,11,15], target = 9 || Output: [1,2] || Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6 || Output: [1,3] || Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1 || Output: [1,2] || Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.
"""


def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-based indexing
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    assert two_sum(numbers=[2, 7, 11, 15], target=9) == [1, 2], "Test case 1 failed"
    print("✓ Test case 1 passed: [2,7,11,15], target=9 -> [1,2]")

    assert two_sum(numbers=[2, 3, 4], target=6) == [1, 3], "Test case 2 failed"
    print("✓ Test case 2 passed: [2,3,4], target=6 -> [1,3]")

    assert two_sum(numbers=[-1, 0], target=-1) == [1, 2], "Test case 3 failed"
    print("✓ Test case 3 passed: [-1,0], target=-1 -> [1,2]")

    assert two_sum(numbers=[1, 2, 3, 4, 5], target=9) == [4, 5], "Test case 4 failed"
    print("✓ Test case 4 passed: [1,2,3,4,5], target=9 -> [4,5]")

    assert two_sum(numbers=[5, 25, 75], target=100) == [2, 3], "Test case 5 failed"
    print("✓ Test case 5 passed: [5,25,75], target=100 -> [2,3]")

    print("\n✅ All test cases passed!")
