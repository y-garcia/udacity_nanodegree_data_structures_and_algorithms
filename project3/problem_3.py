def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) == 0:
        return []

    sorted_list = merge_sort(input_list, 0, len(input_list) - 1)

    return get_numbers(sorted_list)


def merge_sort(input_list, start, end):
    if start > end or start < 0 or end >= len(input_list):
        return []

    if start == end:
        return [input_list[start]]

    midpoint = (start + end) // 2
    left = merge_sort(input_list, start, midpoint)
    right = merge_sort(input_list, midpoint + 1, end)

    return merge(left, right)


def merge(left, right):
    merged = []

    l, r = 0, 0
    while l < len(left) and r < len(right):
        left_number = left[l]
        right_number = right[r]

        if left_number >= right_number:
            merged.append(left_number)
            l += 1

        else:
            merged.append(right_number)
            r += 1

    merged.extend(left[l:])
    merged.extend(right[r:])

    return merged


def get_numbers(sorted_list):
    number1 = 0
    number2 = 0

    for i, value in enumerate(sorted_list):
        if i % 2:
            number1 = number1 * 10 + value
        else:
            number2 = number2 * 10 + value

    return [number1, number2]


test_cases = [
    ([1, 2, 3, 4, 5], [542, 31]),
    ([4, 6, 2, 5, 9, 8], [964, 852]),
    ([4, 6, 0, 5, 9, 8], [964, 850]),
    ([], []),
    (None, [])
]

for test_case in test_cases:
    input_value, expected = test_case
    result = rearrange_digits(input_value)
    print(f"rearrange_digits('{input_value}') = '{result}' |",
          "Pass" if sum(result) == sum(expected) else f"Fail! '{expected}' expected")