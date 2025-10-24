def maxSubArray(nums):
    max_sum = float("-inf")  # Initialize to negative infinity
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0  # Reset current_sum if it becomes negative

    return max_sum
