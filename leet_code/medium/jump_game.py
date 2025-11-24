"""
LeetCode Problem #55: Jump Game
Difficulty: Medium
Link: https://leetcode.com/problems/jump-game/

Problem Statement:
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4] || Output: true || Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4] || Output: false || Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5
"""


def can_jump_1(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return max_reach >= len(nums) - 1


def can_jump_2(nums):
    n = len(nums)
    if n <= 1:  # Base case: If the array has 0 or 1 element, you're already there
        return True

    max_reach = 0  # Keep track of the farthest index you can reach

    for i in range(n):
        if (
            i > max_reach
        ):  # If the current index is beyond the maximum reach, you're stuck
            return False

        max_reach = max(max_reach, i + nums[i])  # Update the maximum reachable index

        if (
            max_reach >= n - 1
        ):  # If you can reach or surpass the last index, you're done
            return True

    return False  # If you've iterated through the array and haven't reached the end, it's impossible


if __name__ == "__main__":
    assert can_jump_1([2, 3, 1, 1, 4]), "Test case 1 failed"
    print("✓ Test case 1 passed: [2,3,1,1,4] -> True")

    assert not can_jump_1([3, 2, 1, 0, 4]), "Test case 2 failed"
    print("✓ Test case 2 passed: [3,2,1,0,4] -> False")

    assert can_jump_1([2, 0, 1, 2]), "Test case 3 failed"
    print("✓ Test case 3 passed: [2,0,1,2] -> True")

    assert can_jump_1([0]), "Test case 4 failed"
    print("✓ Test case 4 passed: [0] -> True")

    assert can_jump_1([2, 0, 0]), "Test case 5 failed"
    print("✓ Test case 5 passed: [2,0,0] -> True")

    assert can_jump_2([2, 3, 1, 1, 4]), "Test case 6 failed"
    print("✓ Test case 6 passed: can_jump_2 method -> True")

    assert not can_jump_2([3, 2, 1, 0, 4]), "Test case 7 failed"
    print("✓ Test case 7 passed: can_jump_2 method -> False")

    print("\n✅ All test cases passed!")
