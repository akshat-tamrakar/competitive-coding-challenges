def binary_search(arr, target, debug=False):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if debug:
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


if __name__ == "__main__":
    assert binary_search([2, 3, 4, 10, 40], 10) == 3, "Test case 1 failed"
    print("✓ Test case 1 passed: [2,3,4,10,40], target=10 -> index 3")

    assert binary_search([2, 4, 8, 16, 32, 68], 16) == 3, "Test case 2 failed"
    print("✓ Test case 2 passed: [2,4,8,16,32,68], target=16 -> index 3")

    assert binary_search([1, 3, 5, 7, 9], 4) is None, "Test case 3 failed"
    print("✓ Test case 3 passed: [1,3,5,7,9], target=4 -> None")

    assert binary_search([1, 2, 3, 4, 5], 1) == 0, "Test case 4 failed"
    print("✓ Test case 4 passed: [1,2,3,4,5], target=1 -> index 0")

    assert binary_search([1, 2, 3, 4, 5], 5) == 4, "Test case 5 failed"
    print("✓ Test case 5 passed: [1,2,3,4,5], target=5 -> index 4")

    assert binary_search([10], 10) == 0, "Test case 6 failed"
    print("✓ Test case 6 passed: [10], target=10 -> index 0")

    assert binary_search([1, 2], 3) is None, "Test case 7 failed"
    print("✓ Test case 7 passed: [1,2], target=3 -> None")

    print("\n✅ All test cases passed!")
