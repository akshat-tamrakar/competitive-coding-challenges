"""
LeetCode Problem #169: Majority Element
Difficulty: Easy
Link: https://leetcode.com/problems/majority-element/

Problem Statement:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3] || Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2] || Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from collections import Counter


def majority_element_1(nums: list[int]) -> int:
    """
    Approach 1: Hash Map / Counter
    Time Complexity: O(n) - iterate through array once
    Space Complexity: O(n) - store counts in hash map
    """
    counts = Counter(nums)
    return counts.most_common(1)[0][0]


def majority_element_2(nums: list[int]) -> int:
    """
    Approach 2: Hash Map with early exit
    Time Complexity: O(n) - iterate through array once
    Space Complexity: O(n) - store counts in hash map
    """
    counts = {}
    majority_threshold = len(nums) // 2

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > majority_threshold:
            return num

    return -1  # Should never reach here based on problem constraints


def majority_element_3(nums: list[int]) -> int:
    """
    Approach 3: Sorting
    Time Complexity: O(n log n) - sorting the array
    Space Complexity: O(1) or O(n) depending on sorting algorithm
    """
    nums.sort()
    return nums[len(nums) // 2]


def majority_element_4(nums: list[int]) -> int:
    """
    Approach 4: Boyer-Moore Voting Algorithm (Optimal)
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using two variables

    The algorithm works by maintaining a candidate and count:
    - If count is 0, set current element as candidate
    - If current element matches candidate, increment count
    - Otherwise, decrement count
    The majority element will always be the final candidate
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


def majority_element_5(nums: list[int]) -> int:
    """
    Approach 5: Divide and Conquer
    Time Complexity: O(n log n) - divide array log n times, each level processes n elements
    Space Complexity: O(log n) - recursion stack
    """

    def majority_element_rec(left: int, right: int) -> int:
        # Base case: single element
        if left == right:
            return nums[left]

        # Divide
        mid = (left + right) // 2
        left_majority = majority_element_rec(left, mid)
        right_majority = majority_element_rec(mid + 1, right)

        # Conquer: if both halves agree, return that element
        if left_majority == right_majority:
            return left_majority

        # Otherwise, count occurrences in current range
        left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
        right_count = sum(
            1 for i in range(left, right + 1) if nums[i] == right_majority
        )

        return left_majority if left_count > right_count else right_majority

    return majority_element_rec(0, len(nums) - 1)


def majority_element(nums: list[int]) -> int:
    # return majority_element_1(nums)
    # return majority_element_2(nums)
    # return majority_element_3(nums)
    # return majority_element_4(nums)
    return majority_element_5(nums)


if __name__ == "__main__":
    result1 = majority_element(nums=[3, 2, 3])
    assert result1 == 3, f"Test case 1 failed: expected 3, got {result1}"
    print("✓ Test case 1 passed: nums=[3,2,3] -> 3")

    result2 = majority_element(nums=[2, 2, 1, 1, 1, 2, 2])
    assert result2 == 2, f"Test case 2 failed: expected 2, got {result2}"
    print("✓ Test case 2 passed: nums=[2,2,1,1,1,2,2] -> 2")

    result3 = majority_element(nums=[1])
    assert result3 == 1, f"Test case 3 failed: expected 1, got {result3}"
    print("✓ Test case 3 passed: nums=[1] -> 1")

    result4 = majority_element(nums=[6, 5, 5])
    assert result4 == 5, f"Test case 4 failed: expected 5, got {result4}"
    print("✓ Test case 4 passed: nums=[6,5,5] -> 5")

    result5 = majority_element(nums=[1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3])
    assert result5 == 3, f"Test case 5 failed: expected 3, got {result5}"
    print("✓ Test case 5 passed: nums=[1,1,1,2,2,3,3,3,3,3,3,3] -> 3")

    print("\n✅ All test cases passed!")
