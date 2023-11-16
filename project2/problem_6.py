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
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in elements_1:
        linked_list_1.append(i)

    for i in elements_2:
        linked_list_2.append(i)

    union_result = union(linked_list_1, linked_list_2)
    union_distinct_result = union_distinct(linked_list_1, linked_list_2)
    intersection_result = intersection(linked_list_1, linked_list_2)

    print("linked_list_1    =", linked_list_1)
    print("linked_list_2    =", linked_list_2)
    print()
    print("  union          =", union_result)
    print("  union_distinct =", union_distinct_result)
    print("  intersection   =", intersection_result)

    return str(union_result), str(union_distinct_result), str(intersection_result)


# Test case 1
print("\n1. Test main functionality of union and intersection\n")
union_result, union_distinct_result, intersection_result = print_test_case_result(
    [3, 2, 4, 35, 6, 65, 6, 4, 3, 21],
    [6, 32, 4, 9, 6, 1, 11, 21, 1]
)

assert union_result == \
       "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> "
assert union_distinct_result == "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> "
assert intersection_result == "4 -> 6 -> 21 -> "

# Test case 2
print("\n2. Test for empty intersection\n")
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
print("\n1. Test empty lists\n")
union_result, union_distinct_result, intersection_result = print_test_case_result(
    [],
    [1, 2, 3, 4]
)

assert union_result == "1 -> 2 -> 3 -> 4 -> "
assert union_distinct_result == "1 -> 2 -> 3 -> 4 -> "
assert intersection_result == ""

print()
union_result, union_distinct_result, intersection_result = print_test_case_result(
    [5, 6, 7, 8],
    []
)

assert union_result == "5 -> 6 -> 7 -> 8 -> "
assert union_distinct_result == "5 -> 6 -> 7 -> 8 -> "
assert intersection_result == ""

# Test Case 2
# TODO test distinct with intersection

# Test Case 3
# TODO test distinct without intersection
