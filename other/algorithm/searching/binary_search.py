from printopia import print_return


@print_return
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        print(f"left: {left}, mid: {mid}, right: {right} \t {arr[mid]} || {target}")

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target not found
    return None


result = binary_search([2, 3, 4, 10, 40], 10)
result = binary_search([2, 4, 8, 16, 32, 68], 16)
result = binary_search([1, 3, 5, 7, 9], 4)
result = binary_search([1, 2, 3, 4, 5], 1)
