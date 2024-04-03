def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    smallest = find_pivot(input_list, 0, len(input_list) - 1)
    largest = smallest - 1

    if smallest == -1 or input_list[smallest] > number > input_list[largest]:
        return -1

    if input_list[smallest] <= number <= input_list[-1]:
        return binary_search(input_list, number, smallest, len(input_list) - 1)

    return binary_search(input_list, number, 0, largest)


def find_pivot(input_list, start, end):
    if start < 0 or end >= len(input_list) or start > end:
        return -1

    midpoint = (start + end) // 2
    mid_value = input_list[midpoint]
    next_value = None if midpoint == len(input_list) - 1 else input_list[midpoint + 1]
    prev_value = None if midpoint == 0 else input_list[midpoint - 1]

    if next_value is not None and mid_value > next_value:
        return midpoint + 1
    elif prev_value is not None and prev_value > mid_value:
        return midpoint

    pivot = find_pivot(input_list, start, midpoint - 1)

    if pivot == -1:
        pivot = find_pivot(input_list, midpoint + 1, end)

    if pivot == -1:
        return 0

    return pivot


def binary_search(input_list, number, start, end):
    if start < 0 or end >= len(input_list) or start > end:
        return -1

    midpoint = (start + end) // 2
    midvalue = input_list[midpoint]

    if number < midvalue:
        return binary_search(input_list, number, start, midpoint - 1)
    elif number > midvalue:
        return binary_search(input_list, number, midpoint + 1, end)
    else:
        return midpoint


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

test_function([[6, 7, 8, 1, 2, 3, 4], 0])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 2])
test_function([[6, 7, 8, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])
test_function([[6, 7, 8, 1, 2, 3, 4], 5])
test_function([[6, 7, 8, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 1, 2, 3, 4], 7])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 9])

test_function([[1, 2, 3, 4, 6, 7, 8], 0])
test_function([[1, 2, 3, 4, 6, 7, 8], 1])
test_function([[1, 2, 3, 4, 6, 7, 8], 2])
test_function([[1, 2, 3, 4, 6, 7, 8], 3])
test_function([[1, 2, 3, 4, 6, 7, 8], 4])
test_function([[1, 2, 3, 4, 6, 7, 8], 5])
test_function([[1, 2, 3, 4, 6, 7, 8], 6])
test_function([[1, 2, 3, 4, 6, 7, 8], 7])
test_function([[1, 2, 3, 4, 6, 7, 8], 8])
test_function([[1, 2, 3, 4, 6, 7, 8], 9])
