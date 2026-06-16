"""
LeetCode Problem #136. Single Number
Difficulty: Easy
Link: https://leetcode.com/problems/single-number

Problem Statement:
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1: Input: nums = [2,2,1]        | Output: 1
Example 2: Input: nums = [4,1,2,1,2]    | Output: 4
Example 3: Input: nums = [1]            | Output: 1
"""


def single_number(nums: list[int]) -> int:
    return single_number_2(nums)


def single_number_1(nums: list[int]) -> int:
    return (2 * sum(set(nums))) - sum(nums)


def single_number_2(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    nums = [2, 2, 1]  # Output: 1
    print(f"The single number in {nums} is: {single_number(nums)}")

    nums = [4, 1, 2, 1, 2]  # Output: 4
    print(f"The single number in {nums} is: {single_number(nums)}")

    nums = [1]  # Output: 1
    print(f"The single number in {nums} is: {single_number(nums)}")
