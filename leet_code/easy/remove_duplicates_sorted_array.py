"""
LeetCode Easy: Remove Duplicates from Sorted Array
Problem: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Return k after placing the final result in the first k slots of nums.
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

