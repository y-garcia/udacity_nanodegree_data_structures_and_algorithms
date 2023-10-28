import sys


class Node:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.encoding = None
        self.left = None
        self.right = None

    def __repr__(self):
        attributes = []
        if self.char is not None:
            attributes.append(self.char)
        if self.frequency is not None:
            attributes.append(str(self.frequency))
        if self.encoding is not None:
            attributes.append(self.encoding)
        return "(" + ', '.join(attributes) + ")"


class MinHeap:
    def __init__(self, nodes=None):
        self.heap = [] if nodes is None else nodes
        self.heapify()

    def insert(self, node):
        self.heap.append(node)
        self.heapify_up()

    def heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2

            if self.heap[parent_index].frequency >= self.heap[index].frequency:
                self.swap(parent_index, index)
                index = parent_index
            else:
                break

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_down(self, index=0):
        if index < 0 or index >= self.size():
            return

        smallest_index = index
        left_index = index * 2 + 1
        right_index = index * 2 + 2

        smallest = self.get(smallest_index)
        left = self.get(left_index)
        right = self.get(right_index)

        if smallest and left and smallest.frequency >= left.frequency:
            smallest_index = left_index
            smallest = self.get(smallest_index)

        if smallest and right and smallest.frequency >= right.frequency:
            smallest_index = right_index

        if index != smallest_index:
            self.swap(index, smallest_index)
            self.heapify_down(smallest_index)

    def heapify(self):
        for i in range(self.size() - 1, -1, -1):
            self.heapify_down(i)

    def get(self, index):
        if index < 0 or index >= self.size():
            return None

        return self.heap[index]

    def pop(self):
        if self.is_empty():
            return None

        root = self.heap.pop(0)
        self.heapify_down()
        return root

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def __repr__(self):
        return str(self.heap)


def traverse(node, encoding=""):
    if node.left:
        traverse(node.left, encoding + "0")

    if node.right:
        traverse(node.right, encoding + "1")

    if node.char:
        node.encoding = encoding


def print_tree(node, level=0):
    if node is not None:
        print("  " * level + str(node))
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)


def create_huffmann_tree(min_heap):
    huffman_tree = None

    if min_heap.size() == 1:
        huffman_tree = min_heap.pop()

    elif min_heap.size() > 1:

        while not min_heap.is_empty():
            node1 = min_heap.pop()
            node2 = min_heap.pop()
            new_node = Node(char=None, frequency=(node1.frequency + node2.frequency))
            new_node.left = node1
            new_node.right = node2

            if min_heap.is_empty():
                huffman_tree = new_node
            else:
                min_heap.insert(new_node)

    return huffman_tree


def huffman_encoding(data):
    if data is None:
        return None, None

    if len(data) == 0:
        return "", None

    nodes = {}

    for char in data:
        node = nodes.setdefault(char, Node(char))
        node.frequency += 1

    min_heap = MinHeap(list(nodes.values()))

    huffman_tree = create_huffmann_tree(min_heap)

    traverse(huffman_tree)

    encoded = ""
    for char in data:
        encoded += nodes[char].encoding

    return encoded, huffman_tree


def huffman_decoding(data, tree):
    if data is None:
        return None

    if len(data) == 0:
        return ""

    if tree is None:
        return None

    decoded = ""

    node = tree
    for bit in data:
        if bit == "0":
            node = node.left
        elif bit == "1":
            node = node.right

        if node.char:
            decoded += node.char
            node = tree

    return decoded


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("\n1. Test correct sorting of MinHeap")
test_nodes = [
    Node("A", 40),
    Node("B", 30),
    Node("C", 20),
    Node("D", 10)
]
print("nodes = ", test_nodes)
test_heap = MinHeap(test_nodes)
print("test_heap = ", test_heap)
assert test_heap.pop().frequency == 10
print("test_heap = ", test_heap)
assert test_heap.pop().frequency == 20
print("test_heap = ", test_heap)
assert test_heap.pop().frequency == 30
print("test_heap = ", test_heap)
assert test_heap.pop().frequency == 40
print("test_heap = ", test_heap)

# Test Case 2
print("\n2. Test correct creation of Huffmann tree")
test_heap = MinHeap([
    Node("A", 7),
    Node("B", 3),
    Node("C", 7),
    Node("D", 2),
    Node("E", 6)
])

print("test_heap = ", test_heap)

test_tree = create_huffmann_tree(test_heap)

assert test_tree.frequency == 25
assert test_tree.left.frequency == 11
assert test_tree.right.frequency == 14
assert test_tree.left.left.frequency == 5
assert test_tree.left.right.frequency == 6 and test_tree.left.right.char == "E"
assert test_tree.right.left.frequency == 7 and test_tree.right.left.char == "A"
assert test_tree.right.right.frequency == 7 and test_tree.right.right.char == "C"
assert test_tree.left.left.left.frequency == 2 and test_tree.left.left.left.char == "D"
assert test_tree.left.left.right.frequency == 3 and test_tree.left.left.right.char == "B"

print("test_tree = ")
print_tree(test_tree)

# Test Case 3
print("\n3. Test correct huffman encoding (also for null or empty input)")
test_data, test_tree = huffman_encoding(None)
assert test_data is None
print(test_data, " = ", None)
assert test_tree is None
print(test_tree, " = ", None)

test_data, test_tree = huffman_encoding("")
assert test_data == ""
print('"'+test_data+'"', ' = ', '""')
assert test_tree is None
print(test_tree, " = ", None)

test_data, test_tree = huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")
assert test_data == "1010101010101000100100111111111111111000000010101010101"
print(test_data, " = ", "1010101010101000100100111111111111111000000010101010101")

print("\n4. Test correct huffman decoding (also for null or empty input)")

test_data = huffman_decoding("", test_tree)
assert test_data == ""
print('"'+test_data+'"', ' = ', '""')

test_data = huffman_decoding("", None)
assert test_data == ""
print('"'+test_data+'"', ' = ', '""')

test_data = huffman_decoding(None, test_tree)
assert test_data is None
print(test_data, ' = ', None)

test_data = huffman_decoding("1010", None)
assert test_data is None
print(test_data, ' = ', None)

test_data = huffman_decoding("1010101010101000100100111111111111111000000010101010101", test_tree)
assert test_data == "AAAAAAABBBCCCCCCCDDEEEEEE"
print(test_data, ' = ', "AAAAAAABBBCCCCCCCDDEEEEEE")