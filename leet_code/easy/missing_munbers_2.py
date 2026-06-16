"""
LeetCode Problem #448: Find All Numbers Disappeared in an Array
Difficulty: Easy
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

Problem Statement:
    Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1: Input: nums = [4,3,2,7,8,2,3,1]      | Output: [5,6]
Example 2: Input: nums = [1,1]                  | Output: [2]
Example 3: Input: nums = [1,2,3,4,5,6,7,8,9]    | Output: [10]
"""


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    return find_disappeared_numbers_4(nums)


def find_disappeared_numbers_1(nums: list[int]) -> list[int]:
    n = len(nums)
    all = set(nums)
    missing = []
    for i in range(1, n + 1):
        if i not in all:
            print("added")
            missing.append(i)

    return missing


def find_disappeared_numbers_2(nums: list[int]) -> list[int]:
    all = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in all]


def find_disappeared_numbers_3(nums: list[int]) -> list[int]:
    arr = [0] * (len(nums) + 1)

    for n in nums:
        arr[n] = 1

    results = []
    for i in range(1, len(nums) + 1):
        if arr[i] == 0:
            results.append(i)
    return results


def find_disappeared_numbers_4(nums: list[int]) -> list[int]:
    for x in nums:
        temp = abs(x) - 1
        if nums[temp] > 0:
            nums[temp] *= -1

    return [(i + 1) for i, n in enumerate(nums) if n > 0]


if __name__ == "__main__":
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]  # [5, 6]
    print(f"The missing number in {nums1} is: {find_disappeared_numbers(nums1)}")

    # nums2 = [1, 1]  # [2]
    # print(f"The missing number in {nums2} is: {find_disappeared_numbers(nums2)}")

    # nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # []
    # print(f"The missing number in {nums3} is: {find_disappeared_numbers(nums3)}")
