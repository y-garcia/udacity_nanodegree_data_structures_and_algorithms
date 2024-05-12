import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    minimum = None
    maximum = None

    for number in ints:
        if minimum is None or number < minimum:
            minimum = number
        if maximum is None or number > maximum:
            maximum = number

    return minimum, maximum


# Example Test Case of Ten Integers
lst = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(lst)

test_cases = [
    (lst, (0, 9)),
    ([2], (2, 2)),
    ([2, 1], (1, 2)),
    ([-1, -2], (-2, -1)),
    ([], (None, None))
]

for test_case in test_cases:
    input_value, expected = test_case
    result = get_min_max(input_value)
    print(f"get_min_max({input_value}) = {result} |",
          "Pass" if result == expected else f"Fail! '{expected}' expected")
