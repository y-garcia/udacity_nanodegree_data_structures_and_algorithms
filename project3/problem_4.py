def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_0 = 0
    next_2 = len(input_list)-1
    current_index = 0

    while current_index <= next_2:

        if input_list[current_index] == 0:
            swap(input_list, next_0, current_index)
            next_0 += 1
            current_index += 1

        elif input_list[current_index] == 2:
            swap(input_list, next_2, current_index)
            next_2 -= 1

        else:
            current_index += 1

    return input_list


def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_cases = [
    [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2],
    [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
]

for test_case in test_cases:
    input_value = test_case
    input_str = str(input_value)
    expected = sorted(input_value)
    result = sort_012(input_value)
    print(f"sort_012({input_str})\n       = {result} |",
          "Pass" if result == expected else f"Fail! '{expected}' expected")
