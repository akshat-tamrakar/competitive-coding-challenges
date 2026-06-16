"""
LeetCode Problem #137. Single Number II
Difficulty: Medium
Link: https://leetcode.com/problems/single-number-ii

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it. You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1: Input: nums = [2,2,3,2]     |Output: 3
Example 2: Input: nums = [0,1,0,1,0,1,99]      |Output: 99
"""


def single_number(nums: list[int]) -> int:
    return single_number_1(nums)


def single_number_1(nums: list[int]) -> int:
    ans = 0
    for i in range(32):
        count = 0
        for num in nums:
            if (num >> i) & 1:
                count += 1

        if count % 3:
            ans |= 1 << i

    return ans


def single_number_2(nums):
    ones = twos = 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones


if __name__ == "__main__":
    nums = [2, 2, 3, 2]  # Output: 3
    print(f"The single number in {nums} is: {single_number(nums)}")

    nums = [0, 1, 0, 1, 0, 1, 99]  # Output: 99
    print(f"The single number in {nums} is: {single_number(nums)}")

"""
EXPLAINATION 1
--------------
Idea: Count the number of 1s at each bit position.

Since every number except one appears 3 times, duplicate numbers contribute bits in multiples of 3.

count_of_1s_at_bit_i % 3
0 → unique number has 0 at that bit.
1 → unique number has 1 at that bit.

Reconstruct the answer from these remaining bits.

Example:

[2,2,3,2]

2 = 10
2 = 10
3 = 11
2 = 10
-------
Count of 1s:
Left bit  = 4
Right bit = 1

4 % 3 = 1
1 % 3 = 1

Result = 11 = 3
"""

"""
EXPLAINATION 2
--------------
ones: bits seen once
twos: bits seen twice

For each number:
    ones = (ones ^ num) & ~twos
    twos = (twos ^ num) & ~ones

Bit state:
0 times → ones → twos → removed → repeat

Answer = ones

In interviews, the bit-counting modulo-3 approach is usually easier to explain. The ones/twos method is more elegant and avoids the explicit 32-bit loop.
"""
