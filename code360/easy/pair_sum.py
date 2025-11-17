"""
Code360 Problem: Pair Sum
Difficulty: Easy
Link: https://www.naukri.com/code360/problems/pair-sum_697295

Problem Statement:
You are given an integer array 'ARR' of size 'N' and an integer 'S'. Your task is to return the list of all pairs of elements such that each sum of elements of each pair equals 'S'.
Each pair should be sorted i.e the first value should be less than or equals to the second value.
Return the list of pairs sorted in non-decreasing order of their first value. In case if two pairs have the same first value, the pair with a smaller second value should come first.

Sample Input:
5 5
1 2 3 4 5

Sample Output:
1 4
2 3

Explanation:
Here, 1 + 4 = 5 and 2 + 3 = 5. Hence the output will be (1, 4), (2, 3).

Constraints:
- 1 <= N <= 10^3
- -10^5 <= ARR[i] <= 10^5
- -2 * 10^5 <= S <= 2 * 10^5
"""


def find_pairs_with_sum(array, target_sum):
    result_pairs = []
    checked_numbers = []

    for number in array:
        print()
        if number not in checked_numbers:
            print(number)
            if (complement := target_sum - number) in array:
                sorted_pair = sorted([number, complement])
                # print(sorted_pair)
                result_pairs.append(sorted_pair)

            checked_numbers.append(number)
    result_pairs.sort()
    return result_pairs


def pair_sum(array, target_sum):
    frequency_map = {}
    pairs_list = []

    for current_value in array:
        complement_value = target_sum - current_value
        # Check if 'complement_value' is present in the dictionary
        if complement_value in frequency_map:
            for _ in range(
                frequency_map[complement_value]
            ):  # Add the pair for each occurrence of 'complement_value'
                pairs_list.append(
                    (
                        min(current_value, complement_value),
                        max(current_value, complement_value),
                    )
                )

        # Update the frequency of 'current_value'
        if current_value in frequency_map:
            frequency_map[current_value] += 1
        else:
            frequency_map[current_value] = 1

    # Sort the result based on the criteria
    pairs_list.sort()
    return pairs_list


if __name__ == "__main__":
    assert pair_sum([1, 2, 3, 4, 5], 5) == [(1, 4), (2, 3)], "Test case 1 failed"
    print("✓ Test case 1 passed: [1,2,3,4,5], target=5 -> [(1,4), (2,3)]")

    assert pair_sum([2, -3, 3, 3, -2], 0) == [(-3, 3), (-3, 3), (-2, 2)], (
        "Test case 2 failed"
    )
    print("✓ Test case 2 passed: [2,-3,3,3,-2], target=0 -> [(-3,3), (-3,3), (-2,2)]")

    assert pair_sum([2, -6, 2, 5, 2], 4) == [(2, 2), (2, 2), (2, 2)], (
        "Test case 3 failed"
    )
    print("✓ Test case 3 passed: [2,-6,2,5,2], target=4 -> [(2,2), (2,2), (2,2)]")

    assert pair_sum([1, 3, 2, 2], 4) == [(1, 3), (2, 2)], "Test case 4 failed"
    print("✓ Test case 4 passed: [1,3,2,2], target=4 -> [(1,3), (2,2)]")

    assert pair_sum([1, 1, 1, 1], 2) == [
        (1, 1),
        (1, 1),
        (1, 1),
        (1, 1),
        (1, 1),
        (1, 1),
    ], "Test case 5 failed"
    print("✓ Test case 5 passed: [1,1,1,1], target=2 -> 6 pairs of (1,1)")

    print("\n✅ All test cases passed!")
