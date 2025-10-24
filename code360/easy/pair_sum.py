"""
You are given an integer array 'ARR' of size 'N' and an integer 'S'. Your task is to return the list of all pairs of elements such that each sum of elements of each pair equals 'S'. Each pair should be sorted i.e the first value should be less than or equals to the second value. Return the list of pairs sorted in non-decreasing order of their first value. In case if two pairs have the same first value, the pair with a smaller second value should come first.

5 5
1 2 3 4 5
Sample Output
1 4
2 3
"""

from printopia import print_return


@print_return
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


@print_return
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


pair_sum([1, 2, 3, 4, 5], 5)  # [[1, 4], [2, 3]]
pair_sum([2, -3, 3, 3, -2], 0)  # [[-3, 3], [-3, 3], [-2, 2]]
pair_sum([2, -6, 2, 5, 2], 4)  # [[2, 2], [2, 2], [2, 2]]
