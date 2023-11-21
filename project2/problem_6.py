class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    if llist_1 is None:
        llist_1 = LinkedList()
    if llist_2 is None:
        llist_2 = LinkedList()

    result = LinkedList()

    node = llist_1.head
    while node:
        result.append(node.value)
        node = node.next

    node = llist_2.head
    while node:
        result.append(node.value)
        node = node.next

    return result


def union_distinct(llist_1, llist_2):
    if llist_1 is None:
        llist_1 = LinkedList()
    if llist_2 is None:
        llist_2 = LinkedList()

    result = LinkedList()
    values = set()

    node = llist_1.head
    while node:
        if node.value not in values:
            result.append(node.value)
        values.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value not in values:
            result.append(node.value)
        values.add(node.value)
        node = node.next

    return result


def intersection(llist_1, llist_2):
    if llist_1 is None:
        llist_1 = LinkedList()
    if llist_2 is None:
        llist_2 = LinkedList()

    result = LinkedList()
    values1 = set()
    values2 = set()

    node = llist_2.head
    while node:
        values2.add(node.value)
        node = node.next

    node = llist_1.head
    while node:
        if node.value not in values1 and node.value in values2:
            result.append(node.value)
        values1.add(node.value)
        node = node.next

    return result


def print_test_case_result(elements_1, elements_2):
    if elements_1 is None:
        linked_list_1 = None
    else:
        linked_list_1 = LinkedList()
        for i in elements_1:
            linked_list_1.append(i)

    if elements_2 is None:
        linked_list_2 = None
    else:
        linked_list_2 = LinkedList()
        for i in elements_2:
            linked_list_2.append(i)

    union_result = union(linked_list_1, linked_list_2)
    union_distinct_result = union_distinct(linked_list_1, linked_list_2)
    intersection_result = intersection(linked_list_1, linked_list_2)

    print()
    print("linked_list_1    =", linked_list_1)
    print("linked_list_2    =", linked_list_2)
    print()
    print("  union          =", union_result)
    print("  union_distinct =", union_distinct_result)
    print("  intersection   =", intersection_result)

    return str(union_result), str(union_distinct_result), str(intersection_result)


# Test case 1
print("\n1. Test main functionality of union and intersection")
union_result, union_distinct_result, intersection_result = print_test_case_result(
    [3, 2, 4, 35, 6, 65, 6, 4, 3, 21],
    [6, 32, 4, 9, 6, 1, 11, 21, 1]
)

assert union_result == \
       "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> "
assert union_distinct_result == "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> "
assert intersection_result == "4 -> 6 -> 21 -> "

# Test case 2
print("\n2. Test for empty intersection")
union_result, union_distinct_result, intersection_result = print_test_case_result(
    [3, 2, 4, 35, 6, 65, 6, 4, 3, 23],
    [1, 7, 8, 9, 11, 21, 1]
)

assert union_result == "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> "
assert union_distinct_result == "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> "
assert intersection_result == ""

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("\n1. Test empty lists")
union_result, union_distinct_result, intersection_result = print_test_case_result(
    [],
    [1, 2, 3, 4]
)

assert union_result == "1 -> 2 -> 3 -> 4 -> "
assert union_distinct_result == "1 -> 2 -> 3 -> 4 -> "
assert intersection_result == ""

union_result, union_distinct_result, intersection_result = print_test_case_result(
    [5, 6, 7, 8],
    []
)

assert union_result == "5 -> 6 -> 7 -> 8 -> "
assert union_distinct_result == "5 -> 6 -> 7 -> 8 -> "
assert intersection_result == ""

union_result, union_distinct_result, intersection_result = print_test_case_result(
    [],
    []
)

assert union_result == ""
assert union_distinct_result == ""
assert intersection_result == ""

# Test Case 2
print("\n2. Test None lists")
# TODO test distinct with intersection

union_result, union_distinct_result, intersection_result = print_test_case_result(
    None,
    [1, 2, 3]
)

assert union_result == "1 -> 2 -> 3 -> "
assert union_distinct_result == "1 -> 2 -> 3 -> "
assert intersection_result == ""

union_result, union_distinct_result, intersection_result = print_test_case_result(
    [4, 5, 6],
    None
)

assert union_result == "4 -> 5 -> 6 -> "
assert union_distinct_result == "4 -> 5 -> 6 -> "
assert intersection_result == ""

union_result, union_distinct_result, intersection_result = print_test_case_result(
    None,
    None
)

assert union_result == ""
assert union_distinct_result == ""
assert intersection_result == ""

# Test Case 3
print("\n3. Test lists with the same values and no intersection")

union_result, union_distinct_result, intersection_result = print_test_case_result(
    [1, 1, 1],
    [2, 2, 2]
)

assert union_result == "1 -> 1 -> 1 -> 2 -> 2 -> 2 -> "
assert union_distinct_result == "1 -> 2 -> "
assert intersection_result == ""

# Test Case 4
print("\n4. Test lists with the same values and intersection")

union_result, union_distinct_result, intersection_result = print_test_case_result(
    [1, 1, 2],
    [2, 3, 3]
)

assert union_result == "1 -> 1 -> 2 -> 2 -> 3 -> 3 -> "
assert union_distinct_result == "1 -> 2 -> 3 -> "
assert intersection_result == "2 -> "
