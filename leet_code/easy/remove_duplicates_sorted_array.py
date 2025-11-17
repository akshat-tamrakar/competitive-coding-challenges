"""
LeetCode Problem #26: Remove Duplicates from Sorted Array
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Example 1:
Input: nums = [1,1,2] || Output: 2, nums = [1,2,_] || Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4] || Output: 5, nums = [0,1,2,3,4,_,_,_,_,_] || Explanation: Your function should return k = 5.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
"""

def remove_duplicates_original(nums: list[int]) -> int:
    if not nums:
        return 0
    
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k

def remove_duplicates_set_based(nums: list[int]) -> int:
    if not nums:
        return 0
    
    seen = set()
    k = 0
    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[k] = num
            k += 1
    return k


if __name__ == "__main__":
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1],
        [1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5]
    ]
    
    methods = [
        ("Two-Pointer", remove_duplicates_original),
        ("Set-Based", remove_duplicates_set_based),
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_case}")
        
        for method_name, method in methods:
            nums_copy = test_case.copy()
            k = method(nums_copy)
            print(f"  {method_name}: k={k}, result={nums_copy[:k]}")
