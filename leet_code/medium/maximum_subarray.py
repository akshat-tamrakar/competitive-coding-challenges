"""
LeetCode Problem #53: Maximum Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Problem Statement:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4] || Output: 6 || Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1] || Output: 1 || Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8] || Output: 23 || Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""


def maxSubArray(nums):
    max_sum = float("-inf")  # Initialize to negative infinity
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0  # Reset current_sum if it becomes negative

    return max_sum


if __name__ == "__main__":
    assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Test case 1 failed"
    print("✓ Test case 1 passed: [-2,1,-3,4,-1,2,1,-5,4] -> 6")

    assert maxSubArray([1]) == 1, "Test case 2 failed"
    print("✓ Test case 2 passed: [1] -> 1")

    assert maxSubArray([5, 4, -1, 7, 8]) == 23, "Test case 3 failed"
    print("✓ Test case 3 passed: [5,4,-1,7,8] -> 23")

    assert maxSubArray([-1]) == -1, "Test case 4 failed"
    print("✓ Test case 4 passed: [-1] -> -1")

    assert maxSubArray([-2, -1]) == -1, "Test case 5 failed"
    print("✓ Test case 5 passed: [-2,-1] -> -1")

    print("\n✅ All test cases passed!")
