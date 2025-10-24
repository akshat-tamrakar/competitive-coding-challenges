""" 167
Two Sum II
==========
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length. Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2. The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""

from printopia import print_return


@print_return
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


two_sum(numbers=[2, 7, 11, 15], target=9)  # [1, 2]
two_sum(numbers=[2, 3, 4], target=6)  # [1, 3]
two_sum(numbers=[-1, 0], target=-1)  # [1, 2]
