"""
LeetCode Problem #260: Single Number III
Difficulty: Medium
Link: https://leetcode.com/problems/single-number-iii

Every element appears twice, except two numbers that appear only once. Find those two numbers.
"""


def single_number(nums: list[int]) -> list[int]:
    return single_number_1(nums)


def single_number_1(nums: list[int]) -> list[int]:
    xor_all = 0
    for num in nums:
        xor_all ^= num

    diff = xor_all & -xor_all
    a = b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num
    return [a, b]


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]  # Output: [3,5]
    print(f"The single number in {nums} is: {single_number(nums)}")

    nums = [-1, 0]  # Output: [-1,0]
    print(f"The single number in {nums} is: {single_number(nums)}")

"""
EXPLAINATION 1
--------------
1. XOR all numbers
   → x ^ y

2. Find rightmost set bit
   diff = xor_all & -xor_all

3. Divide numbers based on that bit

4. XOR each group separately

Answer = two unique numbers

"""
