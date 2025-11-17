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
    nums1 = [1, 1, 2]
    assert remove_duplicates_original(nums1) == 2 and nums1[:2] == [1, 2], "Test case 1 failed"
    print("✓ Test case 1 passed: [1,1,2] -> k=2, [1,2]")
    
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates_original(nums2) == 5 and nums2[:5] == [0, 1, 2, 3, 4], "Test case 2 failed"
    print("✓ Test case 2 passed: [0,0,1,1,1,2,2,3,3,4] -> k=5, [0,1,2,3,4]")
    
    nums3 = [1]
    assert remove_duplicates_original(nums3) == 1 and nums3[:1] == [1], "Test case 3 failed"
    print("✓ Test case 3 passed: [1] -> k=1, [1]")
    
    nums4 = [1, 1, 1, 1, 1]
    assert remove_duplicates_original(nums4) == 1 and nums4[:1] == [1], "Test case 4 failed"
    print("✓ Test case 4 passed: [1,1,1,1,1] -> k=1, [1]")
    
    nums5 = [1, 2, 3, 4, 5]
    assert remove_duplicates_original(nums5) == 5 and nums5[:5] == [1, 2, 3, 4, 5], "Test case 5 failed"
    print("✓ Test case 5 passed: [1,2,3,4,5] -> k=5, [1,2,3,4,5]")
    
    nums6 = [1, 1, 2]
    assert remove_duplicates_set_based(nums6) == 2 and nums6[:2] == [1, 2], "Test case 6 failed"
    print("✓ Test case 6 passed: set_based method -> k=2, [1,2]")
    
    print("\n✅ All test cases passed!")
