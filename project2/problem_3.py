import sys
from heapq import heapify, heappop


class Node:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.encoding = None
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.char}, {self.frequency})"


class MinHeap:
    def __init__(self, nodes=None):
        self.heap = [] if nodes is None else nodes
        self.heapify_down()

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
        smallest_index = index
        left_index = index * 2 + 1
        right_index = index * 2 + 2

        smallest = self.heap[smallest_index] if smallest_index < self.size() else None
        left = self.heap[left_index] if left_index < self.size() else None
        right = self.heap[right_index] if right_index < self.size() else None

        if smallest and left and smallest.frequency > left.frequency:
            smallest_index = left_index

        if smallest and right and smallest.frequency > right.frequency:
            smallest_index = right_index

        if index != smallest_index:
            self.swap(index, smallest_index)

        if left:
            self.heapify_down(left_index)
        if right:
            self.heapify_down(right_index)

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


def huffman_encoding(data):
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


def traverse(node, encoding=""):

    if node.left:
        traverse(node.left, encoding + "0")

    if node.right:
        traverse(node.right, encoding + "1")

    if node.char:
        node.encoding = encoding


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


def huffman_decoding(data, tree):
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
myheap = MinHeap()
myheap.insert(Node("a", 40))
myheap.insert(Node("b", 30))
myheap.insert(Node("c", 20))
myheap.insert(Node("d", 10))
print(myheap)
print(myheap.pop())
print(myheap)
print(myheap.pop())
print(myheap)
print(myheap.pop())
print(myheap)
print(myheap.pop())
print(myheap)

# TODO this test is no longer needed, since we are not using python methods for the heap
myheap = [40, 30, 20, 10]
heapify(myheap)
print(myheap)
print(heappop(myheap))
print(myheap)
print(heappop(myheap))
print(myheap)
print(heappop(myheap))
print(myheap)
print(heappop(myheap))
print(myheap)
# Test Case 2
# TODO test the huffmann tree is created correctly

# Test Case 3
