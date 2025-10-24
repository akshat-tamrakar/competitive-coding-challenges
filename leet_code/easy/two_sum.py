# LeetCode/Easy/two_sum.py
from typing import Union, Any


class Solution:
    @staticmethod
    def two_sum_1(nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

    @staticmethod
    def two_sum_2(nums: list[int], target: int) -> Union[tuple[Any, int], tuple[()]]:
        seen_numbers_map = {}
        for current_index, current_number in enumerate(nums):
            if (required_number := target - current_number) in seen_numbers_map:
                return seen_numbers_map[required_number], current_index
            seen_numbers_map[current_number] = current_index
        return ()


if __name__ == "__main__":
    print(Solution().two_sum_1(nums=[2, 7, 11, 15],target= 9))
    print(Solution().two_sum_2(nums=[2, 7, 11, 15], target=9))
    print(Solution().two_sum_1(nums=[2, 7, 11, 15], target=9))  # Expected output: [0, 1] (because 2 + 7 = 9)
    print(Solution().two_sum_2(nums=[3, 2, 4], target=6))
