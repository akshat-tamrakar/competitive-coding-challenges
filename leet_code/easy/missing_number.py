""" "
LeetCode Problem #268: Missing Number
Difficulty: Easy
Link: https://leetcode.com/problems/missing-number

268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""


def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    nums1 = [3, 0, 1]
    print(f"The missing number in {nums1} is: {find_missing_number(nums1)}")

    nums2 = [0, 1]
    print(f"The missing number in {nums2} is: {find_missing_number(nums2)}")

    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"The missing number in {nums3} is: {find_missing_number(nums3)}")
