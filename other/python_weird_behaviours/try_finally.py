def return_in_finally():
    try:
        return 1  # This is returned
    finally:
        result = 10


def return_override_in_finally():
    try:
        return 1  # This return is ignored because the finally block has its own return
    finally:
        return 2  # The return statement in the finally block overrides the try block


def exception_handling_with_finally():
    try:
        raise ValueError()  # An exception is raised
    except ValueError:
        # The return here is ignored because the finally block has its own return
        return 1
    finally:
        return 3  # The return statement in the finally block takes precedence


def return_before_try():
    return 0  # This return is executed before entering the try-except-finally block
    try:
        raise ValueError()  # This code is unreachable due to the return above
    except ValueError:
        return 1
    finally:
        return 3


if __name__ == "__main__":
    assert return_in_finally() == 1, "Test case 1 failed"
    print("✓ Test case 1 passed: return_in_finally() -> 1 (try block return)")

    assert return_override_in_finally() == 2, "Test case 2 failed"
    print(
        "✓ Test case 2 passed: return_override_in_finally() -> 2 (finally overrides try)"
    )

    assert exception_handling_with_finally() == 3, "Test case 3 failed"
    print(
        "✓ Test case 3 passed: exception_handling_with_finally() -> 3 (finally overrides except)"
    )

    assert return_before_try() == 0, "Test case 4 failed"
    print("✓ Test case 4 passed: return_before_try() -> 0 (early return)")

    print("\n✅ All test cases passed!")
    print("\nKey Takeaway: In Python, a return statement in a finally block")
    print("overrides any return statement in try or except blocks.")
