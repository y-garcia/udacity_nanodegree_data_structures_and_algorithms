def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number != int(number) or number < 0:
        print("Only positive integer numbers allowed")
        return None

    return sqrt_rec(number, 0, number)


def sqrt_rec(target, lower, upper):
    base = (lower + upper) // 2
    squared = base ** 2
    next_squared = (base + 1) ** 2

    if squared <= target < next_squared:
        return base

    elif squared < target:
        return sqrt_rec(target, base + 1, upper)

    elif squared > target:
        return sqrt_rec(target, lower, base - 1)


test_cases = [
    (9, 3),
    (0, 0),
    (16, 4),
    (1, 1),
    (27, 5),
    (-9, None),
    (4.5, None),
]
for test_case in test_cases:
    number, expected = test_case
    result = sqrt(number)
    print(f"Testing sqrt({number}) = {result} \t", "Pass" if (result == expected) else f"Fail: actual = {result}, expected = {expected}")