from printopia import print_return


@print_return
def return_in_finally():
    try:
        return 1  # This is returned
    finally:
        result = 10


@print_return
def return_override_in_finally():
    try:
        return 1  # This return is ignored because the finally block has its own return
    finally:
        return 2  # The return statement in the finally block overrides the try block


@print_return
def exception_handling_with_finally():
    try:
        raise ValueError()  # An exception is raised
    except ValueError:
        # The return here is ignored because the finally block has its own return
        return 1
    finally:
        return 3  # The return statement in the finally block takes precedence


@print_return
def return_before_try():
    return 0  # This return is executed before entering the try-except-finally block
    try:
        raise ValueError()  # This code is unreachable due to the return above
    except ValueError:
        return 1
    finally:
        return 3


return_in_finally()  # returns 1
return_override_in_finally()  # returns 2
exception_handling_with_finally()  # returns 3
return_before_try()  # returns 0
